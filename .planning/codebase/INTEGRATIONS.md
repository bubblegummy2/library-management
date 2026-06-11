# External Integrations

**Analysis Date:** 2026-06-11

## APIs & External Services

**GSD Core:**
- `open-gsd/gsd-core` - External framework used throughout the tutorial.
  - Package: `@opengsd/gsd-core` via npm / `npx`.
  - References: `README.md`, `docs/03-install-gsd-core.md`, `docs/04-new-project.md`, `docs/05-discuss-phase.md`, `docs/06-plan-phase.md`, `docs/12-verify-and-ship.md`.
  - Commands taught: `/gsd-new-project`, `/gsd-discuss-phase`, `/gsd-plan-phase`, `/gsd-execute-phase`, `/gsd-verify-work`, `/gsd-ship`; Codex spelling is documented as `$gsd-*` in `docs/02-install-agent-cli.md`.

**AI Coding Agents:**
- Claude Code - Agent path documented in `README.md`, `docs/02-install-agent-cli.md`, and `docs/10-build-with-claude.md`.
  - Install command: `npm install -g @anthropic-ai/claude-code`.
  - Auth: browser OAuth or API key depending on the user plan.
- Codex - Agent path documented in `README.md`, `docs/02-install-agent-cli.md`, and `docs/11-build-with-codex.md`.
  - Install command: `npm install -g @openai/codex`.
  - Auth: OpenAI account login or `OPENAI_API_KEY`.

**Developer Tooling:**
- Git - Required for version control and worktree exercises.
- GitHub CLI (`gh`) - Required for repo, PR, and review workflows.
- Node.js / npm - Required to install agent CLIs and run GSD Core installer through `npx`.

## Data Storage

**Databases:**
- None for this repository.
- The sample project in `sample-project/library-management/PROJECT_SPEC.md` proposes PostgreSQL for a hypothetical Library Management System, but it is not implemented here.

**File Storage:**
- Repository files are plain markdown, images, and Python scripts.
- Screenshots live in `assets/screenshots/*.png`.

**Caching:**
- None.

## Authentication & Identity

**Auth Provider:**
- None in this repository.
- Tutorial modules instruct users to authenticate external tools:
  - `gh auth login` in `docs/01-setup-environment.md`.
  - Claude Code authentication in `docs/02-install-agent-cli.md`.
  - Codex authentication / `OPENAI_API_KEY` in `docs/02-install-agent-cli.md`.

**OAuth Integrations:**
- GitHub browser login through `gh auth login` is documented for students.
- Claude Code and Codex may use browser login flows, depending on account setup.

## Monitoring & Observability

**Error Tracking:**
- None.

**Analytics:**
- None.

**Logs:**
- Utility scripts print to stdout/stderr:
  - `scripts/verify_doc_links.py` prints broken links and exits non-zero when errors exist.
  - `scripts/render_term.py` prints conversion errors and output file status.

## CI/CD & Deployment

**Hosting:**
- No deployment target is configured.
- GitHub is the implied hosting surface for the tutorial repository and pull request workflow.

**CI Pipeline:**
- No GitHub Actions workflows are present under `.github/workflows/`.
- `.github/PULL_REQUEST_TEMPLATE.md` defines manual PR review expectations.

## Environment Configuration

**Development:**
- Required local tools for students are documented, not enforced: git, Node.js, npm, GitHub CLI, and at least one agent CLI.
- `scripts/render_term.py` requires the `cairosvg` Python package but no requirements file pins it.

**Staging:**
- None.

**Production:**
- None.

## Webhooks & Callbacks

**Incoming:**
- None.

**Outgoing:**
- None.

---
*Integration audit: 2026-06-11*
*Update when adding CI, package dependencies, hosted docs, external APIs, or automation tokens*
