# Generated Skill contract

## Input JSON

```json
{
  "project_name": "Example",
  "skill_slug": "build-example",
  "purpose": "One confirmed sentence.",
  "implementation_environment": "Swift 6 and macOS",
  "authoritative_sources": [{"path": "SPEC.md", "role": "specification", "required": true}],
  "authority_order": ["verified tests", "SPEC.md", "decision log", "build log"],
  "milestones": [{
    "id": "M0",
    "title": "Bounded milestone",
    "goal": "One bounded outcome",
    "prerequisites": [],
    "entry": ["Entry evidence"],
    "evidence": ["Command or observable acceptance evidence"],
    "exit": ["Exit evidence"],
    "specialists": ["build-macos-apps:swiftui-patterns"]
  }],
  "invariants": ["Stable rule"],
  "non_goals": ["Explicit exclusion"],
  "delivery_rules": ["Use a focused branch and draft PR"],
  "specialists": [{"name": "build-macos-apps", "level": "recommended", "job": "Native implementation", "fallback": "Use current Apple documentation and repository conventions"}],
  "unknowns": [],
  "status_file": "BUILD_STATUS.json"
}
```

`status_file` is optional and repository-relative. Its supported shape is:

```json
{"milestones":{"M0":{"state":"complete","evidence":[{"kind":"test","result":"pass","detail":"swift test"}]}}}
```

The generated inspector treats this as documented evidence. Completion requires a non-empty evidence list, remains subject to re-verification, and is never inferred merely from file existence.

## Generated structure

```text
build-project/
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

The manifest records schema, source hashes, milestone contracts, managed paths, and generation hashes. It contains stable structure and provenance, not current completion.

The generated Skill must remain usable when copied out of CodexToolkit. Specialist routes are soft unless explicitly required, and every non-portable route has a fallback or a clear blocker.
