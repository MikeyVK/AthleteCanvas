<!-- docs\development\issue19\pr.md -->
<!-- template=pr version=93bb9b4e created=2026-07-09T10:41Z updated= -->
# docs: Bootstrap phase-gate-mcp and project documentation #19

This PR bootstraps the ypsia workspace's core documentation and coding standards using the latest phase-gate-mcp templates. It resolves the onboarding search puzzle by adding a central docs/README.md index, verplaatsing van CHARTER.md, and removes all obsolete reference directories and legacy branding.
## Changes
Removed legacy .st3/ and agent.md files, cleaned up docs/reference/mcp/, copied updated coding standards to docs/coding_standards/, relocated CHARTER.md to docs/CHARTER.md, generalized contracts.yaml, added docs/README.md onboarding entry point, and replaced AthleteCanvas and st3/s1mpletrader references with ypsia.

## Testing
Verified git status and file layouts. Successfully ran grep_search to prove zero legacy terminology matches (AthleteCanvas, st3, s1mpletrader) in tracked files. Ran run_quality_gates(scope='branch') successfully.
## Checklist

- [ ] All legacy folders (.st3, agent.md, docs/reference/mcp) deleted
- [ ] Coding standards copied to docs/coding_standards/
- [ ] CHARTER.md verplaatst naar docs/
- [ ] Old branding (st3, s1mpletrader, AthleteCanvas) refactored to ypsia
- [ ] docs/README.md onboarding index created
- [ ] contracts.yaml generalized and server restarted
- [ ] run_quality_gates passed successfully

## Related Documentation
- **[docs/development/issue19/planning.md][related-1]**
- **[docs/README.md][related-2]**
- **[docs/CHARTER.md][related-3]**
- **[docs/coding_standards/README.md][related-4]**

---

Closes: #19