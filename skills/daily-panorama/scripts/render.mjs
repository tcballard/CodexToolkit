import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { createHash } from 'node:crypto';
import sharp from 'sharp';
import opentype from 'opentype.js';

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),'..');
export const geometry={width:4320,height:2340,panelWidth:1080,margin:90,bodySize:52};
const {width:W,height:H,panelWidth:P}=geometry;
const fonts=Object.fromEntries(['regular','bold','mono'].map((key,i)=>[key,opentype.loadSync(path.join(root,'assets/fonts',['DejaVuSans.ttf','DejaVuSans-Bold.ttf','DejaVuSansMono.ttf'][i]))]));
const esc=s=>s.replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;');
const hash=b=>createHash('sha256').update(b).digest('hex');
function string(value,label,max=2000){if(typeof value!=='string'||!value.trim()||value.length>max||/[\u0000-\u0008\u000b-\u001f]/u.test(value))throw Error(`Invalid ${label}`);return value;}
export function validate(e){
 if(!e||typeof e!=='object')throw Error('Expected an edition object');
 if(!/^\d{4}-\d{2}-\d{2}$/.test(e.date)||!Number.isFinite(Date.parse(e.date))||new Date(e.date).toISOString().slice(0,10)!==e.date)throw Error('Use a real YYYY-MM-DD date');
 string(e.caption,'caption');
 if(typeof e.sample!=='boolean')throw Error('Set sample to true or false');
 if(!Array.isArray(e.sources))throw Error('Supply a sources array');
 const ids=new Set();
 for(const s of e.sources){string(s.id,'source id',80);if(ids.has(s.id))throw Error('Duplicate source id');ids.add(s.id);string(s.title,'source title',300);if(new URL(s.url).protocol!=='https:')throw Error('Use HTTPS source URLs');if(!['checked','requires-verification'].includes(s.verification))throw Error('Record source verification');string(s.note,'source note');}
 if(!Array.isArray(e.panels)||e.panels.length!==4)throw Error('Provide four panels; related panels may share a storyId');
 for(const [i,p] of e.panels.entries()){
  string(p.storyId,`panel ${i+1} storyId`,100);string(p.headline,'headline',160);string(p.status,'status',80);
  if(p.sourceHeadline!==undefined&&p.sourceHeadline!==p.headline)throw Error('Supplied headline wording changed');
  if(p.headlineLines&&(!Array.isArray(p.headlineLines)||p.headlineLines.join(' ')!==p.headline))throw Error('Headline lines must preserve the headline exactly');
  if(!Array.isArray(p.paragraphs)||p.paragraphs.length<1||p.paragraphs.length>5)throw Error('Provide 1–5 paragraphs');
  p.paragraphs.forEach(s=>string(s,'paragraph'));
  if(!Array.isArray(p.sourceIds)||p.sourceIds.some(id=>!ids.has(id))||(!e.sample&&p.sourceIds.length===0))throw Error('Each nonsample panel needs valid sourceIds');
 }
 return e;
}
function measure(s,size,font='regular'){return fonts[font].getAdvanceWidth(s,size,{kerning:true});}
function glyphs(s,font){for(const c of s)if(!fonts[font].charToGlyphIndex(c))throw Error(`Unsupported character ${JSON.stringify(c)}; use the approved text-only headline treatment, or supply a reviewed glyph asset`);}
export function wrap(s,size=52,font='regular',limit=900){
 glyphs(s,font);const lines=[];let line='';
 for(const word of s.split(/\s+/u)){if(measure(word,size,font)>limit)throw Error('Unbreakable text exceeds panel width');const candidate=line?line+' '+word:word;if(measure(candidate,size,font)>limit&&line){lines.push(line);line=word;}else line=candidate;}
 if(line)lines.push(line);return lines;
}
function text(s,x,y,size=52,fill='#d7dfd3',font='regular'){
 glyphs(s,font);return `<g aria-label="${esc(s).replaceAll('"','&quot;')}" fill="${fill}">${fonts[font].getPath(s,x,y,size,{kerning:true}).toSVG(2)}</g>`;
}
function background(){
 let b=`<defs><linearGradient id="floor" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#050807"/><stop offset="1" stop-color="#0d1b11"/></linearGradient><pattern id="scan" width="8" height="8" patternUnits="userSpaceOnUse"><path d="M0 7.5H8" stroke="#9bff6b" stroke-opacity=".02"/></pattern></defs><rect width="${W}" height="${H}" fill="#050807"/><rect y="1940" width="${W}" height="400" fill="url(#floor)"/><rect width="${W}" height="${H}" fill="url(#scan)"/><path d="M0 55H${W} M0 2200H${W}" stroke="#a5ff57" stroke-opacity=".22" stroke-width="2"/>`;
 for(let row=0;row<6;row++)for(let col=0;col<145;col++){const wave=Math.sin(col*.052+row*.41)*.5+.5;if((col*73+row*137)%101<47+wave*30)b+=`<g opacity="${(.035+wave*.08).toFixed(3)}">${text(['.',':','/','|','+','_'][(col*7+row*11)%6],col*30,1970+row*36,23,'#a5ff57','mono')}</g>`;}
 return b+`<path d="M90 2040L145 2085L90 2130" fill="none" stroke="#a5ff57" stroke-width="11"/><rect x="175" y="2119" width="65" height="11" fill="#a5ff57"/><path d="M285 2125H4080" stroke="#a5ff57" stroke-opacity=".12" stroke-width="2"/><rect x="4120" y="2030" width="64" height="104" fill="#a5ff57" fill-opacity=".72"/>`;
}
function layout(e,logo){
 const date=`${e.date.slice(8)}-${['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][Number(e.date.slice(5,7))-1]}-${e.date.slice(0,4)}`;
 let svg=`<svg xmlns="http://www.w3.org/2000/svg" width="${W}" height="${H}" role="img"><title>${esc(`Today in Omarchy (${date})`)}</title>${background()}`;const report=[];
 for(const [i,p] of e.panels.entries()){
  const x=i*P+90;svg+=`<image href="data:image/png;base64,${logo}" x="${x}" y="125" width="540" height="202" style="mix-blend-mode:screen"/>`;
  svg+=text('THE DAILY PANORAMA',x,400,30,'#a5ff57','mono')+text(date,x,455,32,'#92a390','mono')+text(`0${i+1}/04`,x+785,164,29,'#92a390','mono');
  svg+=`<path d="M${x} 515h100" stroke="#a5ff57" stroke-width="5"/>`;
  const heads=p.headlineLines??wrap(p.headline,80,'bold');if(heads.length>3)throw Error(`Panel ${i+1}: headline needs more than three lines`);
  let y=630;for(const line of heads){if(measure(line,80,'bold')>900)throw Error('Headline overflow');svg+=text(line,x,y,80,'#f0f4eb','bold');y+=103;}
  const statusY=Math.max(820,y+35);if(measure(p.status,30)>900)throw Error('Status overflow');svg+=text(p.status,x,statusY,30,'#a5ff57');
  y=statusY+100;const lines=[];
  for(const [j,para] of p.paragraphs.entries()){for(const line of wrap(para)){svg+=text(line,x,y);lines.push({text:line,width:measure(line,52),baseline:y});y+=76;}if(j<p.paragraphs.length-1)y+=35;}
  if(y>1940)throw Error(`Panel ${i+1}: copy exceeds the reading area; edit copy explicitly, never shrink type`);
  svg+=text('TODAY IN OMARCHY',x,2260,24,'#c5d2bd','mono')+text(`0${i+1} / 04`,x+760,2260,24,'#92a390','mono');
  if(e.sample)svg+=text('SAMPLE EDITION',x+480,455,28,'#a5ff57','mono');
  report.push({panel:i+1,headlineLines:heads,bodyLines:lines,endY:y});
 }
 return {svg:svg+'</svg>',report};
}
export async function render(e,destination){
 validate(e);const dest=path.resolve(destination);if(await fs.lstat(dest).then(()=>true,err=>{if(err.code==='ENOENT')return false;throw err;}))throw Error('Output already exists; use a new edition or revision directory');
 const logo=(await fs.readFile(path.join(root,'assets/masthead.png'))).toString('base64');
 const {svg,report}=layout(e,logo);
 await fs.mkdir(path.dirname(dest),{recursive:true});const staging=await fs.mkdtemp(path.join(path.dirname(dest),'.panorama-'));
 try{
  const master=await sharp(Buffer.from(svg)).png().toBuffer();
  await fs.writeFile(path.join(staging,'composition.svg'),svg);await fs.writeFile(path.join(staging,'composition.png'),master);
  const panels=[];for(let i=0;i<4;i++){const b=await sharp(master).extract({left:i*P,top:0,width:P,height:H}).png().toBuffer();panels.push(b);await fs.writeFile(path.join(staging,`0${i+1}.png`),b);}
  const reconstructed=await sharp({create:{width:W,height:H,channels:4,background:'#000'}}).composite(panels.map((input,i)=>({input,left:i*P,top:0}))).raw().toBuffer();
  if(!reconstructed.equals(await sharp(master).raw().toBuffer()))throw Error('Reconstruction differs from master');
  await sharp(master).resize(1440).png().toFile(path.join(staging,'panorama-preview.png'));
  await sharp(panels[0]).resize(390,845).png().toFile(path.join(staging,'opened-panel-preview.png'));
  const pieces=[];for(let i=0;i<4;i++)pieces.push({input:await sharp(panels[i]).resize(360,780).toBuffer(),left:24+i*384,top:70});
  const label=Buffer.from(`<svg width="1560" height="890">${text('PHONE-SHAPED PANELS / DESIGN PREVIEW',24,39,21,'#a5ff57','mono')}</svg>`);
  await sharp({create:{width:1560,height:890,channels:4,background:'#121712'}}).composite([...pieces,{input:label,left:0,top:0}]).png().toFile(path.join(staging,'panel-previews.png'));
  const feed=Buffer.from(`<svg width="430" height="1040"><rect width="430" height="1040" fill="#000"/>${text('SIMULATED FEED / NOT NATIVE X',20,29,15,'#a5ff57','mono')}${text('Tom Ballard',20,78,21,'#f0f4eb','bold')}${text(`Today in Omarchy (${e.date})`,20,112,17)}${text('Four connected panels. Swipe to read.',20,143,16)}</svg>`);
  const first=await sharp(panels[0]).resize(340).toBuffer();const next=await sharp(panels[1]).resize(340).extract({left:0,top:0,width:54,height:737}).toBuffer();
  await sharp(feed).composite([{input:first,left:20,top:178},{input:next,left:366,top:178}]).png().toFile(path.join(staging,'simulated-feed.png'));
  const json=JSON.stringify(e,null,2)+'\n';await fs.writeFile(path.join(staging,'edition.json'),json);
  await fs.writeFile(path.join(staging,'caption.txt'),e.caption+'\n');
  await fs.writeFile(path.join(staging,'sources.md'),`# Sources for ${e.date}\n\nSource presence is not evidence of verification.\n\n`+e.sources.map(s=>`${s.id}: ${s.title}\n${s.url}\nVerification: ${s.verification}\n${s.note}\n`).join('\n'));
  await fs.writeFile(path.join(staging,'validation.json'),JSON.stringify({geometry,panelRatio:'9:19.5',reconstruction:'pixel-identical',fonts:'bundled DejaVu; SVG glyph outlines',layout:report,viewer:'native X unverified; feed is a simulation',sample:e.sample},null,2)+'\n');
  await fs.writeFile(path.join(staging,'edition-record.json'),JSON.stringify({date:e.date,status:'generated',sample:e.sample,inputSHA256:hash(json),compositionSHA256:hash(master),panels:panels.map((b,i)=>({file:`0${i+1}.png`,sha256:hash(b),bytes:b.length})),sourceIds:e.sources.map(s=>s.id),order:['01.png','02.png','03.png','04.png']},null,2)+'\n');
  await fs.rename(staging,dest);return {directory:dest,panels:4,reconstruction:'pixel-identical'};
 }catch(error){await fs.rm(staging,{recursive:true,force:true});throw error;}
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 try{if(process.argv.length!==4)throw Error('Usage: node render.mjs EDITION.json NEW_OUTPUT_DIRECTORY');const e=JSON.parse(await fs.readFile(process.argv[2],'utf8'));console.log(JSON.stringify(await render(e,process.argv[3])));}catch(error){console.error(error.message);process.exitCode=1;}
}
