# Naming channel matrix

## Universal checks

Run for every candidate:

| Surface | Check | Evidence |
| --- | --- | --- |
| General web | Exact quoted name, normalized variants, product category | Direct results and queries |
| GitHub | Repository, organisation/user, same-category projects, relevant code/package references | GitHub search plus opened repository pages |
| Products and companies | Exact and near commercial/open-source uses | Primary product/company pages |
| Search ambiguity | Dominant unrelated meanings and discoverability | Representative result mix |

## Category-specific checks

Select from actual distribution plans:

| Product | Required when planned | Common optional checks |
| --- | --- | --- |
| macOS app | GitHub, Homebrew cask/formula, App Store display-name search | Domain, CLI/helper command, bundle terminology |
| Python package | PyPI project name, GitHub, installed CLI command | Conda, domain, docs slug |
| Rust crate | crates.io crate name, GitHub, binary command | Homebrew, domain |
| JavaScript package | npm package/scope, GitHub, `bin` command | CDN/search ambiguity, domain |
| Swift package | GitHub, Swift Package Index | package/product/module names |
| Ruby gem | RubyGems, GitHub, executable | Homebrew, domain |
| JVM library/tool | Maven Central coordinates, GitHub, command | plugin marketplaces, domain |
| ChatGPT/Codex plugin | GitHub, plugin name, Skill-name collisions in intended distribution | package/repository slug, domain |
| Editor plugin | Relevant VS Code/JetBrains marketplace, GitHub | package/command, domain |

## Source policy

- Prefer official APIs and registry pages for namespace state.
- Use primary product/repository pages to classify material collisions.
- Record the exact checked variant because registries normalize case, punctuation, and separators differently.
- `404`, empty search, or no exact result means `Not found` only for that source and timestamp.
- Record authentication, rate-limit, regional, or indexing failures as `Blocked` or `Ambiguous`.
- Do not make every registry mandatory. More unchecked surfaces do not improve a report when the product will never distribute there.
