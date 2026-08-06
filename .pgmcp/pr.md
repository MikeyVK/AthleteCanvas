<!-- .pgmcp\pr.md -->
<!-- template=pr version=93bb9b4e created=2026-08-06T15:37Z updated= -->
# chore: align Codex role skills with PGMCP workflows

Aligns the repository's Codex role-skill model with the existing Antigravity workflow entrypoints while keeping `.agents/workflows/` as the single procedural source. This maintenance PR relates to the ongoing tracker #22 but intentionally does not close it.
## Changes
- Documents the Antigravity-to-Codex role and workflow mapping in `AGENTS.md`.
- Routes create, start, and end lifecycle requests internally from `pgmcp-co` to the canonical workflow files.
- Routes active-phase execution, discussion, and adjustment from `pgmcp-imp` to the canonical `go.md` workflow.
- Preserves QA and standalone research behavior and leaves the canonical workflow bodies unchanged.
- Includes the reinitialized PGMCP branch audit artifacts required by the ready workflow.

## Testing
- `quick_validate.py .agents/skills/pgmcp-co` → passed.
- `quick_validate.py .agents/skills/pgmcp-imp` → passed.
- Exact relative workflow links were inspected and resolve from both skill directories.
- `run_quality_gates(scope='files')` for the planning and changed documentation files → passed.
- `run_quality_gates(scope='branch')` → passed.
## Checklist

- [ ] Canonical workflow procedure text remains under `.agents/workflows/` only
- [ ] Lifecycle merge and branch-deletion actions still require explicit human invocation
- [ ] Changed Codex skills pass the official skill validator
- [ ] PR #31 is closed without merge and this is the sole replacement PR
- [ ] Human approval is required before merge

## Related Documentation
- `docs/development/issue22/planning.md`
- `AGENTS.md`
- `.agents/skills/pgmcp-co/SKILL.md`
- `.agents/skills/pgmcp-imp/SKILL.md`


## Deferred Work
No deferred items were established by the authoritative issue #22 planning artifact.

## Tracking State
Issue #22 remains open as the ongoing repository-maintenance tracker; this PR intentionally does not close it.
