<!-- docs\development\issue19\planning.md -->
<!-- template=planning version=130ac5ea created=2026-07-09T10:06Z updated= -->
# Bootstrap phase-gate-mcp and project documentation

**Status:** DRAFT  
**Version:** 1.0  
**Last Updated:** 2026-07-09

---

## Purpose

Bootstrapping ypsia workspace coding standards, aligning documents, and cleaning up legacy terminology.

## Scope

**In Scope:**
docs/coding_standards/, docs/CHARTER.md, .gitignore, deleting .st3/ and agent.md.

**Out of Scope:**
mcp server setup, manuals, or reference docs (these remain in .pgmcp/docs/). No python test files or test code will be created or committed.

## Prerequisites

Read these first:
1. Active branch is feature/19-bootstrap-pgmcp
2. Research phase is completed
---

## Summary

Deploys ypsia coding standards, cleans up legacy st3 and AthleteCanvas terminology, and verifies setup. Note: This is a pure documentation task; no test code files or test suites will be created or committed.

---

## TDD Cycles


### Cycle 1: Cleanup Legacy Folders & Obsolete Files

**Goal:** Delete the .st3/ directory, agent.md in the root, and the docs/reference/mcp/ directory from the workspace.

**Tests:**
- Run git status to verify .st3/ and agent.md are deleted (no test files created)
- Check docs/reference/mcp/ is removed from workspace (no test files created)

**Success Criteria:**
Clean workspace without legacy/obsolete directories and files, preventing accidental editing.



### Cycle 2: Deploy Coding Standards & Relocate Charter

**Goal:** Copy standards from .pgmcp/docs/coding_standards/ to docs/coding_standards/ and move docs/development/CHARTER.md to docs/CHARTER.md.

**Tests:**
- Check docs/coding_standards/ exists and contains updated files (no test files created)
- Check docs/CHARTER.md exists in root (no test files created)

**Success Criteria:**
All files successfully copied and relocated to their target destinations.



### Cycle 3: Terminology Refactor

**Goal:** Scan the entire workspace and replace all references to st3, s1mpletrader, and AthleteCanvas with ypsia (or corresponding paths).

**Tests:**
- Run grep_search tool for st3, s1mpletrader, athletecanvas and verify zero matches in tracked files (excluding package-lock integrity check) (no test files created)
- Check all templates have ypsia and .pgmcp paths (no test files created)

**Success Criteria:**
All legacy names and paths fully replaced and updated in the codebase.



### Cycle 4: Update Root Configurations & Links

**Goal:** Align .gitignore, AGENTS.md, and references within agent configs (like rules and workflows).

**Tests:**
- Review git diff of .gitignore and AGENTS.md (no test files created)
- Execute run_quality_gates tool to verify code styling and standards compliance (no test files created)

**Success Criteria:**
Configurations and rule files successfully updated and compliant.


---

## Risks & Mitigation

- **Risk:** Accidentally breaking links to architecture principles or quality gates in rules/AGENTS.md
  - **Mitigation:** Verify all relative link paths point to docs/coding_standards/ after copy.

---

## Milestones

- Planning approved
- Cleanup completed
- Coding standards deployed
- Terminology refactored
- QA validation passed

## Related Documentation
- **[docs/coding_standards/DOCUMENTATION_STANDARD.md][related-1]**
- **[docs/coding_standards/ARCHITECTURE_PRINCIPLES.md][related-2]**

<!-- Link definitions -->

[related-1]: docs/coding_standards/DOCUMENTATION_STANDARD.md
[related-2]: docs/coding_standards/ARCHITECTURE_PRINCIPLES.md

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-09 | Agent | Initial draft |