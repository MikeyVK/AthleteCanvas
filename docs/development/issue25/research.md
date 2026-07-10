<!-- c:\1Voudig\99_Programming\ypsia\docs\development\issue25\research.md -->
<!-- template=research version=8b7bb3ab created=2026-07-10T17:38Z updated= -->
# Standalone Research Sub-Agent

**Status:** APPROVED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-10

---

## Purpose

Establish a ruleset that equips the research agent to act as a deep technical investigation partner with workspace-level context.

## Scope

**In Scope:**
Defining rules in research.agent.md, read-only workspace exploration, web searching, standalone conversational format.

**Out of Scope:**
Code modifications, test executions, git commits, PR management, phase transitions, planning board operations.

---

## Problem Statement

The research sub-agent lacks a dedicated rule file in the repository defining its behavior, allowed tools, and workspace constraints, which prevents a consistent local-first interactive research experience.

## Research Goals

- Define a standalone @research agent that operates outside the phase-gate workflow.
- Formally define its scope, read-only permitted tools, and interaction protocols.
- Prevent workflow coupling or mandatory phase-gate hand-overs for this agent.

---

## Background

Currently, research is either handled by @co or @imp as part of the phase-gate workflow, or done via external chats that lack direct access to local repository context.

---

## Findings

1. **Standalone Research Agent**: A standalone main-chat `@research` agent can be defined in `.agents/rules/research.agent.md`. It will utilize only read-only tools and be workflow-agnostic, serving as a direct conversational partner for the user.
2. **IDE-Agnostic Improvements**: Active agent instruction files contain legacy references to specific IDEs (`VS Code` and `Google Antigravity`):
   - `AGENTS.md` references them in the auto-load settings (line 3) and chat session model (line 211).
   - Rules files (`co.agent.md`, `imp.agent.md`, `qa.agent.md`, `research.agent.md`) reference them in their frontmatter description blocks.
   - These references should be replaced with generic terms (e.g., "the IDE" or "agent orchestration") to achieve a clean, IDE-agnostic setup. No dedicated IDE-specific folders are required.
3. **Non-Destructive Tool Access**: To maximize effectiveness, the `@research` agent requires access to non-destructive, read-only `pgmcp` server tools (e.g., `get_issue`, `get_project_plan`, `git_diff_stat`, `git_status`) to fetch workspace, issue, and branch metadata.

---

## Approved Strategy

- Create a dedicated, standalone, workflow-independent, read-only research agent configuration (`.agents/rules/research.agent.md`) equipped with codebase, web search, and read-only `pgmcp` workflow and git tools.
- Remove IDE-specific references from `AGENTS.md` and the frontmatter of all agent rules files, replacing them with generic equivalents.

---

## Expected Results

A new research.agent.md file and updated AGENTS.md enabling the @research agent.

## Related Documentation
- **[.agents/rules/research.agent.md][related-1]**

<!-- Link definitions -->

[related-1]: .agents/rules/research.agent.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-10 | Agent | Initial draft |