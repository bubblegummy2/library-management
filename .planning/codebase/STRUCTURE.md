# Codebase Structure

**Analysis Date:** 2026-06-11

## Directory Layout

```
isd-project-main/
├── .github/                 # GitHub pull request template
├── assets/                  # Tutorial screenshots and visual assets
│   └── screenshots/         # Numbered PNG screenshots used by docs
├── docs/                    # Ordered course modules
├── sample-project/          # Example project artifacts for the course
│   └── library-management/  # Library Management System sample
├── scripts/                 # Python documentation utilities
├── templates/               # Student-facing spec and roadmap templates
├── .gitignore               # Ignore rules
├── LICENSE                  # Repository license
└── README.md                # Course overview and module index
```

## Directory Purposes

**`.github/`:**
- Purpose: GitHub collaboration metadata.
- Contains: Pull request template.
- Key files: `.github/PULL_REQUEST_TEMPLATE.md`.
- Subdirectories: No `.github/workflows/` directory is present.

**`assets/screenshots/`:**
- Purpose: Images embedded in tutorial modules.
- Contains: Numbered PNG screenshots such as `01-tool-versions.png`, `04-gsd-new-project.png`, and `10-pr-review.png`.
- Key files: Screenshot names align with module or workflow order.
- Subdirectories: None.

**`docs/`:**
- Purpose: Main curriculum content.
- Contains: Ordered markdown modules from `00-mindset.md` through `13-reviewing-ai-code.md`.
- Key files: `docs/00-mindset.md` introduces the spec-first philosophy; `docs/03-install-gsd-core.md` explains installation; `docs/12-verify-and-ship.md` and `docs/13-reviewing-ai-code.md` cover quality gates.
- Subdirectories: None.

**`templates/`:**
- Purpose: Copyable project planning templates.
- Contains: `PRD.md`, `PROJECT_SPEC.md`, and `ROADMAP.md`.
- Key files: `templates/PROJECT_SPEC.md` defines F-ID / NF-ID conventions used by the tutorial.
- Subdirectories: None.

**`sample-project/library-management/`:**
- Purpose: Concrete example of the course target project.
- Contains: A human-written brief and structured GSD planning outputs.
- Key files: `sample-project/library-management/PROJECT_SPEC.md`, `sample-project/library-management/.planning/PROJECT.md`, `sample-project/library-management/.planning/ROADMAP.md`.
- Subdirectories: `.planning/` contains example planning artifacts.

**`scripts/`:**
- Purpose: Small maintenance utilities.
- Contains: Python executable scripts.
- Key files: `scripts/verify_doc_links.py`, `scripts/render_term.py`.
- Subdirectories: None.

## Key File Locations

**Entry Points:**
- `README.md`: Repository landing page and course index.
- `docs/00-mindset.md`: First lesson in the course.

**Configuration:**
- `.gitignore`: Currently ignores `node_modules/`.
- `.github/PULL_REQUEST_TEMPLATE.md`: Defines manual PR summary, related requirements, test plan, and screenshots sections.

**Core Logic:**
- `scripts/verify_doc_links.py`: Local markdown link checker for `docs/*.md`.
- `scripts/render_term.py`: Terminal screenshot renderer.

**Testing:**
- No `tests/` directory is present.
- `scripts/verify_doc_links.py` is the closest available verification utility.

**Documentation:**
- `README.md`: Course overview.
- `docs/*.md`: Lesson content.
- `templates/*.md`: Planning artifact templates.
- `sample-project/library-management/*.md`: Example project documents.

## Naming Conventions

**Files:**
- Number-prefixed kebab-case for course modules: `00-mindset.md`, `01-setup-environment.md`, `13-reviewing-ai-code.md`.
- Uppercase markdown for repository-level and template artifacts: `README.md`, `LICENSE`, `PROJECT_SPEC.md`, `PRD.md`, `ROADMAP.md`.
- Snake_case for Python scripts: `render_term.py`, `verify_doc_links.py`.
- Number-prefixed screenshots: `01-tool-versions.png`, `05-gsd-verify.png`, `10-pr-review.png`.

**Directories:**
- Lowercase plural names for collections: `docs/`, `assets/`, `scripts/`, `templates/`.
- Kebab-case for sample project directories: `sample-project/`, `library-management/`.

**Special Patterns:**
- F-ID / NF-ID requirement identifiers appear in `templates/PROJECT_SPEC.md`, `templates/PRD.md`, `.github/PULL_REQUEST_TEMPLATE.md`, and sample project artifacts.
- GSD planning artifacts are represented under `.planning/` in `sample-project/library-management/`.

## Where to Add New Code

**New Tutorial Module:**
- Primary content: `docs/{number}-{topic}.md`.
- Assets: `assets/screenshots/{number}-{topic}.png` if the module needs screenshots.
- Index updates: `README.md` table of contents and tutorial module list.

**New Student Template:**
- Implementation: `templates/{TEMPLATE_NAME}.md`.
- Documentation: Mention it from the relevant `docs/*.md` module and `README.md` if it becomes part of the standard workflow.

**New Documentation Utility:**
- Implementation: `scripts/{utility_name}.py`.
- Dependencies: Add a dependency manifest if non-stdlib packages are required.
- Documentation: Mention usage in README or a maintenance note if intended for contributors.

**New Sample Project Artifact:**
- Implementation: `sample-project/{project-name}/`.
- Planning docs: Store example GSD outputs under `sample-project/{project-name}/.planning/`.
- Keep requirement IDs and roadmap phase mappings consistent.

## Special Directories

**`.planning/`:**
- Purpose: GSD planning artifacts for this repository. Created by the mapping workflow.
- Source: Generated planning context.
- Committed: Intended to be tracked when git is functional and planning docs are configured for commits.

**`sample-project/library-management/.planning/`:**
- Purpose: Example GSD planning output for the sample Library Management System.
- Source: Course sample content.
- Committed: Yes, as instructional material.

**`.git/`:**
- Purpose: Git metadata.
- Current state: A previous `git init` attempt failed while creating `.git/hooks/`, leaving an empty `.git` directory in this workspace.
- Caution: Git commands may fail until the filesystem issue is resolved.

---
*Structure analysis: 2026-06-11*
*Update when directory structure changes*
