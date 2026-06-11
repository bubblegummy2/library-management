# Architecture

**Analysis Date:** 2026-06-11

## Pattern Overview

**Overall:** Documentation-first tutorial repository with small utility scripts

**Key Characteristics:**
- Course content is stored as ordered markdown modules in `docs/`.
- Root `README.md` acts as the course landing page and module index.
- Reusable student-facing templates live in `templates/`.
- `sample-project/library-management/` demonstrates the target GSD artifacts for a Library Management System.
- Python scripts support documentation maintenance and screenshot generation, but there is no runtime application.

## Layers

**Curriculum Layer:**
- Purpose: Teach specification-first information system development with agentic AI and GSD Core.
- Contains: `README.md` and `docs/00-mindset.md` through `docs/13-reviewing-ai-code.md`.
- Depends on: Screenshots in `assets/screenshots/`, templates in `templates/`, and external tools documented for students.
- Used by: Students and instructors reading the course.

**Template Layer:**
- Purpose: Provide starter documents students can copy or adapt.
- Contains: `templates/PROJECT_SPEC.md`, `templates/PRD.md`, and `templates/ROADMAP.md`.
- Depends on: The F-ID / NF-ID conventions explained in the tutorial.
- Used by: Course exercises and student project setup.

**Sample Project Layer:**
- Purpose: Show a concrete Library Management System specification and roadmap.
- Contains: `sample-project/library-management/PROJECT_SPEC.md`, `.planning/PROJECT.md`, and `.planning/ROADMAP.md`.
- Depends on: The same spec-first conventions taught in the modules.
- Used by: Examples and reference material for students.

**Utility Script Layer:**
- Purpose: Maintain or generate supporting documentation assets.
- Contains: `scripts/verify_doc_links.py` and `scripts/render_term.py`.
- Depends on: Python standard library and `cairosvg` for rendering.
- Used by: Maintainers when checking docs or creating screenshots.

**Repository Workflow Layer:**
- Purpose: Define contribution and review expectations.
- Contains: `.github/PULL_REQUEST_TEMPLATE.md`, `.gitignore`, and repository licensing.
- Depends on: GitHub pull request workflow.
- Used by: Contributors and reviewers.

## Data Flow

**Student Tutorial Flow:**
1. Student starts at `README.md`.
2. Student follows numbered modules in `docs/`.
3. Student installs tools and GSD Core using commands documented in `docs/01-setup-environment.md`, `docs/02-install-agent-cli.md`, and `docs/03-install-gsd-core.md`.
4. Student creates specifications using `templates/PROJECT_SPEC.md`, `templates/PRD.md`, and GSD commands described in later modules.
5. Student builds, verifies, ships, and reviews work following `docs/10-build-with-claude.md`, `docs/11-build-with-codex.md`, `docs/12-verify-and-ship.md`, and `docs/13-reviewing-ai-code.md`.

**Documentation Link Check Flow:**
1. Maintainer runs `python3 scripts/verify_doc_links.py`.
2. Script scans only `docs/*.md`.
3. It extracts markdown links with a regular expression.
4. It ignores `http://`, `https://`, and `#` anchor-only links.
5. It resolves local links relative to each doc file.
6. It prints `BROKEN: {md} -> {target}` for missing targets and exits `1` if any are found.

**Screenshot Render Flow:**
1. Maintainer runs `python3 scripts/render_term.py --output out.png --title "..."` with stdin or `--text`.
2. Script parses input text and basic ANSI sequences.
3. Script generates an SVG terminal window in memory.
4. CairoSVG converts the SVG to a PNG file.
5. Output is written to the requested path, creating parent directories as needed.

**State Management:**
- Course state is file-based and manual.
- There is no database, server state, background process, or generated state directory other than optional screenshots produced by `scripts/render_term.py`.

## Key Abstractions

**Module:**
- Purpose: One lesson in the ordered course.
- Examples: `docs/00-mindset.md`, `docs/04-new-project.md`, `docs/13-reviewing-ai-code.md`.
- Pattern: Number-prefixed markdown file with narrative instruction, commands, and next-step links.

**Template:**
- Purpose: Reusable student starter artifact.
- Examples: `templates/PROJECT_SPEC.md`, `templates/PRD.md`, `templates/ROADMAP.md`.
- Pattern: Markdown with bracketed placeholders and guidance comments.

**Sample GSD Artifact:**
- Purpose: Demonstrate expected project outputs.
- Examples: `sample-project/library-management/.planning/PROJECT.md`, `sample-project/library-management/.planning/ROADMAP.md`.
- Pattern: Structured markdown with F-ID / NF-ID references and phase mapping.

**Utility Script:**
- Purpose: One-off maintenance helper.
- Examples: `scripts/verify_doc_links.py`, `scripts/render_term.py`.
- Pattern: Executable Python script with a `main()` function or top-level script logic.

## Entry Points

**Course Entry:**
- Location: `README.md`.
- Triggers: User opens the repository on GitHub or locally.
- Responsibilities: Explain audience, principles, quick start, module order, and reference links.

**Module Entry Points:**
- Location: `docs/*.md`.
- Triggers: Student follows the tutorial sequence.
- Responsibilities: Teach one workflow step and link to the next module.

**Link Checker:**
- Location: `scripts/verify_doc_links.py`.
- Triggers: Manual command invocation.
- Responsibilities: Validate local links in `docs/*.md`.

**Screenshot Renderer:**
- Location: `scripts/render_term.py`.
- Triggers: Manual command invocation.
- Responsibilities: Render terminal-style PNG screenshots.

## Error Handling

**Strategy:** Simple fail-fast behavior in utility scripts.

**Patterns:**
- `scripts/verify_doc_links.py` accumulates link errors and exits with status `1` if any are found.
- `scripts/render_term.py` exits with status `1` if `cairosvg` cannot be imported.
- Tutorial docs repeatedly instruct students to stop and fix missing tools before proceeding.

## Cross-Cutting Concerns

**Documentation Consistency:**
- Numbered module filenames establish course order.
- Module links at the end of documents keep the path navigable.
- `README.md` mirrors the module sequence.

**Validation:**
- Local markdown link validation is available but only covers files matching `docs/*.md`.
- No automated validation exists for root README links, template placeholders, screenshots, or sample project consistency.

**Security:**
- No production code handles user data or secrets.
- `docs/02-install-agent-cli.md` shows `OPENAI_API_KEY="sk-..."` as an example placeholder; avoid replacing it with a real key.
- `docs/13-reviewing-ai-code.md` explicitly teaches students to review for hardcoded secrets.

---
*Architecture analysis: 2026-06-11*
*Update when adding a generated docs site, application code, CI, or new course artifact types*
