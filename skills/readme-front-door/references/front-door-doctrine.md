# README front-door doctrine

## The seconds test

A visitor scanning the opening should be able to answer:

- What is the product?
- Who is it for?
- What useful outcome does it create?
- Why would I choose or inspect this instead of the obvious alternative?
- What is the fastest credible way to try or see it?

The opening is a decision surface, not a compressed table of contents.

## Evidence order

Prefer facts in this order:

1. Verified repository behavior, tests, and runnable artifacts.
2. Package, build, release, and compatibility metadata.
3. Maintained specifications and product documentation.
4. Current README content corroborated elsewhere in the repository.
5. User-provided confirmed facts.

When sources conflict, surface the conflict instead of selecting the stronger claim.

## Element selection

### Hero or visual

Use a visual when it accelerates recognition or demonstrates the product. A decorative banner that pushes the explanation below the fold has failed. Prefer one approved asset to a collage.

### Title and tagline

Use the canonical product name. A good tagline is specific enough that a plausible competitor could not claim it unchanged. Keep an exact user-supplied tagline exact.

### Explanation

Use one short paragraph. Lead with the product category or mechanism, the user, and the outcome. Put differentiation in a concrete constraint, workflow, platform, or proof—not an adjective pile.

### Command

Show one verified happy path. A command is not a proof point unless it actually runs in the supported environment. Do not guess package names, channels, flags, or shell syntax.

### Proof and demo

Choose the strongest compact evidence: a working demo, representative screenshot, measured result with methodology, supported platform behavior, or concrete capability visible in the repository. Link to deeper evidence instead of crowding the opening.

### Badges

Badges communicate current machine-readable facts. Use only a few that matter to adoption or trust, such as build status, package version, licence, or explicit platform compatibility. Do not use badges as decoration.

## Tone failures

Reject:

- revolutionary, magical, game-changing, seamless, or effortless without evidence;
- generic phrases such as "supercharge your workflow";
- throat-clearing about missions or the future;
- claims that merely restate the product name;
- forced jokes, faux rebellion, or conversational filler;
- multiple calls to action competing above the first substantive section.

## Structural patterns

These are ingredients, not templates:

- Developer tool: title → specific tagline → explanation → install command → proof/demo.
- Visual product: title → explanation → screenshot/demo → first-use action.
- Library: title + restrained badges → one-sentence category and distinction → install command → minimal example link.
- Early project: title → honest status → concrete purpose → supported run command → current limitation.

Vary the order when repository context makes another hierarchy clearer.
