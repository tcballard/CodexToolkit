# Stability gate

All hard gates must pass.

1. **Authority:** one authoritative specification or an explicit ordered set exists.
2. **Identity:** project name, normalized Skill slug, purpose, repository, and implementation environment are known.
3. **Milestones:** at least one bounded milestone has entry, exit, and evidence criteria.
4. **Constraints:** invariants, material constraints, and non-goals are explicit.
5. **Inspectable state:** the repository and named required sources can be read.
6. **Status authority:** the order between verified behavior/tests, decisions, logs, plans, and user decisions is explicit.
7. **Unknowns:** unresolved decisions are labeled and do not make the next milestone incoherent.
8. **Delivery:** repository rules exist or the safe branch/draft-PR default is accepted.

Verdicts:

- `Scaffoldable`: every hard gate passes and no material unknown remains.
- `Scaffoldable with explicit unknowns`: every hard gate passes; bounded unknowns are recorded.
- `Needs specification`: any hard gate fails.

Do not downgrade a hard gate to make generation proceed. A vague product idea, unbounded roadmap, or file with a promising name is insufficient.
