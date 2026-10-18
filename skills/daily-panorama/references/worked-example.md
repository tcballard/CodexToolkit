# Worked example: 17 October 2026

Tom supplied the full Today in Omarchy edition and an existing green masthead. He required the original headlines and preferred a terminal background, then approved the taller mobile direction on 18 October 2026. The 9:19.5 format was chosen for opened-panel reading; native X viewing remains unverified.

The example’s four stories are Try Omarchy 1.0/1.0.1, Snapdragon hardware video decoding, iPhone Clipboard and Tom’s plugin/theme skill releases. The dated release notes and merged PR support their availability distinctions. The clipboard README was checked after the edition and had evolved; the marketplace joining date was not independently established, so that claim is omitted.

`assets/example/edition.json` contains the concise adapted copy, exact headline words, source notes and a caption draft. It is historical worked material, not fresh news. The emoji markers remain metadata, matching the approved visual treatment. `assets/example/approved-preview.png` records the accepted phone-shaped design; font outlines in the portable renderer may differ slightly from the initial system-font pilot.

Render it from the skill directory:

```bash
npm ci --prefix scripts
node scripts/render.mjs assets/example/edition.json /absolute/path/editions/2026-10-17-example
```

Review all panels, then replace the example’s reporting for the next edition. Never copy its dates, release status or source-verification claims into a later edition without checking again.
