# Quality gates

Do not claim completion until all applicable gates pass.

## Source

- The real source exists, opens, and has a recorded SHA-256.
- Source priority and immutable elements are explicit.
- Source resolution supports the requested output, or scaling risk is disclosed.
- The post-export source hash matches the pre-export hash.

## Output mechanics

- File signature and requested format agree.
- Exact width and height pass.
- Actual byte size meets any ceiling.
- Output opens without corruption.
- Core scaling is proportional.
- The original source was not overwritten.

## Alpha and color

- Alpha-channel presence is recorded separately from transparent-pixel presence.
- Required transparency is measured, not inferred from a `.png` extension.
- Background and palette match the approved contract.
- Color-profile preservation or removal is reported.

## Composition

- Protected content stays inside every required safe area/crop.
- No logo, wordmark, embedded typography, or approved copy was approximated.
- Exact added text matches approved spelling and punctuation.
- Full-resolution output was visually inspected.
- At least one representative reduced/cropped preview was visually inspected.
- Light/dark/checkerboard contexts were inspected when transparency matters.

## Delivery

- Evidence separates automated facts from manual visual judgment.
- Limitations and unsupported formats are explicit.
- Repository references changed only when authorized and resolve correctly.
- No commit, push, or publication occurred without explicit scope.
