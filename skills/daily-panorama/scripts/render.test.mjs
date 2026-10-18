import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import sharp from 'sharp';
import {validate,wrap,render} from './render.mjs';

const here=path.dirname(fileURLToPath(import.meta.url));
const example=JSON.parse(await fs.readFile(path.join(here,'../assets/example/edition.json'),'utf8'));
const copy=()=>structuredClone(example);
test('rejects invented dates and changed supplied headlines',()=>{
 const e=copy();e.date='2026-02-30';assert.throws(()=>validate(e),/real/);
 const changed=copy();changed.panels[0].headline='A new headline';assert.throws(()=>validate(changed),/wording/);
 const lines=copy();lines.panels[0].headlineLines=['Wrong headline'];assert.throws(()=>validate(lines),/preserve/);
});
test('requires evidence references but permits a labelled sample or two stories',()=>{
 const e=copy();e.panels[0].sourceIds=['missing'];assert.throws(()=>validate(e),/sourceIds/);
 const sample=copy();sample.sample=true;sample.sources=[];sample.panels.forEach(p=>p.sourceIds=[]);assert.doesNotThrow(()=>validate(sample));
 const two=copy();two.panels[1].storyId=two.panels[0].storyId;two.panels[3].storyId=two.panels[2].storyId;assert.doesNotThrow(()=>validate(two));
});
test('rejects unsupported glyphs and unbreakable copy without silently stripping it',()=>{
 assert.throws(()=>wrap('x'.repeat(200)),/Unbreakable/);
 assert.throws(()=>wrap('A laptop 💻'),/Unsupported/);
});
test('renders an edition atomically, preserves copy and reconstructs every pixel',async()=>{
 const temp=await fs.mkdtemp(path.join(os.tmpdir(),'daily-panorama-'));
 try{
  const output=path.join(temp,'edition');await render(copy(),output);
  const manifest=JSON.parse(await fs.readFile(path.join(output,'edition-record.json')));assert.equal(manifest.status,'generated');assert.deepEqual(manifest.order,['01.png','02.png','03.png','04.png']);
  assert.deepEqual(JSON.parse(await fs.readFile(path.join(output,'edition.json'))),example);
  const panels=[];for(let i=1;i<=4;i++){const file=path.join(output,`0${i}.png`);const m=await sharp(file).metadata();assert.deepEqual([m.width,m.height],[1080,2340]);assert.ok((await fs.stat(file)).size<5_000_000);panels.push({input:file,left:(i-1)*1080,top:0});}
  const stitched=await sharp({create:{width:4320,height:2340,channels:4,background:'#000'}}).composite(panels).raw().toBuffer();assert.ok(stitched.equals(await sharp(path.join(output,'composition.png')).raw().toBuffer()));
  const svg=await fs.readFile(path.join(output,'composition.svg'),'utf8');assert.ok(!svg.includes('<text'));assert.ok(svg.includes('aria-label="Try Omarchy"'));
  await assert.rejects(()=>render(copy(),output),/already exists/);
  const long=copy();long.panels[0].paragraphs=['word '.repeat(200)];await assert.rejects(()=>render(long,path.join(temp,'overflow')),/reading area/);await assert.rejects(()=>fs.stat(path.join(temp,'overflow')),/ENOENT/);
  assert.deepEqual((await fs.readdir(temp)).sort(),['edition']);
 }finally{await fs.rm(temp,{recursive:true,force:true});}
});
