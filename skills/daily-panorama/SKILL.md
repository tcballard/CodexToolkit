---
name: daily-panorama
description: "Create The Daily Panorama, Today in Omarchy’s mobile-first visual newsletter: one continuous terminal-style composition split into four ordered reading panels. Use for adapting a supplied edition, researching a dated edition, revising panels or exporting posting images and source notes. Preserve supplied headlines and distinguish released work, development changes and plans."
---

# The Daily Panorama

Turn the strongest reporting into four connected mobile reading panels. Today in Omarchy is a scheduled editorial task in a chat, not another skill or a prerequisite installation. Use the supplied edition as the editorial authority; do not change its schedule.

## Establish the edition

Use the requested date and source material. For fresh reporting, define a rolling 24-hour window ending at the agreed publication time in Europe/London, then verify meaningful developments through primary sources. Record event dates separately from retrieval dates. Distinguish shipped releases, merged development changes, community work, measurements on named hardware and future plans. Attribute measurements and retain limitations that affect whether someone should try the feature.

Select an editorial thread, not a compulsory list of four stories. Two strong stories may occupy two panels each through explanation, evidence or a practical takeaway. Never invent a fourth story or pad a quiet day. Retain Tom’s supplied headline wording exactly, including punctuation; layout changes may introduce line breaks. Preserve first-person British English, candid humour and useful qualifications. Condense body copy only with editorial judgment; never drop a material caveat to fit. Do not invent personal experiences or engagement claims.

## Compose and render

Use the approved terminal identity: original green masthead, near-black canvas, restrained green character texture, clean light type and generous space. One 4320 × 2340 master becomes four 1080 × 2340 slices, left to right. Artwork and terminal motifs connect the panels; headlines and important content stay inside each panel. Keep exact copy in JSON and typeset deterministically. Never generate text as part of artwork or present generated UI as a working-feature screenshot. Use real screenshots only with provenance and a reviewed layout revision.

Read [format and input](references/format.md) for the JSON contract, dimensions, production checklist and viewing limits. Copy [the worked example](assets/example/edition.json), replacing its date, copy, source ledger and caption. See [example provenance](references/worked-example.md) before treating its historical reporting as current news.

From the skill directory, install the locked Node dependencies and render to a new output directory:

```bash
npm ci --prefix scripts
node scripts/render.mjs /absolute/path/edition.json /absolute/path/editions/2026-10-17-v1
```

Use Node 22 or newer. The production pipeline is Node only. Bundled fonts become SVG outlines, avoiding dependence on system fonts. The renderer rejects unsupported glyphs, overflowing lines and excessive copy rather than silently rewriting text or shrinking it. Preserve approved wording when resolving a failure. The approved typography omits emoji markers visually; retain them as editorial metadata if supplied, and do not silently strip emoji from a headline to bypass validation.

## Review and deliver

Open the full composition, every individual panel and the phone-size previews. Check wording, paragraphs, spacing, contrast, clipping and seams. Inspect `validation.json`; pixel-perfect reconstruction proves the split, not editorial accuracy or native-client behaviour. Read the caption and source notes alongside the panels. Keep source verification honest; a URL alone does not establish a claim.

Upload order is `01.png`, `02.png`, `03.png`, `04.png`. The 9:19.5 panels target tall phones when opened; X controls, handset dimensions and client layouts may leave margins or crop previews. The feed image is explicitly a simulation. Native iOS viewing has not been verified; inspect actual X before asserting a layout or changing safe areas.

Save the composition, panels, editable JSON/SVG, caption, sources and edition record durably in the user’s chosen destination. Keep generated, approved and published states distinct. An edition record is not proof of publication. Update a publication log only with observed publication evidence. Do not publish an X post without explicit instruction.

Example invocation: “Use daily-panorama to turn this Today in Omarchy edition into the approved terminal panorama. Keep my headlines, reflow for mobile, verify sources, and give me four numbered images, the master, previews and caption.”
