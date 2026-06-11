# Technology Stack

**Analysis Date:** 2026-06-11

## Languages

**Primary:**
- Markdown - The main project surface is curriculum content in `README.md`, `docs/*.md`, `templates/*.md`, `.github/PULL_REQUEST_TEMPLATE.md`, and `sample-project/library-management/*.md`.

**Secondary:**
- Python 3 - Utility scripts in `scripts/render_term.py` and `scripts/verify_doc_links.py`.
- Shell snippets - Commands embedded throughout the tutorial modules, especially `docs/01-setup-environment.md`, `docs/02-install-agent-cli.md`, and `docs/03-install-gsd-core.md`.

## Runtime

**Environment:**
- No application runtime is required for the repository itself.
- Python 3 is required only for optional utility scripts.
- Node.js 20+, npm, git, and GitHub CLI are tutorial prerequisites documented for students in `docs/01-setup-environment.md`, but they are not used by a local app in this repo.

**Package Manager:**
- No repository-level package manager manifest is present. There is no `package.json`, `requirements.txt`, `pyproject.toml`, or lockfile.
- GSD Core is used externally through `npx @opengsd/gsd-core@latest`, documented in `README.md` and `docs/03-install-gsd-core.md`.

## Frameworks

**Core:**
- None. This is a documentation/tutorial repository, not a web app, API, or CLI package.

**Testing:**
- No formal test framework is configured.
- `scripts/verify_doc_links.py` performs a custom link check for local markdown links in `docs/*.md`.

**Build/Dev:**
- `scripts/render_term.py` can generate terminal-style PNG screenshots from text input using CairoSVG.
- There is no static-site generator, bundler, or docs build pipeline configured in the repository.

## Key Dependencies

**Critical:**
- `cairosvg` - Python package imported by `scripts/render_term.py` to convert generated SVG into PNG screenshots.
- Python standard library modules `argparse`, `sys`, `textwrap`, `re`, and `pathlib` - Used by `scripts/render_term.py`.
- Python standard library modules `pathlib`, `re`, and `sys` - Used by `scripts/verify_doc_links.py`.

**Infrastructure:**
- GitHub repository conventions - `.github/PULL_REQUEST_TEMPLATE.md` defines PR review structure.
- GSD Core - External workflow framework taught by the curriculum and referenced as `open-gsd/gsd-core` / `@opengsd/gsd-core`.

## Configuration

**Environment:**
- The repository has no required environment variables.
- The tutorial instructs students to configure git identity and authenticate `gh` in `docs/01-setup-environment.md`.
- The tutorial documents optional agent authentication for Claude Code and Codex in `docs/02-install-agent-cli.md`.

**Build:**
- No build config files are present.
- `.gitignore` currently ignores only `node_modules/`.

## Platform Requirements

**Development:**
- Any platform that can edit markdown files.
- WSL/Ubuntu and macOS setup paths are documented in `docs/01-setup-environment.md`.
- Python 3 plus `cairosvg` is needed to regenerate terminal screenshots with `scripts/render_term.py`.

**Production:**
- No production deployment target exists for this repository.
- The content is intended to be read from GitHub or cloned locally as course material.

---
*Stack analysis: 2026-06-11*
*Update after adding a docs build system, package manifest, test framework, or application runtime*
