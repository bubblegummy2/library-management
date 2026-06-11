# Coding Conventions

**Analysis Date:** 2026-06-11

## Naming Patterns

**Files:**
- Course modules use two-digit numeric prefixes plus kebab-case: `docs/01-setup-environment.md`, `docs/09-worktree-teamwork.md`.
- Root/template documents use uppercase descriptive names: `README.md`, `templates/PROJECT_SPEC.md`, `templates/ROADMAP.md`.
- Python utilities use snake_case: `scripts/render_term.py`, `scripts/verify_doc_links.py`.
- Screenshot filenames use numeric prefixes and kebab-case descriptions: `assets/screenshots/04-gsd-new-project.png`.

**Functions:**
- Python functions use snake_case, for example `escape_xml`, `ansi_to_spans`, `colorize_line`, `build_svg`, and `main` in `scripts/render_term.py`.
- `scripts/verify_doc_links.py` is top-level procedural code and does not define functions.

**Variables:**
- Python module constants in `scripts/render_term.py` use uppercase names such as `BG`, `CHROME`, `TEXT`, `FONT_SIZE`, and `ANSI_COLORS`.
- Local Python variables use snake_case such as `visible_lines`, `svg_lines`, `cur_color`, and `wrapped`.

**Types:**
- No custom classes, interfaces, or type aliases are present.

## Code Style

**Formatting:**
- Python scripts use 4-space indentation.
- `scripts/render_term.py` groups imports, constants, helper functions, and `main()` in a conventional script layout.
- Markdown documents use ATX headings (`#`, `##`, `###`) and fenced code blocks.
- Tables are used heavily for requirements, tools, roadmaps, and PR metadata.

**Linting:**
- No linter configuration is present.
- No formatter configuration is present.

## Import Organization

**Order:**
1. Python standard library imports.
2. Third-party imports inside guarded blocks when optional.

**Grouping:**
- `scripts/render_term.py` imports standard library modules first, then attempts to import `cairosvg` in a `try` block.
- `scripts/verify_doc_links.py` uses compact imports: `from pathlib import Path` followed by `import re, sys`.

**Path Aliases:**
- None.

## Error Handling

**Patterns:**
- `scripts/render_term.py` catches `ImportError` for `cairosvg`, prints an install hint to stderr, and exits `1`.
- `scripts/verify_doc_links.py` accumulates an error count and exits `1` when broken links exist.
- Tutorial docs use instructional guardrails, such as telling students to stop and fix missing tools before continuing.

**Error Types:**
- No custom error types.
- Expected script failures are represented by process exit codes.

## Logging

**Framework:**
- No logging framework.
- Scripts use `print()`.

**Patterns:**
- Success messages use a checkmark in both scripts, for example `✓ Written:` and `✓ All local links OK`.
- Errors are printed as plain text, with `scripts/render_term.py` writing the missing dependency message to stderr.

## Comments

**When to Comment:**
- `scripts/render_term.py` uses short section comments to separate palette, ANSI conversion, and terminal content generation.
- Markdown docs use blockquotes and comments where they help students distinguish instructions from placeholders.

**JSDoc/TSDoc:**
- Not applicable.

**TODO Comments:**
- No TODO comments were found in the scanned source.

## Function Design

**Size:**
- `scripts/render_term.py` has several focused helper functions and a `main()` entry point.
- `build_svg()` is the central rendering function and constructs SVG markup line by line.

**Parameters:**
- Python helpers accept simple scalar parameters such as `line`, `title`, `lines`, and `width`.
- `argparse` handles command-line options in `main()`.

**Return Values:**
- Helper functions return strings or lists for rendering.
- `main()` performs file output and prints status.

## Module Design

**Exports:**
- Scripts are intended for command-line execution, not import as libraries.
- `scripts/render_term.py` uses the standard `if __name__ == "__main__": main()` guard.

**Barrel Files:**
- None.

## Markdown Authoring Patterns

**Course Flow:**
- Modules start with a title and usually end with a next-module link.
- Modules include command blocks students can copy into a terminal or agent.
- The tone is instructional and direct, with repeated emphasis on spec-first discipline.

**Requirement IDs:**
- Templates and samples use `F01`, `F02`, etc. for functional requirements and `NF01`, `NF02`, etc. for non-functional requirements.
- PRs are expected to reference related F-IDs / NF-IDs in `.github/PULL_REQUEST_TEMPLATE.md`.

---
*Convention analysis: 2026-06-11*
*Update when linting, formatting, tests, or new language conventions are added*
