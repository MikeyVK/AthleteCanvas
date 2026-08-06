<!-- docs/development/issue22/planning.md -->
<!-- template=planning version=130ac5ea created=2026-08-06T15:26Z updated=2026-08-06T15:31Z -->
# Codex-native PGMCP workflow routing

**Status:** DRAFT  
**Version:** 1.1  
**Last Updated:** 2026-08-06

---

## Purpose

Integrate the existing Antigravity workflow entrypoints with Codex role skills without duplicating procedure text or changing PGMCP authority.

## Scope

### In Scope

| Target | Expected outcome | Authoritative source |
|---|---|---|
| `AGENTS.md` | Add the runtime mapping and correct `open-issue` to `start-issue` | Existing role model and `.agents/workflows/` |
| `.agents/skills/pgmcp-co/SKILL.md` | Route explicit create, start, and end lifecycle requests to their existing workflows | `create-issue.md`, `start-issue.md`, `end-issue.md` |
| `.agents/skills/pgmcp-imp/SKILL.md` | Route active-phase execute, discuss, and adjust requests to `go.md` | `go.md` |
| `docs/development/issue22/planning.md` | Record scope, dependencies, validation, and closeout prerequisites | Issue #22 and files above |

### Reviewed But Unchanged

- `.agents/skills/pgmcp-qa/SKILL.md`: no internal Antigravity workflow is mapped to QA.
- `.agents/skills/pgmcp-research/SKILL.md`: standalone research startup remains non-phase-gated.
- `.agents/workflows/*.md`: remain the single procedural source for both Antigravity and Codex.
- `.agents/skills/*/agents/openai.yaml`: role names and prompts remain accurate.
- Production code, MCP tools, workflow contracts, and role authority.

## Decisions

1. Keep `.agents/workflows/` as the single procedural source of truth.
2. Treat workflows as internal procedural references, not Codex slash commands or discoverable sub-skills.
3. Keep `pgmcp-co`, `pgmcp-imp`, `pgmcp-qa`, and `pgmcp-research` as separate top-level skills.
4. Record the `/start` mapping in `AGENTS.md` only. Leave every role skill's existing startup section semantically unchanged and do not route Codex through `start.md`; this avoids imposing phase-gated startup on standalone research.
5. Require explicit user intent before routing `end-issue`; never infer merge or branch deletion authority.
6. Treat `create-issue` as normal coordination work: call `get_work_context` before loading it. Only `start-issue` and `end-issue` retain their explicitly documented lifecycle-boundary exceptions.

## Router Specification

### Coordination skill

Add an internal workflow-routing section to `.agents/skills/pgmcp-co/SKILL.md`:

| User intent | Workflow reference | Guardrail |
|---|---|---|
| Create/scaffold/submit an issue | `../../workflows/create-issue.md` | Read the workflow completely before acting |
| Start/open/bootstrap an issue lifecycle | `../../workflows/start-issue.md` | This is an explicit lifecycle-entry exception |
| End/merge/close an issue lifecycle | `../../workflows/end-issue.md` | Route only on explicit human invocation |

Normal coordination requests continue to call `get_work_context` first.

### Implementation skill

Add an internal workflow-routing section to `.agents/skills/pgmcp-imp/SKILL.md`:

| User intent | Workflow reference |
|---|---|
| Execute the active phase | `../../workflows/go.md` default mode |
| Discuss the active phase plan | `../../workflows/go.md` discuss mode |
| Apply a session-local adjustment | `../../workflows/go.md` adjust mode |

The workflow's initial `get_work_context` call and returned `phase_instructions` remain authoritative.

## Dependencies And Ordering

1. Record the runtime mapping and `start-issue` terminology in `AGENTS.md`.
2. Add coordination routing without weakening lifecycle exceptions or merge approval.
3. Add implementation routing without weakening `get_work_context` precedence.
4. Validate exact relative paths from each skill directory.
5. Validate both changed skill folders and review the final diff.

## Review Criteria

- Every routed path resolves from its owning `SKILL.md`.
- Every referenced workflow is read completely before execution.
- No workflow procedure is copied into a skill.
- `end-issue` still requires explicit human invocation.
- `pgmcp-imp` still calls `get_work_context` before active-phase execution.
- QA remains read-only and research remains non-mutating.
- Rendered links in this planning document resolve from `docs/development/issue22/`.
- No `.pgmcp/agents/antigravity/` generated copy is edited.

## Lifecycle Preconditions And Closeout

- PR #31 was closed without merge because its scope was incomplete.
- The current branch was reinitialized for issue #22 with the docs workflow.
- After documentation and ready checks pass, submit exactly one replacement PR.
- Do not merge the replacement PR without explicit human approval.

## Risks And Mitigations

| Risk | Mitigation |
|---|---|
| Antigravity and Codex procedures drift | Keep one canonical workflow body under `.agents/workflows/` |
| Router broadens role authority | Route only operations already owned by the role |
| Codex treats workflows as slash commands | Use “internal workflow reference” terminology |
| Startup semantics conflict with standalone research | Keep `/start` mapping in role startup contracts; do not route research through `start.md` |
| A second active PR is created accidentally | Verify PR #31 is closed before submitting one replacement PR |

## Related Documentation

- [Workspace instructions](../../../AGENTS.md)
- [Create issue workflow](../../../.agents/workflows/create-issue.md)
- [Start issue workflow](../../../.agents/workflows/start-issue.md)
- [End issue workflow](../../../.agents/workflows/end-issue.md)
- [Active phase workflow](../../../.agents/workflows/go.md)
- [Startup workflow](../../../.agents/workflows/start.md)
- [Coordination skill](../../../.agents/skills/pgmcp-co/SKILL.md)
- [Implementation skill](../../../.agents/skills/pgmcp-imp/SKILL.md)

---

## Version History

| Version | Date | Author | Changes |
|---|---|---|---|
| 1.0 | 2026-08-06 | Agent | Initial draft |
| 1.1 | 2026-08-06 | Agent | Add exact routing, target matrix, link validation, startup decision, and lifecycle closeout |
