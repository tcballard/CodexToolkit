'use strict';
const test = require('node:test');
const assert = require('node:assert/strict');
const {spawnSync} = require('node:child_process');
const path = require('node:path');
function count(input, ...args) {
 const r=spawnSync(process.execPath,[path.join(__dirname,'count-post.cjs'),...args],{input,encoding:'utf8'});
 return {status:r.status,value:r.stdout?JSON.parse(r.stdout):null};
}
test('ordinary boundary and custom limit',()=>{
 assert.equal(count('a'.repeat(280)).status,0);
 assert.equal(count('a'.repeat(281)).status,1);
 assert.equal(count('a'.repeat(400),'400').status,0);
 assert.equal(count('a'.repeat(401),'400').status,1);
});
test('URLs, Unicode, emoji and literal newlines',()=>{
 for(const [text,length] of [['https://example.com/very/long/path',23],['漢字',4],['👨‍👩‍👧‍👦',2],['e\u0301',1],['a\nb',3],['a\n',2]]) assert.equal(count(text).value.weightedLength,length,text);
});
test('invalid text and arguments fail',()=>{
 assert.equal(count('').status,1);
 assert.equal(count('\uFFFE').status,1);
 assert.equal(count('hello','0').status,2);
 assert.equal(count('hello','NaN').status,2);
});
