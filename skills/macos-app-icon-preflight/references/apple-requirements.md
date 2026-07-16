# Apple requirements: source index and refresh protocol

This file is not a static platform specification. Re-open current official sources for every version-sensitive preflight and record the check date in the working report.

## Official source index

- [Human Interface Guidelines: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons/)
- [Icon Composer](https://developer.apple.com/icon-composer/)
- [WWDC25: Say hello to the new look of app icons](https://developer.apple.com/videos/play/wwdc2025/220/)
- [WWDC25: Create icons with Icon Composer](https://developer.apple.com/videos/play/wwdc2025/361/)
- [Xcode: Configuring your app icon using an asset catalog](https://developer.apple.com/documentation/xcode/configuring-your-app-icon)
- [Apple Design Resources](https://developer.apple.com/design/resources/)

## Last scope-time observation

Checked 2026-07-16. At that date Apple's public materials described a 1024-pixel canvas in the current iPhone/iPad/Mac design system, system-applied enclosure/masking, layered `.icon` files integrated with Xcode, and individual image delivery for some complex artwork. Apple's Icon Composer page stated that the download required macOS Tahoe 26.4 or later.

These observations may age. Re-check before repeating them.

## Refresh protocol

1. Establish target macOS versions, Xcode version, distribution path, and available tooling.
2. Open the HIG, Icon Composer page, relevant current Apple video/transcript, and Xcode documentation.
3. Prefer the most recent current documentation over an older talk when they differ.
4. Record title, direct URL, checked date, relevant statement in paraphrase, and which finding it supports.
5. Mark JavaScript-only, unavailable, or contradictory material `Unverified`; do not fill gaps from memory.
6. Treat design advice separately from build/package requirements.
7. Hand `.icon` or asset-catalogue mechanics to current Build macOS Apps/Xcode guidance.

Never infer App Store, signing, notarization, packaging, or runtime readiness from icon artwork guidance.
