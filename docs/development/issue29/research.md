<!-- c:\1Voudig\99_Programming\ypsia\docs\development\issue29\research.md -->
<!-- template=research version=8b7bb3ab created=2026-07-10T18:46Z updated= -->
# Allow Research Agent to Write Brain Artifacts and Issue Docs

**Status:** APPROVED  
**Version:** 1.0.0  
**Last Updated:** 2026-07-10

---

## Purpose

Update research agent guidelines to remove constraints on writing research and planning documentation, while maintaining strict code read-only boundaries.

## Scope

**In Scope:**
Updating rules in research.agent.md, allowing write_to_file for brain artifacts, allowing safe_edit_file and scaffold_artifact for docs/development/issueXX/ directory.

**Out of Scope:**
Modifying production code, tests, general documentation, configuration files outside issue directories.

---

## Problem Statement

The @research agent is currently strictly read-only, preventing it from writing its findings to the Antigravity brain (as persistent artifacts) or to the repository under the active docs/development/issueXX/ directory.

## Research Goals

- Permit the @research agent to create and update brain artifacts in the Antigravity brain directory.
- Permit the @research agent to scaffold and edit documentation artifacts under the active issue's directory in the repository.
- Ensure production code and tests remain strictly read-only and out of bounds.

---

## Background

Currently, the @research agent is strictly read-only, which forces the user to manually copy-paste findings or recreate them in the repository or brain, leading to context compaction and friction.

---

## Findings

The ruleset in research.agent.md can be updated to permit write_to_file for brain artifacts and safe_edit_file/scaffold_artifact for docs/development/issueXX/, while keeping production code and tests strictly read-only.

---

## Approved Strategy

Allow the @research agent to write brain artifacts (via write_to_file) and issue-specific documentation under docs/development/issueXX/ (via safe_edit_file and scaffold_artifact).

---

## Expected Results

An updated research.agent.md file permitting brain artifact and issue documentation edits.

## Related Documentation
- **[.agents/rules/research.agent.md][related-1]**

<!-- Link definitions -->

[related-1]: .agents/rules/research.agent.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2026-07-10 | Agent | Initial draft |