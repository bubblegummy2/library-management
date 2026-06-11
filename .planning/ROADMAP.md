# Roadmap: Library Management System (LMS) for Universitas XYZ

**Created:** 2026-06-11
**Project Mode:** mvp
**Source:** `.planning/PROJECT.md` and reference roadmap from `sample-project/library-management/.planning/ROADMAP.md`

## Milestone Overview

| Phase | Name | Goal | Requirements |
|-------|------|------|--------------|
| 1 | Foundation | Establish the secure full-stack base, database schema, and role-aware authentication. | FND-01, FND-02, FND-03, AUTH-01, AUTH-02, AUTH-03, AUTH-04, AUTH-05 |
| 2 | Book Catalog | Let students find books and admins manage catalog records. | CAT-01, CAT-02, CAT-03, CAT-04, CAT-05, CAT-06, CAT-07, CAT-08 |
| 3 | Borrowing System | Enable the full lending lifecycle from request through return and overdue handling. | LOAN-01, LOAN-02, LOAN-03, LOAN-04, LOAN-05, LOAN-06, LOAN-07, LOAN-08, LOAN-09 |
| 4 | Librarian Dashboard & Polish | Deliver operational monitoring, responsive UI, deployment readiness, and maintainability handoff. | DASH-01, DASH-02, DASH-03, DASH-04, UX-01, UX-02, UX-03, OPS-01, OPS-02, OPS-03 |

## Phase Details

### Phase 1: Foundation

**Goal:** Establish the secure full-stack base, database schema, and role-aware authentication.
**Mode:** mvp
**Requirements:** FND-01, FND-02, FND-03, AUTH-01, AUTH-02, AUTH-03, AUTH-04, AUTH-05
**UI hint:** yes

**Deliverables:**
- Dockerized FastAPI, React, and PostgreSQL project scaffold.
- Database schema for users, roles, books, inventory state, borrow requests, loans, returns, and history.
- Secure login flow with hashed passwords and JWT access tokens.
- Role separation for admin and student users.
- Protected backend route pattern for later phases.

**Success Criteria:**
1. `docker compose up` brings backend, frontend, and database online.
2. Admin and student users can log in and receive JWT tokens.
3. Protected routes reject unauthenticated requests.
4. Admin-only routes reject student users.
5. Borrowing-related schema changes can be executed inside database transactions.

### Phase 2: Book Catalog

**Goal:** Let students find books and admins manage catalog records.
**Mode:** mvp
**Requirements:** CAT-01, CAT-02, CAT-03, CAT-04, CAT-05, CAT-06, CAT-07, CAT-08
**UI hint:** yes

**Deliverables:**
- Book catalog API endpoints and frontend views.
- Student catalog browsing and search.
- Search by title, author, and category.
- Availability or stock status in search results.
- Admin CRUD flow for catalog records.
- Search performance checks against the less-than-2-second target.

**Success Criteria:**
1. Students can browse and search the catalog by title, author, and category.
2. Search results show whether a book is available.
3. Admins can create, view, update, and delete valid book records.
4. Catalog deletion preserves lending history and avoids data integrity violations.
5. Search interactions complete within the performance target under expected load.

### Phase 3: Borrowing System

**Goal:** Enable the full lending lifecycle from request through return and overdue handling.
**Mode:** mvp
**Requirements:** LOAN-01, LOAN-02, LOAN-03, LOAN-04, LOAN-05, LOAN-06, LOAN-07, LOAN-08, LOAN-09
**UI hint:** yes

**Deliverables:**
- Student borrow request flow.
- Admin approve and reject workflow.
- Active loan creation and availability updates.
- Return recording flow.
- Student loan status and borrowing history.
- Overdue detection based on due dates.
- In-app overdue notifications for students and admins.

**Success Criteria:**
1. Students can request to borrow available books and see request status.
2. Admins can approve or reject borrow requests.
3. Approved requests create active loans and reduce available stock safely.
4. Admins can record returns and restore availability correctly.
5. Students can view their own active loans and borrowing history.
6. Overdue loans are detected and surfaced in the application.

### Phase 4: Librarian Dashboard & Polish

**Goal:** Deliver operational monitoring, responsive UI, deployment readiness, and maintainability handoff.
**Mode:** mvp
**Requirements:** DASH-01, DASH-02, DASH-03, DASH-04, UX-01, UX-02, UX-03, OPS-01, OPS-02, OPS-03
**UI hint:** yes

**Deliverables:**
- Admin dashboard for pending requests, active loans, and overdue items.
- Role-aware navigation for admin and student views.
- Responsive layouts for desktop and mobile browsers.
- User-facing success and error feedback across core workflows.
- Deployment and handover documentation.
- Final project structure cleanup for maintainability.

**Success Criteria:**
1. Admins can monitor pending requests, active loans, and overdue items from one dashboard.
2. Dashboard data matches current catalog and lending records.
3. Student and admin interfaces expose only role-appropriate actions.
4. Core screens render correctly on mobile and desktop browser widths.
5. Deployment and maintenance documentation is sufficient for handover.

## Coverage

| Phase | Requirement Count |
|-------|-------------------|
| Phase 1 | 8 |
| Phase 2 | 8 |
| Phase 3 | 9 |
| Phase 4 | 10 |

**v1 requirements:** 35
**Mapped:** 35
**Unmapped:** 0

---
*Roadmap created: 2026-06-11*
*Last updated: 2026-06-11 after initial roadmap creation*
