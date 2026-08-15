---
name: write-x-bangers
description: Write, rewrite, critique, or plan high-performing posts and threads for X using the published X recommendation-system mechanics, strong editorial judgement, and an evidence-led builder voice. Use for X/Twitter posts, launch announcements, release posts, quote posts, threads, hooks, replies, post critiques, social copy, or requests to make a post a “banger,” more engaging, more shareable, or more likely to travel beyond existing followers.
---

# Write X Bangers

Create posts people genuinely want to read, reply to, share, quote, or follow the author for. Use algorithm knowledge as a quality constraint, never as a promise or a substitute for a worthwhile idea.

Read [references/x-ranking.md](references/x-ranking.md) before explaining or applying ranking mechanics. Read [references/default-voice.md](references/default-voice.md) when the user has not supplied a different voice.

## Establish the job

Infer these inputs from the request and linked material:

- audience: the specific people who should care
- outcome: announce, teach, challenge, recruit, sell, or start a serious discussion
- payload: one claim, result, lesson, or artifact worth passing on
- proof: metric, shipped feature, demo, source, example, screenshot, or concrete experience
- action: the one natural next step, if any

If a missing fact would make the central claim unsafe or materially different, ask one concise question. Otherwise make a reasonable assumption and draft immediately. Never invent proof, numbers, users, quotations, availability, or launch status.

For a post about a linked page, release, repository, or product, inspect it before drafting. Distinguish shipped facts from plans. If the user asks for a current algorithm explanation, recheck the X source rather than relying only on the dated snapshot.

## Choose the post shape

Use the smallest format that carries the idea:

- **Single post:** default; keep it within X's 280-character weighted limit for portability unless the user asks for a long post. Treat each URL as 23 characters and verify the final count.
- **Launch post:** lead with the user-visible change or result, then the product name and proof.
- **Lesson post:** claim, concrete observation, implication.
- **Contrarian post:** name the precise disagreement and earn it with evidence; do not manufacture conflict.
- **Question post:** provide a useful premise before asking; avoid empty engagement bait.
- **Thread:** use only when the reasoning, evidence, or sequence cannot fit honestly in one post. Give every post a distinct job and make the first post useful without opening the thread.
- **Quote post:** add a new claim, context, evidence, or consequence; never merely restate the quoted post.
- **Reply:** answer the person directly and add one useful fact or perspective. Optimise for conversation, not parasitic visibility.

## Draft the post

1. Write several candidate opening lines silently. Select the one with the most specific tension, result, novelty, or utility.
2. Make the first line intelligible outside the author's follower graph. Name the subject early; avoid vague pronouns and throat-clearing.
3. Spend the body on one idea. Prefer concrete nouns, active verbs, exact scope, and causal explanation.
4. Add proof as close as possible to the claim it supports.
5. Create an honest interaction surface:
   - a useful artifact people may share or copy
   - a decision or trade-off knowledgeable people can discuss
   - a surprising result people may quote with their interpretation
   - a clear reason to visit the profile or follow for the next instalment
6. End cleanly. Add at most one content-native call to action. Do not append “Thoughts?” when the post does not need it.
7. Remove generic setup, duplicated claims, inflated adjectives, needless hashtags, and any sentence that sounds generated.

When rewriting “without changing facts,” preserve factual claims and their certainty—not emojis, hype, hashtags, generic calls to action, or promotional framing. Remove weak furniture unless the user explicitly asks to retain it.

Clear topic semantics help the system match a post to interested viewers. Do not keyword-stuff. Natural specificity is stronger than a bag of trend terms.

## Protect quality and reach

- Optimise for intended-viewer relevance before raw engagement.
- Prefer a self-contained top-level post for discovery. Do not hide the central idea behind a link or an unexplained reply.
- Give readers a legitimate reason to reply, share privately, copy the link, quote, or follow.
- Avoid rage bait, deceptive curiosity gaps, forced polarisation, and repetitive posting bursts. Negative-action predictions explicitly reduce ranking, and repeated posts from one author are diversity-discounted.
- Use zero hashtags by default; use at most one when it is a genuine discovery convention.
- Use emojis only if they belong to the author's established voice.
- Never state that a particular tactic “beats the algorithm” or guarantees reach.
- Do not convert published scoring weights into engagement-count equivalences.

## Editorial gate

Score the draft silently from 0–2 on each dimension and revise until no dimension is zero and the total is at least 10/12:

1. audience fit
2. opening strength
3. specificity and proof
4. useful reply/share surface
5. voice authenticity
6. low regret risk: no hype, ambiguity, or likely negative response caused by poor framing

Do not show the rubric unless the user asks for critique or scoring.

## Return the result

Lead with the finished copy, not process commentary. Present it in a writing block when supported.

Default output:

1. one recommended post
2. two alternative opening lines, only when they offer meaningfully different angles

For a simple rewrite, return only the improved post unless alternatives would materially help. For a critique, give the decisive weakness, the fix, and a rewritten version. For a thread, number posts and verify that each is within the requested length.

Do not clutter the answer with algorithm theory. Briefly explain the editorial choice only when requested or when the framing depends on a non-obvious trade-off.
