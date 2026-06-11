# Requirements: Library Management System (LMS) for Universitas XYZ

**Defined:** 2026-06-11
**Core Value:** Universitas XYZ must have one reliable digital source of truth for catalog availability and the full book lending lifecycle.

## v1 Requirements

### Foundation

- [ ] **FND-01**: The full stack can be started locally with Docker Compose, including FastAPI backend, React frontend, and PostgreSQL database.
- [ ] **FND-02**: The database schema stores users, roles, books, book inventory state, borrow requests, active loans, returns, and borrowing history.
- [ ] **FND-03**: Database changes for borrowing and returning books use ACID-safe transactions so stock, loan status, and history stay consistent.

### Authentication

- [ ] **AUTH-01**: Admins and students can log in with registered credentials.
- [ ] **AUTH-02**: Passwords are stored using secure hashing, never plaintext.
- [ ] **AUTH-03**: Authenticated users receive JWT access tokens for protected API requests.
- [ ] **AUTH-04**: Protected API routes reject requests without a valid token.
- [ ] **AUTH-05**: Role-based authorization separates admin-only actions from student actions.

### Catalog

- [ ] **CAT-01**: Admins can create book catalog records.
- [ ] **CAT-02**: Admins can view book catalog records.
- [ ] **CAT-03**: Admins can update book catalog records.
- [ ] **CAT-04**: Admins can delete book catalog records when deletion does not violate lending history.
- [ ] **CAT-05**: Students can browse the book catalog.
- [ ] **CAT-06**: Students can search books by title, author, and category.
- [ ] **CAT-07**: Search results show current stock or availability status.
- [ ] **CAT-08**: Book search responses complete in less than 2 seconds under expected academic project load.

### Borrowing

- [ ] **LOAN-01**: Students can submit a request to borrow an available book.
- [ ] **LOAN-02**: Admins can approve or reject borrow requests.
- [ ] **LOAN-03**: Approved borrow requests create active loan records and update book availability.
- [ ] **LOAN-04**: Students can see the status of their borrow requests and active loans.
- [ ] **LOAN-05**: Admins can record book returns.
- [ ] **LOAN-06**: Returned books update availability and borrowing history correctly.
- [ ] **LOAN-07**: Students can view their own borrowing history.
- [ ] **LOAN-08**: The system identifies overdue active loans based on due dates.
- [ ] **LOAN-09**: The system surfaces in-app overdue notifications to affected students and admins.

### Dashboard

- [ ] **DASH-01**: Admins can view a dashboard summary of pending borrow requests.
- [ ] **DASH-02**: Admins can view a dashboard summary of active loans.
- [ ] **DASH-03**: Admins can view a dashboard summary of overdue items.
- [ ] **DASH-04**: Dashboard data reflects current catalog and lending records.

### User Experience

- [ ] **UX-01**: The web UI is responsive on desktop and mobile browsers.
- [ ] **UX-02**: Admin and student navigation expose only actions relevant to the user's role.
- [ ] **UX-03**: Core screens provide clear success and error feedback for catalog, borrow, return, and authentication actions.

### Operations

- [ ] **OPS-01**: The application is structured for 24/7 deployment on Docker-capable infrastructure.
- [ ] **OPS-02**: Backend, frontend, and database configuration are documented for handover.
- [ ] **OPS-03**: Code is organized into maintainable backend, frontend, and database boundaries.

## v2 Requirements

Deferred to future release. Tracked but not in current roadmap.

### Reporting

- **RPT-01**: Admins can export PDF reports.

### Integrations

- **INT-01**: The LMS can integrate with the university academic system.
- **INT-02**: Users can receive overdue notifications by email or SMS.

### Platform

- **MOB-01**: Users can access the LMS through a native mobile application.
- **I18N-01**: Users can switch between multiple interface languages.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Online fine payment | Fines may be recorded manually; payment handling is outside the project scope. |
| Native mobile app | The selected delivery channel is responsive web. |
| Academic system integration | v1 keeps user and role management inside the LMS. |
| Email or SMS notifications | v1 uses in-app overdue notifications only. |
| PDF report generation | Dashboard and on-screen reporting are enough for v1. |
| Multi-language support | v1 uses a single language to reduce delivery complexity. |
| Inter-library loans | The system manages only Universitas XYZ inventory. |
| E-book or digital content delivery | The LMS tracks physical books only. |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| FND-01 | Phase 1 | Pending |
| FND-02 | Phase 1 | Pending |
| FND-03 | Phase 1 | Pending |
| AUTH-01 | Phase 1 | Pending |
| AUTH-02 | Phase 1 | Pending |
| AUTH-03 | Phase 1 | Pending |
| AUTH-04 | Phase 1 | Pending |
| AUTH-05 | Phase 1 | Pending |
| CAT-01 | Phase 2 | Pending |
| CAT-02 | Phase 2 | Pending |
| CAT-03 | Phase 2 | Pending |
| CAT-04 | Phase 2 | Pending |
| CAT-05 | Phase 2 | Pending |
| CAT-06 | Phase 2 | Pending |
| CAT-07 | Phase 2 | Pending |
| CAT-08 | Phase 2 | Pending |
| LOAN-01 | Phase 3 | Pending |
| LOAN-02 | Phase 3 | Pending |
| LOAN-03 | Phase 3 | Pending |
| LOAN-04 | Phase 3 | Pending |
| LOAN-05 | Phase 3 | Pending |
| LOAN-06 | Phase 3 | Pending |
| LOAN-07 | Phase 3 | Pending |
| LOAN-08 | Phase 3 | Pending |
| LOAN-09 | Phase 3 | Pending |
| DASH-01 | Phase 4 | Pending |
| DASH-02 | Phase 4 | Pending |
| DASH-03 | Phase 4 | Pending |
| DASH-04 | Phase 4 | Pending |
| UX-01 | Phase 4 | Pending |
| UX-02 | Phase 4 | Pending |
| UX-03 | Phase 4 | Pending |
| OPS-01 | Phase 4 | Pending |
| OPS-02 | Phase 4 | Pending |
| OPS-03 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 35 total
- Mapped to phases: 35
- Unmapped: 0

---
*Requirements defined: 2026-06-11*
*Last updated: 2026-06-11 after initial definition*
