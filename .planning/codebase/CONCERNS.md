# Codebase Concerns

**Analysis Date:** 2026-06-11

## Tech Debt

**No dependency manifest for Python utility scripts:**
- Issue: `scripts/render_term.py` requires `cairosvg`, but there is no `requirements.txt`, `pyproject.toml`, or setup documentation for script dependencies.
- Files: `scripts/render_term.py`.
- Why: The repository is primarily tutorial content, and scripts appear to be maintainer utilities.
- Impact: A maintainer trying to regenerate screenshots can hit `ERROR: cairosvg not installed` without a documented setup command beyond the inline message.
- Fix approach: Add `requirements.txt` or a short maintenance section documenting `pip install cairosvg`.

**Link checker covers only `docs/*.md`:**
- Issue: `scripts/verify_doc_links.py` ignores links in `README.md`, `templates/*.md`, `.github/PULL_REQUEST_TEMPLATE.md`, and sample project markdown.
- Files: `scripts/verify_doc_links.py`, `README.md`, `templates/*.md`, `sample-project/library-management/*.md`.
- Why: Initial script scope is intentionally small.
- Impact: Broken links outside `docs/` can slip through.
- Fix approach: Expand the script to scan all relevant markdown files or accept path globs as CLI arguments.

**Git repository state is currently broken in this workspace:**
- Issue: A `git init` attempt failed at `.git/hooks/` with `Read-only file system`, leaving an empty `.git` directory.
- Files: `.git/`.
- Why: Filesystem permission or mount behavior in this environment.
- Impact: GSD commit steps and normal git status/commit operations may fail until repaired.
- Fix approach: Recreate the repository on a filesystem that permits `.git/hooks/`, or remove the broken `.git` directory only after confirming it is not a real repository that needs preservation.

## Known Bugs

**Potential false positives/limitations in markdown link parsing:**
- Symptoms: Regex-based parsing can mishandle unusual markdown links with nested parentheses, reference-style links, or image syntax edge cases.
- Trigger: Complex markdown link formats in `docs/*.md`.
- File: `scripts/verify_doc_links.py`.
- Workaround: Keep links simple or manually inspect complex links.
- Root cause: The script uses a simple regular expression instead of a markdown parser.

**Screenshot renderer dependency failure is runtime-only:**
- Symptoms: `scripts/render_term.py` exits if `cairosvg` is missing.
- Trigger: Running the script in a fresh Python environment.
- File: `scripts/render_term.py`.
- Workaround: Install `cairosvg` manually.
- Root cause: No project-level dependency setup.

## Security Considerations

**API key placeholder in tutorial docs:**
- Risk: `docs/02-install-agent-cli.md` shows an `OPENAI_API_KEY="sk-..."` example. A contributor could accidentally replace the placeholder with a real key in docs or screenshots.
- Current mitigation: The shown value is a placeholder.
- Recommendations: Keep examples clearly fake, and scan docs/screenshots before publishing.

**No secret scan automation:**
- Risk: Tutorial repos often collect screenshots and copied terminal output; accidental tokens can be committed in markdown or PNG assets.
- Current mitigation: Human review through `.github/PULL_REQUEST_TEMPLATE.md`.
- Recommendations: Add a lightweight secret scan in CI if the repo will receive student or public contributions.

## Performance Bottlenecks

**Link checker is simple but non-incremental:**
- Problem: It scans all `docs/*.md` every run.
- Measurement: Current repository size is small, so this is not a practical bottleneck.
- Cause: Simplicity.
- Improvement path: No action needed unless docs grow substantially.

**Screenshot renderer processes only first 50 visible lines:**
- Problem: Long terminal samples are truncated to 50 lines.
- Measurement: Hard-coded in `scripts/render_term.py` as `visible_lines = lines[:50]`.
- Cause: Designed for screenshot-sized outputs.
- Improvement path: Add a CLI option for max visible lines if longer screenshots are needed.

## Fragile Areas

**Course module sequencing:**
- Why fragile: `README.md`, numbered `docs/*.md` files, screenshot names, and next-module links all encode ordering manually.
- Common failures: Adding, removing, or renumbering modules can leave stale links or mismatched screenshots.
- Safe modification: Update `README.md`, next/previous links, and screenshots together; run `scripts/verify_doc_links.py`.
- Test coverage: Only local links in `docs/*.md` are checked.

**F-ID / NF-ID consistency across samples and templates:**
- Why fragile: Requirement IDs appear in templates, sample specs, sample roadmap, and PR template guidance.
- Common failures: A roadmap references an ID that no longer exists, or a PR template asks for a convention not used by current templates.
- Safe modification: Check `templates/PROJECT_SPEC.md`, `templates/PRD.md`, `templates/ROADMAP.md`, and `sample-project/library-management/.planning/ROADMAP.md` together.
- Test coverage: No automated consistency check.

**Generated screenshots:**
- Why fragile: Screenshots are binary files and can drift from current command examples.
- Common failures: Docs describe current commands while images show older output.
- Safe modification: Regenerate screenshots with `scripts/render_term.py` or manually verify visual consistency.
- Test coverage: None.

## Scaling Limits

**No docs build system:**
- Current capacity: Works well as a small GitHub-rendered tutorial.
- Limit: As the course grows, manual navigation and consistency checks become harder.
- Symptoms at limit: Broken cross-links, duplicated explanations, outdated screenshots, and hard-to-find modules.
- Scaling path: Add a docs site generator or stronger markdown validation if the curriculum expands.

## Dependencies at Risk

**CairoSVG:**
- Risk: Unpinned dependency for screenshot rendering.
- Impact: Future CairoSVG changes could alter rendering output or install behavior.
- Migration plan: Pin in `requirements.txt` if screenshot generation becomes part of normal maintenance.

**External GSD Core command names:**
- Risk: The tutorial documents GSD Core commands and behavior that may evolve upstream.
- Impact: Students may follow stale instructions if `@opengsd/gsd-core` changes.
- Migration plan: Periodically verify modules against the current GSD Core release.

## Missing Critical Features

**Automated documentation validation:**
- Problem: No CI runs link checks, secret scans, markdown lint, or sample consistency checks.
- Current workaround: Manual review.
- Blocks: Reliable public contribution workflow.
- Implementation complexity: Low to medium.

**Contributor maintenance guide:**
- Problem: There is no dedicated guide explaining how to regenerate screenshots, run checks, or update module ordering.
- Current workaround: Infer from scripts and docs.
- Blocks: Smooth handoff to additional maintainers.
- Implementation complexity: Low.

## Test Coverage Gaps

**Utility scripts are untested:**
- What's not tested: ANSI parsing, SVG generation, link extraction, and broken-link exit behavior.
- Risk: Script changes can silently break screenshot generation or link checking.
- Priority: Medium.
- Difficulty to test: Low after refactoring `scripts/verify_doc_links.py` into functions.

**Course examples are not consistency-checked:**
- What's not tested: F-ID / NF-ID alignment between sample project spec and roadmap.
- Risk: Students may learn from inconsistent examples.
- Priority: Medium.
- Difficulty to test: Low to medium with a small markdown table parser.

---
*Concerns audit: 2026-06-11*
*Update as issues are fixed or new ones discovered*
