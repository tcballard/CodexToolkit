# Validate a hard length limit

Use the official `twitter-text` parser through the bundled Node helper. Do not approximate X weighted length with byte length, JavaScript `.length`, or a generic Unicode character count. URLs normally count as 23; Unicode and emoji have special rules. Sources: https://github.com/twitter/twitter-text and https://docs.x.com/fundamentals/counting-characters.

Install locked dependencies once when missing: run `npm ci --ignore-scripts` in this skill's `scripts/` directory. Then run `node /absolute/path/to/skill/scripts/count-post.cjs 280 < /path/to/final-post.txt`. Substitute the actual paths. The file must contain only the exact final copy, including links and any numbering; the helper preserves trailing newlines. Use a quoted heredoc or file API to write text safely.

Exit 0 means text passes the parser at the supplied limit; 1 means invalid/over-limit text; 2 means missing dependencies or bad invocation. Revise and recount after changes. A custom limit such as 400 validates that weighted budget only, not account access to long posts or Article requirements. For a word limit, count words separately. For ordinary-language character budgets, clarify the convention only if it materially changes the answer; don't silently claim different measures are identical.

If Node or the parser is unavailable, use an available official composer counter. Otherwise keep a conservative draft and say exact weighted validation was unavailable when compliance matters; never label an estimate verified. No counter result predicts whether the post will expand in the feed.
