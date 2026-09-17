#!/usr/bin/env node
'use strict';
const fs = require('node:fs');
let parseTweet, configs;
try { ({ parseTweet, configs } = require('twitter-text')); }
catch { console.error('Missing parser. Run npm ci --ignore-scripts in this script directory.'); process.exit(2); }
const args = process.argv.slice(2);
if (args.length > 1 || (args.length && !/^[1-9]\d*$/.test(args[0]))) {
 console.error('Usage: node count-post.cjs [weighted-character-limit] < post.txt'); process.exit(2);
}
const limit = args.length ? Number(args[0]) : 280;
if (!Number.isSafeInteger(limit)) { console.error('Limit must be a positive safe integer.'); process.exit(2); }
const text = fs.readFileSync(0, 'utf8');
const result = parseTweet(text, { ...configs.defaults, maxWeightedTweetLength: limit });
console.log(JSON.stringify({weightedLength:result.weightedLength,limit,withinLimit:result.weightedLength<=limit,validText:result.valid,parser:'twitter-text@3.1.0',scope:'Text length and parser validity only; not account or long-post eligibility'},null,2));
process.exitCode = result.valid ? 0 : 1;
