# Approved mobile format

| Element | Specification |
| --- | --- |
| Master | 4320 × 2340, one continuous composition |
| Panels | Four 1080 × 2340 PNGs, 9:19.5, left to right |
| Side margins | 90 px inside every panel |
| Masthead | Unchanged crop of Tom’s supplied green artwork, 540 × 202 |
| Type | DejaVu Sans; 80 px bold headlines, 52 px body, 76 px leading |
| Body at 390 px display width | Approximately 19 CSS px before viewer scaling |
| Reading area | Body finishes above y=1940; no automatic shrinking |
| Identity | Near-black #050807, green #a5ff57, light copy #d7dfd3 |

The terminal decoration is editorial artwork, not commands or software output. Keep one master and split it mechanically. Do not independently generate four pictures. The layout is an approved starting point, not a mandate for four separate stories. About 45–65 words per panel usually fits; the renderer’s measured limits decide. Do not replace strong writing with filler to reach a count.

## Edition JSON

The example is the runnable contract:

- `date`: real ISO calendar date, YYYY-MM-DD. Display labels derive from it.
- `sample`: boolean; true adds SAMPLE EDITION to every panel.
- `caption`: complete accompanying X draft. Check the destination’s weighted character limit with available writing tools; the renderer does not validate X’s weighted limit.
- `sources`: array of `{id, title, url, verification, note}`. Use HTTPS primary-source URLs. Verification is `checked` or `requires-verification`; explain what was checked and any remaining gaps in the note.
- `panels`: exactly four entries. Each has `storyId`, `headline`, `status`, `paragraphs`, `sourceIds`. Several panels may share a storyId and sources.
- Optional `sourceHeadline` must match `headline` exactly, providing a mechanical guard against rewriting supplied headlines.
- Optional `headlineLines` must join with spaces to exactly reproduce the headline. Otherwise wrapping is measured automatically. Never insert or delete words to make it fit.
- Optional `emoji` is retained as metadata, not rendered. The approved pilot uses headline words without emoji glyphs. Request a reviewed glyph treatment if visual emoji are essential.

Use status labels that communicate availability, such as RELEASED · VM USES DEV, MERGED INTO DEVELOPMENT, COMMUNITY PLUGIN or PLANNED. A polished panel does not make a development change stable. Sample editions may have no sources; nonsample panels require valid source references. `requires-verification` is allowed so a design draft can remain honest, but resolve material gaps before presenting it as publication-ready.

## Outputs and revisions

The renderer writes `composition.png`, outlined `composition.svg`, `01.png` through `04.png`, panorama/contact-sheet/opened-panel previews, `simulated-feed.png`, `edition.json`, `caption.txt`, `sources.md`, `validation.json` and `edition-record.json`. SVG paths preserve typography; edit the JSON to revise wording. The installed renderer and bundled assets regenerate outputs. Keep the package alongside an edition if handing editable sources to someone without the skill.

Use a new revision directory. Existing outputs are never replaced. Layout/schema errors produce no final output directory; failed exports remove their staging directory. The edition record includes content hashes, dimensions via validation, source IDs and posting order. Retain it with the edition; an external publication log belongs with the publication, not in the installed skill.

## Viewing evidence

The reference post https://x.com/doganuraldesign/status/2110745483547206034 was observed in desktop web on 18 October 2026 as a horizontal media strip in media order. Later panels extended outside the visible post column. Opening media encountered a sign-in prompt. Expanded-image behaviour, native iOS, authenticated timeline layouts and alternate client cropping remain unverified. Do not universalise the desktop observation or assume a 2×2 grid.

`simulated-feed.png` models a horizontal strip and labels itself as simulated. The opened-panel preview is the artwork at phone-like dimensions, not a native X screenshot. On clients that display a grid, the panorama will be interrupted; individual reading panels still work when opened. Critical copy is contained within each panel, but there is no verified universal thumbnail safe area.

## Production checklist

1. Confirm date/window, editorial material and any supplied exact headlines.
2. Check primary sources, availability and caveats; select only worthwhile material.
3. Write caption and concise panel copy; preserve supplied voice and wording.
4. Render a new revision; inspect measured overflow and split checks.
5. Open all four panels at phone size, the master and labelled feed simulation.
6. Check current X client behaviour if claiming a particular viewing experience.
7. Save sources, editable input, master, panels and record; mark approval honestly.
8. Publish only when explicitly instructed; record the actual post URL afterwards.
