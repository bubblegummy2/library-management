<!-- GSD:project-start source:PROJECT.md -->

## Project

**Library Management System**

A web application for a university library that helps staff manage the book catalog, members, borrowing, returns, overdue loans, and daily operational statistics. The primary users are librarians and administrators who need a clean, simple interface they can use every day.

The system will be built with Next.js 14 App Router, TypeScript, Prisma ORM, SQLite, and Tailwind CSS.

**Core Value:** Librarians can reliably track which books are available, who has borrowed them, and which loans are overdue.

### Constraints

- **Tech stack**: Next.js 14 App Router, TypeScript, Prisma ORM, SQLite, and Tailwind CSS - chosen by project requirement.
- **Database**: SQLite - suitable for a local/simple deployment, but future multi-user production deployment may require revisiting database choice.
- **Access model**: Admin plus librarian roles - v1 needs role-based access but no student-facing account system.
- **Inventory model**: Quantity count per book - simpler than per-copy tracking and aligned with v1 scope.
- **UI style**: Clean and simple - optimized for repeated librarian use rather than marketing presentation.

<!-- GSD:project-end -->

<!-- GSD:stack-start source:research/STACK.md -->

## Technology Stack

## Recommended Stack Shape

- **Framework:** Next.js 14 App Router with TypeScript.
- **Data access:** Prisma ORM with SQLite for v1.
- **Styling:** Tailwind CSS with a restrained, staff-facing dashboard layout.
- **Mutation path:** Server Actions for form-driven create/update/delete workflows.
- **Authorization path:** Centralized data access layer (DAL) that verifies session and role before reads or mutations.

## Findings

### Next.js App Router

- Server Components for data-heavy list/detail pages.
- Server Actions for form submissions and mutations.
- `revalidatePath` after mutations that affect dashboard counts, catalog lists, member lists, or loan lists.
- Route Handlers only where an explicit API endpoint is needed.

### Authentication And Authorization

- Use a `verifySession()` or equivalent DAL function.
- Store staff users with roles: `ADMIN`, `LIBRARIAN`.
- Gate admin-only actions separately from librarian daily operations.
- Do not rely only on hidden UI controls for authorization.
- Avoid returning password hashes or internal fields to client components.

### Prisma With Next.js

- Put Prisma client setup in a single module, for example `src/lib/prisma.ts`.
- Keep database operations behind domain-level server functions or DAL functions.
- Model relations explicitly: books, members, loans, and staff users.

### SQLite

- https://www.prisma.io/docs/orm/reference/supported-databases
- https://www.prisma.io/docs/orm/reference/prisma-schema-reference

## Stack Decision

<!-- GSD:stack-end -->

<!-- GSD:conventions-start source:CONVENTIONS.md -->

## Conventions

Conventions not yet established. Will populate as patterns emerge during development.
<!-- GSD:conventions-end -->

<!-- GSD:architecture-start source:ARCHITECTURE.md -->

## Architecture

Architecture not yet mapped. Follow existing patterns found in the codebase.
<!-- GSD:architecture-end -->

<!-- GSD:skills-start source:skills/ -->

## Project Skills

No project skills found. Add skills to any of: `.claude/skills/`, `.agents/skills/`, `.cursor/skills/`, `.github/skills/`, or `.codex/skills/` with a `SKILL.md` index file.
<!-- GSD:skills-end -->

<!-- GSD:workflow-start source:GSD defaults -->

## GSD Workflow Enforcement

Before using Edit, Write, or other file-changing tools, start work through a GSD command so planning artifacts and execution context stay in sync.

Use these entry points:

- `/gsd-quick` for small fixes, doc updates, and ad-hoc tasks
- `/gsd-debug` for investigation and bug fixing
- `/gsd-execute-phase` for planned phase work

Do not make direct repo edits outside a GSD workflow unless the user explicitly asks to bypass it.
<!-- GSD:workflow-end -->

<!-- GSD:profile-start -->

## Developer Profile

> Profile not yet configured. Run `/gsd-profile-user` to generate your developer profile.
> This section is managed by `generate-claude-profile` -- do not edit manually.
<!-- GSD:profile-end -->
