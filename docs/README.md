<!-- docs/README.md -->
<!-- template=generic_doc version=43c84181 created=2026-07-09T10:39Z updated=2026-07-09T12:47Z -->
# Ypsia Documentation Index

**Status:** DEFINITIVE  
**Version:** 1.1  
**Last Updated:** 2026-07-09

---

## Purpose

Provide a centralized entry point for developer onboarding, project charter, and coding standards of the ypsia platform.

---

## Summary

Central index linking to the project charter, coding standards, and codebase directories to resolve onboarding search puzzles.

---

## Codebase Structure

This repository is organized as follows:
* **[docs/](.)**: Central documentation root.
  * **[CHARTER.md](CHARTER.md)**: Grondwet van Ypsia (Founding Charter), detailing the core mission, roadmap, stack, and design guidelines.
  * **[coding_standards/](coding_standards/)**: Directory containing coding standards and guidelines:
    * **[ARCHITECTURE_PRINCIPLES.md](coding_standards/ARCHITECTURE_PRINCIPLES.md)**: System design and architecture rules.
    * **[QUALITY_GATES.md](coding_standards/QUALITY_GATES.md)**: Pre-merge quality gates checklist.
    * **[DOCUMENTATION_STANDARD.md](coding_standards/DOCUMENTATION_STANDARD.md)**: Rules for writing documentation.
* **[backend/](../backend/)**: Backend application code (Python/FastAPI).
* **[frontend/](../frontend/)**: Frontend single-page application (React/Vite).
* **[web/](../web/)**: Static marketing/info site.
* **[.agents/](../.agents/)**: Agent instructions and workflow configuration files.

---

## Onboarding & Getting Started

1. **Orientation**: Read the **[Grondwet van Ypsia (CHARTER.md)](CHARTER.md)** first to align on the project's vision and core goals.
2. **Coding Standards**: Read the **[ARCHITECTURE_PRINCIPLES.md](coding_standards/ARCHITECTURE_PRINCIPLES.md)** before writing any code.
3. **Setup instructions**: Refer to the platform setup guidelines under **[.pgmcp/docs/setup/README.md](../.pgmcp/docs/setup/README.md)** for environment configuration and server startup.

---

## Related Documentation
- **[planning.md](development/issue19/planning.md)**
- **[CHARTER.md](CHARTER.md)**
- **[coding_standards/README.md](coding_standards/README.md)**

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-07-09 | Agent | Initial draft |
| 1.1 | 2026-07-09 | Agent | Fixed absolute links to clean relative links |
