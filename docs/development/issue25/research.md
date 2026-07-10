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

A standalone main-chat @research agent can be defined in .agents/rules/research.agent.md. It will utilize only read-only tools and be workflow-agnostic, serving as a direct conversational partner for the user.

---

## Approved Strategy

Create a dedicated, standalone, workflow-independent, read-only research agent configuration in the workspace.

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