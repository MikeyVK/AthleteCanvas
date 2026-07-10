<!-- docs\development\issue23\research.md -->
<!-- template=research version=8b7bb3ab created=2026-07-10T15:09Z updated= -->
# Research: label sync & refresh role slash-command

**Status:** DEFINITIVE  
**Version:** 1.0  
**Last Updated:** 2026-07-10

---

## Purpose

Document findings on repository label status, workflow structures, and design a lightweight chore workflow and role-refresh mechanism.

## Scope

**In Scope:**
labels.yaml configuration updates, new slash commands under .agents/workflows/, registration of chore workflow in pgmcp config files.

**Out of Scope:**
Changes to python backend code, frontend UI interfaces, or test fixtures (this is a pure tooling/configuration issue).

---

## Problem Statement

Discrepancy between local labels configuration (labels.yaml) and remote GitHub labels. Lack of an automated refresh mechanism for mid-session agent context, sub-role, and AGENTS.md instruction synchronization. Orchestration overhead for simple housekeeping/chore tasks due to the lack of a lightweight workflow.

## Research Goals

- Compare local labels.yaml with remote repository labels and align them
- Design a new custom start/refresh workflow to synchronize agent rules mid-session
- Design a new lightweight chore workflow to reduce orchestration overhead

---

## Background

The pgmcp server provides github label management tools and parses slash commands from .agents/workflows/*.md. The workflows and phases are configured via workflows.yaml and contracts.yaml in the server configuration.

---

## Findings

### GitHub Labels Mismatch Analysis
GitHub labels currently use default grey colors and lack descriptions for ypsia scope. The following table highlights the mismatches between the old labels.yaml (designed for pgmcp server development) and Ypsia's actual repository needs:

| Label Category | Old YAML Config | Remote GitHub (Ypsia-focused) | Rationale / Resolution |
| :--- | :--- | :--- | :--- |
| **type:\*** | feature, bug, refactor, docs, research, epic, chore | type:feature, type:bug, type:refactor, type:docs, type:research, type:epic, type:chore | Keep as-is; categories match. |
| **priority:\*** | critical, high, medium, low, triage | priority:critical, priority:high, priority:medium, priority:low, priority:triage | Update `priority:high` and `priority:medium` color/descriptions on remote to match YAML colors (D93F0B, FBCA04). |
| **scope:\*** | architecture, mcp-server, platform, tooling, workflow, documentation | scope:ai, scope:backend, scope:data, scope:frontend, scope:infrastructure, scope:nutrition, scope:planning, scope:tooling, scope:documentation | **Remove** old server scopes (`mcp-server`, `platform`, `workflow`). **Add** Ypsia-specific scopes to `labels.yaml` with soft-blue colors (`BFD4F2`) and clear descriptions, then sync to GitHub. |

### Slash Command Workflows
Workflows are parsed from `.agents/workflows/*.md`. The new `/start` workflow will enforce that the agent reads `AGENTS.md` and their respective `@` sub-role configuration file (`.agents/rules/<role>.agent.md`), outputting a formal confirmation.
A new `chore` workflow registered in `workflows.yaml` and `contracts.yaml` with the path `planning -> implementation -> ready` will reduce phases from 7 to 3, with `implementation` phase configured as `cycle_based: false` to avoid TDD loops for minor housekeeping tasks.

---

## Approved Strategy

Preserve compatibility. Update labels.yaml to align with Ypsia scopes, using rich colors (BFD4F2) and descriptions. Add /start workflow in .agents/workflows/start.md. Add chore workflow in workflows.yaml and contracts.yaml.

---

## Expected Results

Synchronized GitHub labels matching labels.yaml. Functional /start slash command that outputs role confirmation. Functional chore workflow with planning -> implementation -> ready phases.

## Related Documentation
- **[docs/README.md][related-1]**
- **[docs/coding_standards/README.md][related-2]**

<!-- Link definitions -->

[related-1]: docs/README.md
[related-2]: docs/coding_standards/README.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-10 | Agent | Initial draft |