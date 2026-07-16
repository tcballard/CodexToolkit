# Workshop Skills Build Scope

- Repository: `tcballard/CodexToolkit`
- Product: `tcballard-toolkit`
- Status: Draft for owner review; implementation not started
- Scoped on: 2026-07-16
- Intended environments: ChatGPT and Codex
- Delivery: dedicated branches and draft pull requests; never direct to the default branch

## 1. Executive summary

This scope defines four independently discoverable workshop Skills:

1. `technical-product-name-check`
2. `visual-asset-adapter`
3. `macos-app-icon-preflight`
4. `project-skill-scaffold`

All four belong in CodexToolkit because they convert recurring, error-prone work into narrow evidence contracts. They do not form one runtime system and should not be implemented in one large release. The recommended delivery is four incremental toolkit releases, each with its own branch, validation, human review, and draft PR.

The main scope decisions are:

- Keep all four candidates as separate Skills. Their invocation intent, required evidence, output, and failure modes differ materially.
- Build `technical-product-name-check` first because it has a clear contract and no dependency on the visual or project-orchestration Skills.
- Build `visual-asset-adapter` before `macos-app-icon-preflight`; the former supplies a general fidelity and image-evidence contract, while the latter adds current Apple-specific judgment.
- Implement `macos-app-icon-preflight` v0.0.1 as inspection, limited deterministic preparation, preview-grid verification, and implementation handoff. Do not attempt semantic removal of baked shells or unrestricted icon redesign.
- Defer `project-skill-scaffold` implementation until the first three are settled and its generated contract is piloted against at least Premonition plus one structurally different project. It has the highest strategic value and the greatest risk of encoding stale project state.
- Do not add `README.md` files inside Skill directories. The installed Skill authoring standard explicitly treats them as auxiliary clutter. `SKILL.md` is the self-contained overview; essential detail belongs in `references/`, deterministic utilities in `scripts/`, and reusable output material in `assets/`.
- Do not create toolkit-level shared runtime utilities in the first release. Soft orchestration and a documented evidence vocabulary are sufficient. Each Skill must remain usable when extracted; small mechanical utilities may be vendored with provenance if a Skill later graduates.
- Treat repository delivery as a handoff boundary. These Skills inspect, produce, and verify their own artefacts, but conform to a future `repo-delivery-guard` or the existing publishing workflow rather than duplicating branch/commit/PR mechanics.

### Release recommendation

| Order | Candidate | Recommendation | Proposed toolkit release | Main reason |
| --- | --- | --- | --- | --- |
| 1 | `technical-product-name-check` | Build now | v0.0.8 | Clear evidence contract; independent of the other three |
| 2 | `visual-asset-adapter` | Build now | v0.0.9 | Highest immediate recurring value; foundation for visual fidelity checks |
| 3 | `macos-app-icon-preflight` | Build now with reduced editing scope | v0.0.10 | Distinct platform job; current Apple workflow must remain live-sourced |
| 4 | `project-skill-scaffold` | Defer implementation until two-project pilot | v0.0.11 at earliest | Highest stale-state and generated-content risk |

The scope artefact itself does not change the plugin version because it adds no installed capability.

## 2. Repository findings and governing conventions

The scoped repository currently contains ten focused Skills at the v0.0.7 planning head: Product Demo, Launch Pack, GitHub Social Preview, README Front Door, Open-Source PR Preflight, Authored Frontend Design, Authored macOS Design, Merge & Tell, Build Premonition, and Maintain Premonition Logs.

No repository-local `AGENTS.md`, `CONTRIBUTING*`, PR template, or existing `docs/` convention was found at scope time. The root README and `.codex-plugin/plugin.json` therefore provide the current local product contract: focused Skills may mature in the toolkit and later graduate, detailed knowledge should be progressively disclosed, and fragile checks should be deterministic.

The installed capability review establishes these boundaries:

- Skill Creator owns Skill anatomy, concise trigger metadata, progressive disclosure, validation, and the rule against auxiliary Skill READMEs.
- Plugin Creator owns plugin manifests, plugin validation, and installation/update mechanics.
- Build macOS Apps owns SwiftUI/AppKit implementation, Xcode and SwiftPM build/run work, asset-catalogue integration, signing, packaging, and notarisation.
- Product Design owns design exploration, visual alternatives, visual targets, product-flow audits, and prototype workflows.
- Image generation owns new raster creation and semantic image editing. It explicitly prefers repository-native vector editing when matching an existing logo or icon system.
- GitHub tooling owns repository inspection and authorized publication actions.
- Existing CodexToolkit Skills own their named outcomes: GitHub social composition, README front-door editing, authored interface design, project-specific Premonition orchestration, logs, demos, launch coordination, public copy, and OSS PR readiness.

### Shared evidence vocabulary

Every candidate must label material statements using the following states when ambiguity exists:

- **Confirmed:** directly observed in a primary source, file, command result, or current public source.
- **Inferred:** a reasoned conclusion from identified evidence; not presented as a source fact.
- **Unverified:** plausible but not checked or not checkable in the current environment.
- **Preference:** supplied by the user or repository owner.
- **Proposed:** future work, suggested wording, candidate structure, or unaccepted change.

Every completion report must name the evidence, date current external checks, distinguish automated from manual verification, and state what was not checked.

## 3. Skill scope: `technical-product-name-check`

### One-sentence job

Run a dated, source-linked practical collision and namespace preflight for a technical product name without claiming legal or trademark clearance.

### User problem

A developer-tool name may appear free in one namespace while colliding with an established product, package, command, repository, app, or search term elsewhere. Ad hoc checks are inconsistent, quickly stale, and often confuse “not found” with “reserved” or “legally clear.”

### Invocation triggers

Invoke when the user asks to:

- check, validate, compare, shortlist, or de-risk a name for a developer tool, library, CLI, app, plugin, package, or open-source project;
- check availability or collisions across repositories, registries, commands, stores, domains, or search;
- re-run a prior naming report;
- decide whether to proceed, modify, reserve, or reject a technical product name.

Do not invoke for broad brand strategy, unrestricted name ideation, legal advice, trademark filing, purchasing domains, creating repositories, publishing packages, or reserving namespaces.

### Inputs

Mandatory:

- one candidate name or a shortlist;
- a one-line product description;
- product category and intended audience;
- planned distribution channels or enough context to select them.

Optional:

- preferred repository owner or organisation;
- desired repository slug, package slug, command, bundle/display name, domain, and social handle;
- geographic or language constraints;
- preference for distinctiveness, descriptiveness, humour, or neutrality;
- future expansion plans;
- a prior report to compare.

Discoverable from a repository:

- canonical product name and terminology;
- package manifests and executable names;
- bundle identifiers and platform targets;
- existing repository slug and organisation;
- installation channels and release plans;
- existing naming decisions or warnings in documentation and history.

If the product context or intended namespaces remain unknown, produce a coverage proposal and pause before declaring risk.

### Outputs

Default output is an inline naming report. Persist `docs/naming/<candidate>-name-check.md` only when the user requests a durable report or the repository workflow requires it.

The report contains:

- candidate and product context;
- checked-at timestamp and locale/language scope;
- normalized variants;
- sources and exact queries or endpoints;
- exact, near, category, inactive, unrelated, command, and search collisions;
- registry matrix with `Found`, `Not found`, `Blocked`, `Not checked`, or `Ambiguous` states;
- qualitative usability review;
- namespace plan;
- practical risk rating;
- recommendation and targeted variants where useful;
- changes since a prior report;
- explicit “not checked” section;
- legal disclaimer.

### Workflow

1. Inspect the repository or supplied product brief before judging the name.
2. Establish mandatory namespaces from actual distribution plans.
3. Normalize spacing, punctuation, hyphenation, casing, singular/plural, likely slug, command, package, and common misspellings without inventing a rebrand.
4. Run the universal checks:
   - general web search for exact and quoted variants;
   - GitHub repository, organisation, user, and relevant code/package references;
   - major product/company and same-category collisions;
   - search-result ambiguity and dominant unrelated meanings.
5. Run category-specific checks only where relevant:
   - macOS app: Homebrew cask/formula, App Store search, repository, bundle/display-name collisions, planned domain;
   - Python package: PyPI and intended CLI command;
   - Rust crate: crates.io and intended binary command;
   - JavaScript package: npm, scopes, and intended CLI command;
   - Swift package: GitHub and Swift Package Index;
   - ChatGPT/Codex plugin: GitHub, plugin name/skill-name collisions visible in intended distribution, package/repository slug if applicable;
   - Ruby or JVM tooling: RubyGems or Maven Central when planned.
6. Open material results rather than relying on search snippets. Record whether a use is active, abandoned, same-category, or unrelated without treating inactivity as permission.
7. Evaluate pronounceability, spelling, memorability, descriptive fit, distinctiveness, searchability, package/command ergonomics, cultural/technical meanings, and expansion flexibility.
8. Apply the risk model and draft a recommendation.
9. Verify the report includes dates, sources, coverage, limitations, and no legal-clearance claim.
10. If re-running, compare like-for-like checks and highlight changed results rather than silently replacing the earlier conclusion.

### Registry strategy and current-source rules

Universal checks are always required. Registry checks are selected by distribution intent; no fixed “check everything” list is valid.

Use current primary endpoints or official search surfaces where available. At scope time, useful authorities include GitHub’s repository search endpoint and documented search-specific rate limits, npm’s package naming guidance, PyPI’s JSON API, Homebrew’s formula/cask JSON API, RubyGems.org’s API, Maven Central’s search API, and the Swift Package Index search surface. GitHub currently documents 30 authenticated or 10 unauthenticated search requests per minute, so the implementation must serialize and cache within a single report, respect response headers, and record incomplete/blocked results rather than retry aggressively.

The Skill must browse on every availability run. A prior report is historical evidence, never a live availability source.

### Risk model

Use categories, not a synthetic score:

- **LOW:** no material collision in required channels; search and spelling are practical.
- **LOW–MODERATE:** minor unrelated or inactive uses; clear namespace plan exists.
- **MODERATE:** meaningful ambiguity, near collision, command friction, or unavailable preferred slug that needs a conscious workaround.
- **HIGH:** strong same-category product, dominant search collision, serious command/package confusion, or expansion constraint.
- **BLOCKING:** exact collision in a required namespace with no accepted alternative, deceptive similarity to an established same-category product, or insufficient current evidence to support adoption where the user requires certainty.

This is practical product risk. It is not a legal finding.

### Verification

- Every checked source has a current date, direct link, exact variant/query, and observed state.
- Required namespaces are all checked or explicitly blocked.
- Exact and near collisions are separated.
- “Not found” is never rewritten as “available,” “reserved,” or “clear.”
- CLI/package/repository names are checked independently when they differ.
- The final rating maps to listed evidence and the “not checked” section is non-empty when coverage is incomplete.
- A re-run reports deltas from the prior dated report.

### Guardrails

- Never claim trademark or legal clearance.
- Never reserve, buy, register, publish, or create anything without explicit authority.
- Never expose private user or organisation data in public queries.
- Never fabricate a registry result or hide an inconvenient cross-category collision.
- Treat app-store, registrar, marketplace, and search results as time-bound and potentially incomplete.
- Do not recommend speculative alternatives unless they solve an identified problem.

### Non-goals

- Brand positioning or visual identity.
- Open-ended naming workshops.
- Legal opinion, trademark classes, or counsel replacement.
- Domain appraisal or purchasing.
- Repository/package/plugin creation.
- Automated namespace reservation.

### Dependencies and boundaries

- May consume a repository product brief or concise user description; neither is a hard dependency.
- Uses web search and official registry surfaces for current evidence.
- Uses GitHub tooling for GitHub-specific search when available.
- Does not duplicate Merge & Tell, README Front Door, Launch Pack, or general product ideation.

### Suggested Skill structure

```text
skills/technical-product-name-check/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── channel-matrix.md
│   ├── risk-rubric.md
│   └── quality-gates.md
├── assets/templates/
│   └── naming-report.md
└── scripts/
    ├── normalize_name.py
    └── validate_naming_report.py
```

Do not add a scripted registry crawler in v0.0.1. Registry authentication, rate limits, HTML changes, and result interpretation make a broad crawler a maintenance liability before real usage data exists.

### v0.0.1 acceptance criteria

1. Check one developer-tool name across the universal set plus its relevant current namespaces.
2. Compare three candidates using identical coverage and recommend one without false numerical precision.
3. Detect a name that is free on GitHub but strongly occupied elsewhere.
4. Detect a CLI collision even when the repository slug appears unused.
5. Record date, direct sources, queries/variants, result state, and what was not checked.
6. Separate practical collision risk from legal clearance.
7. Re-run a prior report and show changes.
8. Select different registry coverage for a macOS app, Python package, Rust crate, and ChatGPT/Codex plugin.
9. Fail report validation when dates, sources, coverage, recommendation, disclaimer, or “not checked” data is missing.

### Deferred capabilities

- Registry adapter library with backoff and caching.
- Domain RDAP or registrar-specific integrations.
- Trademark database triage.
- Language/cultural review beyond specified locales.
- Automated namespace reservation.
- Historical name-monitoring service.

## 4. Skill scope: `visual-asset-adapter`

### One-sentence job

Faithfully reformat an approved visual source for a specified destination while preserving immutable brand content and proving the output’s technical and visual fidelity.

### User problem

Simple-looking adaptations repeatedly become accidental redesigns: real logos are replaced, wordmarks are approximated, assets are stretched or blurred, crop-safe regions are ignored, transparency is asserted without checking alpha, and file-size claims are made without measuring bytes.

### Invocation triggers

Invoke when the user asks to:

- resize, pad, crop, extend, compress, or reformat an existing approved asset;
- make a transparent README banner from a real wordmark;
- adapt approved artwork for an X banner, documentation header, release card, or platform crop;
- produce platform-ready variants without changing the identity;
- review an existing adaptation for fidelity, transparency, crop, sharpness, dimensions, or file size.

Do not invoke when no source asset exists, when the user wants a new identity or visual concept, or when the main job is GitHub-specific social-preview storytelling or macOS icon suitability.

### Modes

Use two top-level modes rather than a large mode catalogue:

- **Adapt:** inspect, plan, transform, export, verify.
- **Review:** compare an existing output with its source and destination contract.

Target types such as `transparent-banner`, `social-canvas`, `profile-banner`, `release-card`, and `custom` are parameter profiles inside Adapt, not separate invocation modes.

### Inputs

Mandatory:

- one real, readable source asset;
- source-of-truth priority when multiple assets conflict;
- target platform or exact dimensions;
- output format;
- whether transparency is required;
- permitted transformation class.

Conditionally mandatory:

- exact approved copy if new text placement is authorized;
- file-size ceiling;
- safe-area/crop model;
- required background or transparency behavior;
- repository destination;
- explicit authorization for composition changes, README edits, or replacement.

Discoverable:

- repository logos, wordmarks, icons, palettes, type assets, and approved artwork;
- existing brand documentation and source formats;
- platform constraints already recorded in the repository;
- the current consuming file and relative path.

If the referenced source is missing, opaque to the current environment, corrupt, or too small for a credible output, stop and report the exact blocker. A written description is not an approved adaptation source.

### Outputs

Default outputs are the adapted asset plus an inline evidence report. For repository-bound work, save to the exact requested path or a non-destructive sibling filename. Never overwrite the source by default.

The evidence report includes:

- source and output paths plus SHA-256 hashes;
- source and output dimensions, format, color mode, alpha state, and byte size;
- source visual bounds and target safe area;
- immutable elements and permitted transforms;
- exact transformation parameters;
- compression method;
- full-size and destination/crop preview observations;
- automated checks, manual checks, and unresolved limitations.

Persist a sidecar JSON manifest only when reproducibility, multiple variants, or later audit justifies it.

### Workflow

1. Read repository instructions and inspect working-tree state when the task is repository-bound.
2. Locate and open the real source. Establish source priority rather than blending conflicting brand files.
3. Inspect dimensions, aspect ratio, file signature, color mode/profile, alpha channel, alpha bounds, visual bounds, embedded text, sharpness limits, and corruption.
4. Identify immutable content: logo geometry, wordmark typography, product name, brand colors, signature motif, and approved copy.
5. Establish the target contract: canvas, format, bytes, transparency, safe area, crop behavior, background, destination, and allowed changes.
6. Choose the least invasive transform:
   - resize proportionally;
   - add transparent or approved-color padding;
   - crop only expendable surrounding area;
   - extend background without modifying the core asset;
   - place exact approved copy deterministically with a real font only when authorized;
   - compress after composition.
7. Write a short composition plan before any transform that changes placement or adds space.
8. Produce a new output without touching the source.
9. Verify file signature, dimensions, bytes, alpha semantics, core aspect ratio, core sharpness, visual bounds, safe-area containment, crop previews, and approved text.
10. Inspect full size and at least one representative destination preview. For multi-crop platforms, inspect each named crop.
11. Revise failures rather than accepting the first output.
12. Modify README/code references only when explicitly in scope, then validate relative paths.

### Permitted transformation classes

- **Mechanical:** proportional resize, format conversion, padding, lossless optimization, metadata cleanup.
- **Compositional:** repositioning, background extension, safe-area adaptation, deterministic approved text placement.
- **Semantic edit:** reconstruction, inpainting, subject alteration, or generated extension that can change visual meaning.

Mechanical and approved compositional work belong in v0.0.1. Semantic edits route to image editing and require explicit user authorization plus a fidelity review; they are not silently performed by this Skill.

### Verification

- Source and output both open successfully.
- Dimensions, format, and actual bytes exactly meet the target contract.
- Alpha-channel presence and corner/region transparency are measured when transparency is required.
- The immutable core retains its aspect ratio and is not replaced by a generated approximation.
- Crop-safe previews keep all protected content visible.
- Full-size and reduced/destination previews are visually inspected.
- Text strings match approved copy exactly.
- The original source hash is unchanged.
- Repository paths resolve when references are edited.

The validator must distinguish “has an alpha channel” from “contains transparent pixels.” Both are required evidence fields.

### Guardrails

- Never invent or approximate a missing logo, icon, or wordmark.
- Never stretch non-proportionally.
- Never alter embedded typography, slogans, or brand colors without permission.
- Never convert adaptation into redesign.
- Never claim transparency, size, dimensions, crop safety, or fidelity without checks.
- Never overwrite the source by default.
- Never commit, push, or change consuming documentation unless explicitly requested.
- Never use image generation for final logos, wordmarks, or exact typography.

### Non-goals

- Brand exploration or redesign.
- New logo/icon generation.
- GitHub repository narrative and copy composition.
- macOS icon platform judgment.
- Generic image-generation prompting.
- Automatic publication or repository delivery.

### Dependencies and boundaries

- `github-social-preview` owns repository-aware 1280 × 640 composition, exact product copy, and GitHub thumbnail review. Visual Asset Adapter may mechanically prepare an already approved source or finished card, but does not replace that Skill.
- `macos-app-icon-preflight` owns Apple-specific icon readiness and handoff.
- Product Design and image generation own exploration, redesign, and semantic image creation/editing.
- README Front Door owns whether and how an approved banner belongs in the README.

### Suggested Skill structure

```text
skills/visual-asset-adapter/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── transformation-contract.md
│   ├── target-profiles.md
│   └── quality-gates.md
└── scripts/
    ├── inspect_image.py
    ├── adapt_image.py
    └── verify_image.py
```

Use Python for a cross-platform orchestration surface. The implementation spike must establish which formats can be inspected with the standard library and which transforms require Pillow. At scope time this environment has Pillow 12.2.0 and ImageMagick `identify`, but not the `magick` wrapper or macOS `sips`; the Skill must capability-check and fail clearly instead of assuming one backend everywhere.

Do not create shared toolkit image scripts in v0.0.1. Keep the adapter self-contained; let icon preflight use it softly when installed and retain a narrow fallback probe.

### v0.0.1 acceptance criteria

1. Turn an existing transparent wordmark into a correctly padded README banner without redrawing or changing its aspect ratio.
2. Adapt approved square artwork into an X/profile-style banner and prove protected content survives each specified crop.
3. Produce a 1280 × 640 asset below a supplied byte limit when the input is already approved complete artwork; route repository-aware composition to GitHub Social Preview.
4. Refuse when the referenced source is absent or unreadable.
5. Preserve required transparency and distinguish alpha-channel presence from actual transparent pixels.
6. Report exact dimensions, format, actual bytes, hashes, transform parameters, and visual checks.
7. Review a user-provided adaptation and identify distortion, approximation, blur, crop, alpha, or size failures.
8. Leave the source file byte-for-byte unchanged.
9. Fail rather than silently degrade when no supported image backend can perform the requested transform.

### Deferred capabilities

- Semantic generative extension or inpainting.
- Automated perceptual similarity as a sole fidelity verdict.
- Broad vector editing beyond deterministic placement/scale.
- Color-profile conversion beyond inspect-and-preserve.
- Animated image/video adaptation.
- Large profile catalogue requiring continuous platform maintenance.

## 5. Skill scope: `macos-app-icon-preflight`

### One-sentence job

Inspect and, where safely authorized, prepare supplied artwork for modern macOS app-icon use, then hand off verified design evidence without claiming packaging or App Store readiness.

### User problem

Marketing tiles and generated artwork are often mistaken for icon-ready sources. Common defects include baked rounded-square masks, external shells and shadows, insufficient or excessive padding, edge collisions, tiny detail, weak small-size contrast, blurry source scaling, and confusion between icon design, Xcode integration, signing, and release compliance.

### Invocation triggers

Invoke when the user asks to:

- inspect or review actual artwork for macOS app-icon suitability;
- remove or diagnose a baked shell, external frame, glow, or shadow;
- assess safe padding, visual bounds, contrast, or small-size legibility;
- prepare a clean source from approved editable artwork;
- create a preview grid;
- produce an implementation handoff for an existing macOS project.

Do not invoke for open-ended icon ideation, logo design, non-macOS asset adaptation, Xcode implementation alone, signing, notarisation, packaging, or App Store clearance.

### Inputs

Mandatory:

- a real source image or editable source asset;
- target macOS version range and distribution context, or explicit permission to discover them from the project;
- operation: inspect, prepare, review-export, or implementation-handoff;
- whether stylistic or semantic changes are permitted.

Optional:

- repository/Xcode project path;
- existing asset catalogue or `.icon` file;
- brand invariants and approved source hierarchy;
- preferred source format and size;
- existing variants and prior preflight report.

Discoverable:

- deployment target, Xcode project settings, asset catalogues, icon files, Info.plist values, package/distribution scripts, brand assets, and repository instructions.

No actual image target means no icon generation or editing. The Skill may explain required inputs, then must pause.

### Outputs

Default inspection output is an inline preflight report. Create files only when the operation requires them:

- prepared source: user-approved path such as `assets/icon-source-preflight.png`;
- preview grid: temporary by default, durable only when requested;
- handoff: `docs/icon-implementation-handoff.md` only when repository integration is the next authorized step.

The report separates:

- design readiness;
- source/export readiness;
- Xcode or Icon Composer integration readiness;
- runtime inspection status;
- signing, packaging, notarisation, and App Store status as explicitly not assessed unless separately performed.

### Current platform baseline and freshness rule

Every run making version-sensitive claims must re-check current official Apple documentation or current Build macOS Apps guidance and record the source/date.

As of 2026-07-16, Apple’s current published guidance says:

- iPhone, iPad, and Mac share a 1024 px icon canvas in the current design system;
- exported Icon Composer layers must not include the rounded-rectangle or circle mask because the mask is applied later;
- source layers can use SVG for scalable flat artwork and transparent PNG for raster/non-SVG content;
- Icon Composer can save a `.icon` file for Xcode and supports multiple appearance/platform previews;
- complex or illustrative artwork may still be delivered as individual images to Xcode;
- Apple’s current Icon Composer download requires macOS Tahoe 26.4 or later.

These are dated scope facts, not permanent rules. The Skill must not hard-code them without a freshness checkpoint.

### Workflow

1. Inspect repository instructions, project target, working tree, and actual source hierarchy.
2. Re-check current official Apple icon and Xcode delivery guidance for the target version range. Record source/date and any tool availability.
3. Inspect source dimensions, aspect ratio, format, color/alpha state, visual/alpha bounds, edge occupancy, likely rounded-mask signature, external halo/shadow, framing, contrast, detail density, and scaling limits.
4. Open and visually inspect the source. Automated heuristics may flag likely problems but cannot decide subjective platform fit alone.
5. Distinguish:
   - source artwork and internal subject lighting/depth;
   - dynamic/platform material treatment;
   - baked outer container, mask, frame, glow, or drop shadow.
6. Render a labeled evaluation grid at representative display sizes and against light, dark, and high-contrast backgrounds. These are review sizes, not claims about required asset-catalogue slots.
7. Produce findings with `Platform rule`, `Evidence-backed defect`, `Subjective craft concern`, or `Unverified` labels.
8. If preparation is authorized, choose the least invasive path:
   - crop or pad proportionally;
   - remove a detachable vector/layer mask or outer effect;
   - flatten/export approved layers correctly;
   - preserve the central subject and useful internal lighting;
   - produce a clean source without baking the platform mask.
9. If the shell/shadow is inseparable from a raster subject, stop with an editing handoff. Do not pretend a mechanical crop removed it. Route semantic repair to image editing or Product Design with the source locked as an invariant.
10. Verify the prepared source and preview grid. Compare source hashes, dimensions, alpha, bounds, small-size legibility, contrast, and visual balance.
11. Produce a Build macOS Apps/Xcode handoff naming the target, current Apple source, chosen delivery format, files, remaining integration, and checks still required.

### v0.0.1 editing boundary

v0.0.1 supports deterministic preparation only: proportional crop/scale/pad, detachable layer/mask removal, approved layer export, and non-semantic background cleanup when exact pixels or editable layers make the result reliable.

It does not use generative inpainting to reconstruct a subject, redraw the icon, or manufacture clean edges from a baked raster shell. Those tasks require explicit redesign/edit authorization and specialist visual tooling.

### Verification

- Actual source exists, opens, and remains unchanged unless explicit replacement was authorized.
- Current Apple/platform claims have dated official sources.
- Visual bounds and edge clearance are measured and manually inspected.
- Likely baked mask, external halo/shadow, and internal subject shading are reported separately.
- Preview grid includes labeled small sizes and contrasting contexts.
- Prepared output meets the declared dimensions/format/alpha contract and remains sharp.
- Central subject geometry, identity, and intended internal depth are preserved.
- Handoff explicitly states what has not been integrated or release-validated.

### Guardrails

- Never generate or edit a specific icon without a real target image.
- Never treat “remove external shadow” as “remove all dimensionality.”
- Never bake a mask merely because older examples used one.
- Never state a subjective preference as an Apple requirement.
- Never claim App Store, signing, notarisation, or release readiness from visual inspection.
- Never overwrite source artwork by default.
- Never silently redesign or use generated approximations.
- Never make a version-compatibility claim from static bundled notes alone.

### Non-goals

- New icon concept or brand direction.
- General visual-format adaptation.
- Asset-catalogue/Xcode implementation as the primary job.
- Signing, packaging, notarisation, App Store review, or marketing artwork.
- Automatic `.icon` authoring without current tool support and human preview.

### Dependencies and boundaries

- Soft-use `visual-asset-adapter` for deterministic image evidence and preparation when installed. Retain a self-contained narrow probe/preview fallback for extraction.
- Build macOS Apps owns `.icon`/asset-catalogue integration, Xcode build/run, runtime inspection, signing, packaging, and notarisation.
- Product Design or image generation owns creative exploration or semantic repair after explicit authorization.
- Authored macOS Design owns app interface design, not application icon production.

### Suggested Skill structure

```text
skills/macos-app-icon-preflight/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── apple-requirements.md
│   ├── icon-review-rubric.md
│   └── quality-gates.md
└── scripts/
    ├── inspect_icon.py
    └── render_preview_grid.py
```

`apple-requirements.md` is a dated source index and refresh protocol, not a timeless copy of Apple rules.

### v0.0.1 acceptance criteria

1. Detect and visually confirm a likely pre-baked rounded-square shell.
2. Distinguish an external shadow/halo from useful internal subject shading.
3. Measure and identify insufficient or excessive edge padding.
4. Render and inspect representative small-size previews on multiple backgrounds.
5. Prepare authorized source artwork when the required change is deterministic and does not redesign the subject.
6. Stop and produce a specialist-edit handoff when a baked raster shell cannot be removed faithfully.
7. Produce an implementation handoff for an existing macOS project with current official source links.
8. Refuse or pause when no actual source image exists.
9. Avoid every release-readiness claim beyond inspected evidence.
10. Work whether or not Visual Asset Adapter is installed by using a narrower fallback path.

### Deferred capabilities

- Semantic raster reconstruction or inpainting.
- Automated Icon Composer project generation.
- Full `.app` and App Store asset audit.
- Cross-platform icon-family production.
- Visual regression automation across macOS versions.
- Store-listing screenshot or marketing-icon workflows.

## 6. Skill scope: `project-skill-scaffold`

### One-sentence job

Generate or safely refresh a lean project-specific orchestration Skill from a stable specification and inspectable repository, without implementing the project or hard-coding transient progress as truth.

### User problem

Long-running agent builds lose project authority, milestone position, safety invariants, settled decisions, specialist routing, and evidence between sessions. A generic handoff prompt helps once; a project Skill should repeatedly reconstruct the correct next bounded slice without replacing the specification, build log, or implementation expertise.

### Invocation triggers

Invoke when the user asks to:

- scaffold `build-<project>` from a repository and stable specification;
- turn a mature project plan into a reusable coding-session Skill;
- refresh an existing project Skill after requirements or implementation state changes;
- validate that a project Skill still points to current authoritative sources and milestones;
- create a fresh-session opening instruction for a project.

Do not invoke for vague ideas, general project setup, implementing milestones, writing a full specification, producing a one-off handoff only, maintaining a diary/log only, or converting every repository into a Skill.

### Stability gate

A project is scaffoldable only when all hard gates pass:

1. One authoritative specification or clearly ordered set of authoritative documents is designated.
2. Product name, repository root, purpose, and intended implementation environment are known.
3. At least one milestone has bounded scope and evidence-based acceptance criteria.
4. Project invariants, material constraints, and known non-goals are explicit.
5. Current repository state can be inspected.
6. Status authority is defined: for example, verified behavior and tests over logs, logs over plans.
7. Unresolved decisions are explicitly labeled and do not make the next milestone incoherent.
8. Repository delivery rules are available or the default safe branch/draft-PR contract is accepted.

If any gate fails, return `Needs specification` with exact missing evidence. Do not scaffold a confident orchestration Skill from a brainstorm.

### Inputs

Mandatory, whether supplied or discovered:

- local repository or accessible repository URL;
- stable authoritative specification source;
- project name and normalized Skill slug;
- milestone/phase structure with acceptance evidence;
- current status authority;
- invariants, constraints, and non-goals;
- repository instructions and delivery conventions.

Optional:

- build/decision log;
- acceptance matrix;
- terminology/glossary;
- plugin/Skill routing preferences;
- explicit session model/provenance rules;
- existing project Skill for refresh;
- handoff/progress templates already owned by the project.

Discoverable:

- repository structure, languages, targets, manifests, CI, tests, docs, branches, tags, and history;
- specification and log paths;
- current milestone evidence;
- installed specialist Skills and plugins;
- existing project-specific Skill and its generated-source manifest.

### Generated output

Default minimal generated structure:

```text
skills/build-<project>/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── project-map.md
│   ├── milestone-map.md
│   ├── repository-contract.md
│   └── source-manifest.json
└── scripts/
    ├── inspect_project_state.py
    └── validate_project_skill.py
```

Conditional files:

- `references/terminology.md` only when project language is specialized or collision-prone;
- `references/acceptance-map.md` only when acceptance criteria cannot remain concise in `milestone-map.md`;
- templates only when the project already requires a repeatable session/log schema.

Do not generate `README.md`, example invocations, or a generic templates directory by default. `SKILL.md` contains the opening invocation, authority rules, state reconstruction, next-slice selection, specialist routing, safeguards, verification, and finish/handoff contract.

### Status architecture

Embed stable structure, not transient completion:

- `milestone-map.md` defines milestone IDs, intent, prerequisites, evidence gates, and cut/defer relationships.
- `repository-contract.md` defines authority, invariants, delivery rules, and specialist boundaries.
- `project-map.md` maps authoritative documents and important repository surfaces.
- `source-manifest.json` records scaffold schema version, source paths, content hashes, and generated ownership. Hashes are refresh provenance, not project status.
- `inspect_project_state.py` calculates current evidence at session start from repository state, logs, tests, and named acceptance markers. It reports observations and conflicts; it does not mark completion from filenames alone.
- The Skill chooses the earliest incomplete milestone whose entry criteria are evidenced, then asks only for an owner decision that materially changes scope.

Do not encode a branch name, current commit, date-relative deadline, installed plugin version, or `Milestone X complete` as permanent instruction text.

### Workflow

1. Inspect repository instructions, working tree, history, specification candidates, logs, manifests, CI, tests, and any existing project Skill.
2. Apply the stability gate and report `Scaffoldable`, `Scaffoldable with explicit unknowns`, or `Needs specification`.
3. Establish authority order among specification, decision log, verified repository behavior, build log, and user decisions.
4. Build a concise project map pointing to sources rather than copying large specifications.
5. Convert milestones into executable slices with entry criteria, bounded goal, allowed files/surfaces, required specialist routes, verification, exit evidence, and next-state rule.
6. Encode invariants, non-goals, privacy/safety rules, delivery rules, terminology, and forbidden shortcuts.
7. Map installed specialists by job and mark each dependency `required`, `recommended`, or `optional`. Always describe a fallback or blocker outside CodexToolkit.
8. Generate the minimal project Skill into a new path or a proposed refresh path.
9. Generate the state inspector and validator from generic scaffold-owned templates, then run them against the repository.
10. Compare documented status with repository evidence. Report conflicts without selecting the more optimistic source.
11. For a refresh, create a proposed diff. Update only scaffold-owned blocks/files identified by `source-manifest.json`; preserve unmanaged bytes and hand-edited sections. Never overwrite the active Skill silently.
12. Validate trigger metadata, referenced paths, source hashes, milestone IDs, authority order, optional markers, script behavior, and the fresh-session starter.
13. Review the complete diff and hand off to the normal repository delivery workflow only after owner approval.

### Refresh and stale detection

A generated Skill is stale when any of these are true:

- an authoritative source content hash changed;
- an authoritative path disappeared or a new competing authority appeared;
- milestone IDs or acceptance criteria changed;
- the state inspector finds evidence that conflicts with the last recorded project map;
- required specialist names are unavailable and no fallback remains;
- the generated schema is older than the scaffold’s supported migration floor.

Stale does not mean wrong. Refresh produces a reviewable proposed diff and a conflict report.

For v0.0.1, refresh must never perform an unreviewed in-place rewrite. It may update scaffold-owned blocks with stable IDs only after showing the proposed diff; otherwise it writes a sibling temporary candidate outside the active Skill and requests review.

### Relationship to adjacent workflows

- **Project orchestration:** this Skill’s output reconstructs authority and selects the next eligible bounded slice every session.
- **Project handoff:** a one-time or end-of-session state transfer; the generated Skill may consume it as evidence but does not replace it.
- **Session starter:** the concise opening instruction produced by the project Skill; not a separate source of truth.
- **Spec-to-build:** converts requirements into an implementation plan; Project Skill Scaffold consumes stable milestone structure but does not redo detailed technical planning.
- **Build journal/log:** append-only record of observed work; the generated Skill reads it according to authority rules but does not infer truth from prose.

### Verification

- Skill Creator validation passes for the generated Skill.
- Every required referenced path exists; optional paths are labeled and absence-tested.
- Source manifest hashes match the inspected sources at generation time.
- Milestone IDs are unique and each has entry, exit, and evidence criteria.
- State inspector distinguishes observed, inferred, unverified, and conflicting status.
- No milestone is marked complete from filename presence alone.
- Fresh-session starter identifies authority, current evidence, next eligible slice, required specialists, and finish contract.
- Refresh leaves hand-edited/unmanaged bytes unchanged and produces a reviewable diff.
- Existing project Skill is never overwritten without explicit approval.

### Guardrails

- Never scaffold from an unstable brainstorm.
- Never copy a large specification into `SKILL.md`.
- Never collapse requirements, observed implementation status, and future plans.
- Never make the project Skill a substitute for implementation specialists.
- Never hard-require a toolkit-only Skill without an extraction-safe fallback or explicit blocker.
- Never invent milestone completion, tests, commits, provenance, or owner decisions.
- Never silently replace hand-maintained content.
- Never commit to the default branch or publish without authority.

### Non-goals

- Implementing the project.
- Writing or stabilizing the project specification.
- Generic repository scaffolding.
- Full project management, issue creation, or roadmap ownership.
- Replacing build logs, ADRs, tests, Git history, or specialist plugins.
- Autonomous refresh daemon.

### Dependencies and boundaries

- Uses Skill Creator and Plugin Creator for generated structure and validation.
- May consume future `repository-product-brief`, `spec-to-build`, `project-handoff`, or `build-journal` outputs, but none is required in v0.0.1.
- Routes technical implementation to installed specialists such as Build macOS Apps; it does not vendor those instructions.
- Conforms to future `repo-delivery-guard` or the existing authorized publishing workflow.
- Build Premonition is the primary positive reference, not a template to clone literally.

### Suggested scaffold-Skill structure

```text
skills/project-skill-scaffold/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── stability-gate.md
│   ├── generated-skill-contract.md
│   ├── refresh-contract.md
│   └── quality-gates.md
├── assets/templates/
│   ├── project-map.md
│   ├── milestone-map.md
│   ├── repository-contract.md
│   └── source-manifest.json
└── scripts/
    ├── inspect_scaffold_inputs.py
    └── validate_generated_skill.py
```

Use Python rather than shell for path handling, JSON, hashing, cross-platform ChatGPT/Codex execution, and deterministic diagnostics. Generated state inspectors may be language-aware through configuration, but the base mechanism remains language-agnostic.

### v0.0.1 acceptance criteria

1. Scaffold a new `build-<project>` Skill from a repository with a stable spec and milestone plan.
2. Return `Needs specification` with precise missing gates for a vague idea.
3. Refresh an existing project Skill after one milestone is completed without embedding the transient commit as permanent truth.
4. Preserve hand-edited/unmanaged content and present the refresh diff before replacement.
5. Detect and report conflict between documented status and repository evidence.
6. Produce a self-contained fresh-session starter pointing to the correct next eligible milestone.
7. Validate every referenced file or explicit optional marker.
8. Route Premonition-style macOS work to Build macOS Apps without copying its implementation playbooks.
9. Extract the generated Skill into a standalone plugin without requiring CodexToolkit files.

### Deferred capabilities

- Automatic migration across generated schema versions.
- Autonomous in-place refresh.
- Issue/roadmap synchronization.
- Broad language-specific project analyzers.
- Automatic milestone completion from CI APIs.
- Multi-repository project orchestration.
- Shared organisation-wide project policy packs.

## 7. Overlap analysis

| Existing capability | Potential duplication | Scoped boundary |
| --- | --- | --- |
| Build Premonition | Project-specific authority, milestones, routing, and session finish | It is a worked example and pilot. Project Skill Scaffold generates the project-specific orchestration contract; it does not generalize Premonition’s content or Sol provenance rules into every project. |
| Maintain Premonition Logs | Project status and handoff evidence | Logs remain append-only evidence. Project Skill Scaffold reads status sources but does not own diary or ledger maintenance. |
| Launch Pack | Claims, assets, channel planning, release handoff | None of the four owns a release package. Naming reports and approved assets may feed Launch Pack later. |
| GitHub Social Preview | Exact-brand GitHub social card composition | Visual Asset Adapter handles faithful mechanical adaptation; GitHub Social Preview owns repository narrative, product copy, 1280 × 640 composition, and thumbnail survival. |
| README Front Door | Banner placement and repository opening copy | Visual Asset Adapter produces an approved banner; README Front Door decides placement and edits the README. |
| Authored macOS Design | Native app interface direction and implementation | macOS App Icon Preflight owns icon source readiness only. |
| Open-Source PR Preflight | Contribution readiness and PR package | The candidates conform to delivery rules but do not duplicate PR preflight or publication. |
| Skill Creator / Plugin Creator | Skill/plugin scaffold mechanics | Project Skill Scaffold orchestrates project-specific evidence into a generated Skill and delegates structural validation to these maintained standards. |
| Build macOS Apps | Xcode integration, runtime, signing, packaging, notarisation | macOS App Icon Preflight stops at verified source/handoff. Build macOS Apps integrates and validates the app. |
| Product Design | Visual exploration, remixes, design audits, prototypes | Visual Asset Adapter and icon preflight begin from approved source and reject open-ended redesign. Route ideation or semantic redesign to Product Design. |
| Image generation/editing | New raster images and semantic edits | Adapter uses deterministic transforms where possible. Icon preflight may hand off inseparable raster repair; neither asks generation to approximate a final logo/wordmark. |
| GitHub tooling | Repository search and publication | Technical Name Check may use GitHub search for evidence. Publication remains separate and explicitly authorized. |
| Generic image compression | Byte reduction only | Visual Asset Adapter includes compression as one verified step inside a larger source-fidelity and destination contract. |

No candidate should be merged into another existing Skill. The overlaps are orchestration boundaries, not identical jobs.

## 8. Shared architecture

### Dependency shape

```text
repository or concise product brief
├── technical-product-name-check
└── project-skill-scaffold

approved visual source
└── visual-asset-adapter
    └── macos-app-icon-preflight (soft use only)
```

This is an information flow, not a required runtime graph.

### Shared conventions

All four Skills use:

- the shared evidence vocabulary in section 2;
- exact source paths/URLs and inspected-at timestamps;
- `Passed`, `Failed`, `Blocked`, `Skipped`, and `Not applicable` verification states;
- a final result containing outcome, evidence, limitations, files, and exact next action;
- non-destructive outputs by default;
- current-source refresh for web/platform claims;
- explicit authority before repository publication or external state change.

### Shared scripts

Do not create a toolkit-level `scripts/` library in the first implementation wave.

- Naming normalization and report validation are unique to Technical Product Name Check.
- General image inspection/adaptation/verification belong inside Visual Asset Adapter.
- macOS icon preview heuristics need Apple-specific labels and manual review; keep a narrow fallback inside Icon Preflight and soft-route to Visual Asset Adapter when present.
- Project state inspection and generated-Skill validation belong inside Project Skill Scaffold and generated project Skills.

If two mature Skills later share more than a small stable utility, extract a versioned library with a vendoring path for standalone plugins. Do not create coupling in anticipation.

### File naming

- Skill directories and names use lower-case hyphen-case.
- UI metadata lives at `agents/openai.yaml`.
- Detailed instructions use lower-case hyphen-case filenames in `references/`.
- Reusable output templates live under `assets/templates/`, not a custom top-level `templates/` directory.
- Scripts use lower-case snake_case and emit machine-readable JSON plus concise human output where useful.
- Durable reports use repository-owned `docs/` locations only when explicitly requested; otherwise return inline or temporary evidence.

### Versioning

- Each Skill enters CodexToolkit as workshop-stage v0.0.1 in design maturity, while the containing plugin advances one patch version per focused implementation PR.
- Skill frontmatter does not gain an unsupported version field.
- Script/report schemas use an explicit integer schema version where machine compatibility matters.
- A later standalone extraction starts with its own plugin `0.0.1` or a consciously chosen maturity version; toolkit history is recorded in the extraction PR, not encoded as a runtime dependency.

### Extractability rules

- `SKILL.md` explains the complete job, triggers, workflow, boundaries, and fallback behavior.
- References are task-essential and local to the Skill.
- Cross-Skill calls are soft and named by capability; missing specialists produce a fallback or blocker.
- No Skill imports another Skill’s filesystem path.
- No generated output assumes the CodexToolkit repository name or layout.
- Project-specific examples are labeled examples and excluded from validation logic.
- Graduation copies the complete Skill directory, reruns Skill/Plugin validation, and updates toolkit routing in a separate focused change.

### Repository delivery

Each candidate ends with a handoff to `repo-delivery-guard` when available, otherwise the repository’s current safe workflow:

1. inspect instructions, branch, and working tree;
2. isolate a dedicated branch;
3. keep the diff scoped;
4. run validation and inspect the final diff;
5. commit intentionally;
6. open a draft PR;
7. never create a ceremonial issue;
8. never modify the default branch directly.

The four Skills reference this boundary rather than reproducing its mechanics in full.

## 9. Implementation sequence

### Stage 0 — approve this scope

Expected files:

- `docs/scopes/workshop-skills-build-scope.md` only.

Verification checkpoint:

- Confirm the document matches current repository Skills, installed specialist boundaries, current official Apple sources, and official registry surfaces.
- Confirm no candidate directory, manifest version, or README capability claim was added.

Human review:

- Approve the four boundaries, staged release plan, reduced icon editing scope, and deferred project-scaffold pilot.

Definition of done:

- Scope PR approved and merged with no implementation artefacts.

### Stage 1 — Technical Product Name Check

Expected files:

- the seven files listed in its suggested structure;
- root README and plugin manifest updates for v0.0.8.

Verification checkpoint:

- Skill and plugin validation;
- normalization-script unit fixtures;
- naming-report validator pass/fail fixtures;
- one single-name, one three-name comparison, one cross-category collision, and one re-run delta exercise using current sources.

Human review:

- Review risk rubric, required coverage selection, citations, and legal boundary.

Definition of done:

- The Skill can produce a dated, source-backed, category-tailored report without calling a result “available” or “legally clear.”

### Stage 2 — Visual Asset Adapter

Expected files:

- the six files listed in its suggested structure;
- root README and plugin manifest updates for v0.0.9.

Verification checkpoint:

- backend capability detection;
- inspect/adapt/verify success and failure fixtures;
- alpha-channel versus transparent-pixel test;
- source-hash preservation;
- exact dimension/byte-limit tests;
- full-size and crop-preview human inspection.

Human review:

- Approve transformation classes, target profiles, source-fidelity report, and failure behavior when source/backend is missing.

Definition of done:

- The Skill completes deterministic adaptations without altering the approved core and reports exact technical/visual evidence.

### Stage 3 — macOS App Icon Preflight

Expected files:

- the six files listed in its suggested structure;
- root README and plugin manifest updates for v0.0.10.

Verification checkpoint:

- current Apple-source refresh test;
- baked-mask, external-shadow, internal-shading, padding, and small-size scenario fixtures;
- preview-grid generation;
- deterministic-preparation success fixture;
- inseparable-raster-shell refusal fixture;
- Build macOS Apps handoff review.

Human review:

- Review which findings are Apple rules versus craft judgment, the dated target matrix, and the no-release-readiness boundary.

Definition of done:

- The Skill diagnoses supplied artwork, safely prepares only deterministic cases, and produces a current-source implementation handoff without redesign or packaging claims.

### Stage 4 — Project Skill Scaffold pilot

Expected files:

- a temporary evaluation plan outside installed Skill paths;
- test inputs from Build Premonition and one structurally different project such as a cross-provider tool or library;
- no plugin manifest change yet.

Verification checkpoint:

- stability gate classifies stable versus vague inputs;
- generated structure comparison across two projects;
- status-conflict and stale-source exercises;
- refresh preservation test with hand-edited content.

Human review:

- Approve the minimal generated contract and identify Premonition-specific leakage.

Definition of done:

- One stable generator contract works for two different projects without copying large specs or hard-coding transient progress.

### Stage 5 — Project Skill Scaffold implementation

Expected files:

- the files listed in its suggested scaffold-Skill structure;
- root README and plugin manifest updates for v0.0.11 or later.

Verification checkpoint:

- Skill and plugin validation;
- all nine acceptance scenarios;
- generated-Skill validation;
- extraction test in a temporary standalone plugin;
- reviewable refresh diff with byte-preservation evidence.

Human review:

- Approve stability gate, generated ownership model, state inference boundaries, and fresh-session starter.

Definition of done:

- The Skill reliably creates and refreshes extraction-safe project orchestration without overwriting hand work or inventing status.

## 10. Risks and open questions

### Current macOS icon requirements

Risk: Apple’s icon design and delivery model is actively evolving. Static bundled sizes and old mask assumptions can become wrong.

Decision: every version-sensitive run refreshes official Apple sources and records date/target/tool availability. `apple-requirements.md` stores source pointers and a refresh procedure, not immutable claims. Open question: which Xcode and macOS target combinations should be included in initial fixtures after implementation begins?

### Icon Composer availability

Risk: Apple currently states Icon Composer requires macOS Tahoe 26.4 or later, while ChatGPT/Codex execution environments may be Linux or an older Mac.

Decision: Icon Composer is an optional current-platform handoff, not a hard runtime dependency. The Skill can inspect and prepare sources elsewhere but cannot claim `.icon` preview or Xcode integration without the actual tool/runtime evidence.

### External registry coverage and rate limits

Risk: APIs differ in authentication, result semantics, rate limits, and reliability; some marketplaces expose only web search.

Decision: v0.0.1 uses current official APIs/search surfaces through existing web/GitHub tools, records blocked/incomplete results, and avoids a monolithic crawler. Open question: after real runs, which registries justify maintained adapters?

### Availability semantics

Risk: a 404 or empty search result can be temporary, incomplete, case-normalized, reserved, or unavailable for policy reasons.

Decision: report only the observed state. “Not found” never means available or reservable. Namespace reservation remains a user action.

### Image backend availability

Risk: Pillow, ImageMagick, `sips`, color-management tools, and vector renderers vary by environment.

Decision: scripts capability-check. PNG inspection should have the narrowest dependency-free path feasible; transformations declare their backend and fail clearly when unsupported. Open question: should v0.0.1 formally support SVG adaptation or restrict SVG to deterministic passthrough/placement pending a renderer spike?

### Fidelity measurement

Risk: perceptual metrics can miss a wrong logo or reward a blurry approximation.

Decision: source identity, hashes, transform parameters, aspect ratio, visual bounds, and human comparison remain primary. Automated similarity is supporting evidence only and is deferred.

### Generated project-Skill synchronization

Risk: embedding milestone status makes Skills stale; calculating status can overclaim from weak signals.

Decision: embed stable milestone definitions and authority, calculate observations at session start, and report conflicts. Source hashes detect refresh need without becoming project truth. Open question: how much managed-block machinery is justified after the two-project pilot?

### Hand-edit preservation

Risk: automated refresh can erase useful project-specific judgment.

Decision: v0.0.1 refresh is proposed-diff-first and updates only scaffold-owned content after review. No silent in-place regeneration.

### Shared utility maintenance

Risk: a shared library improves consistency but creates extraction and version-coupling costs.

Decision: no shared runtime library initially. Revisit only after duplicated stable code appears in released Skills.

### Current web access

Risk: Technical Product Name Check cannot produce a current availability conclusion offline.

Decision: offline work may normalize variants and plan coverage, but the final result is `Blocked` or explicitly historical until current sources are checked.

### Actions requiring explicit confirmation

Explicit user authority is required before:

- semantic image editing or redesign;
- overwriting approved source assets;
- changing README/code references beyond the requested artefact;
- accepting a generated project-Skill refresh over hand-maintained content;
- installing tools or dependencies outside normal repository requirements;
- purchasing domains, reserving handles/namespaces, or creating repositories/packages;
- committing, pushing, opening/updating PRs, or any external publication.

## 11. Final recommendation

### `technical-product-name-check` — Build now

The job is narrow, recurring, evidence-heavy, and clearly distinct from product ideation and legal clearance. Its main maintenance risk is current-source coverage, controlled in v0.0.1 by using live tools and a report validator rather than a registry crawler.

### `visual-asset-adapter` — Build now

This offers the highest immediate value because the same fidelity, crop, transparency, and file-size failures recur across repository and social assets. Keep it deterministic and source-led; route semantic edits elsewhere.

### `macos-app-icon-preflight` — Build now with reduced editing scope

Keep it separate from Visual Asset Adapter because platform rules, target freshness, small-size icon judgment, and Xcode handoff create a distinct invocation. v0.0.1 should inspect, preview, prepare deterministic cases, and hand off; defer semantic shell removal and automated Icon Composer generation.

### `project-skill-scaffold` — Defer implementation, retain candidate

Do not merge it with handoff or spec-to-build. Its project-orchestration job is real and strategically valuable, but a generic generator derived from one project would likely encode Premonition-specific assumptions or stale status. Pilot the generated contract across two different projects, then build it as the fourth focused release if the stability and refresh contracts hold.

No candidate is rejected. None should be merged into another Skill. The recommended program is three immediate bounded builds followed by one evidence-gated project-scaffold implementation.

## 12. Current primary sources

Checked 2026-07-16:

- Apple Human Interface Guidelines, [App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons/)
- Apple Developer, [Icon Composer](https://developer.apple.com/icon-composer/)
- Apple WWDC25, [Say hello to the new look of app icons](https://developer.apple.com/videos/play/wwdc2025/220/)
- Apple WWDC25, [Create icons with Icon Composer](https://developer.apple.com/videos/play/wwdc2025/361/)
- Apple Developer, [Configuring your app icon using an asset catalog](https://developer.apple.com/documentation/xcode/configuring-your-app-icon)
- Apple Developer, [Design Resources](https://developer.apple.com/design/resources/)
- GitHub Docs, [REST API endpoints for search](https://docs.github.com/en/rest/search/search)
- GitHub Docs, [Rate limits for the REST API](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api)
- npm Docs, [Package name guidelines](https://docs.npmjs.com/package-name-guidelines/)
- PyPI Docs, [JSON API](https://docs.pypi.org/api/json/)
- Homebrew Formulae, [JSON API documentation](https://formulae.brew.sh/docs/api/)
- crates.io, [Data access](https://crates.io/data-access)
- RubyGems Guides, [RubyGems.org API](https://guides.rubygems.org/rubygems-org-api/)
- Maven Central, [REST API](https://central.sonatype.org/search/rest-api-guide/)
- [Swift Package Index](https://swiftpackageindex.com/)

These links are implementation inputs, not permanent cached conclusions. Each Skill must refresh current external facts when it runs.
