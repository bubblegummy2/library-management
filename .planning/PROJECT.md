# Library Management System (LMS) for Universitas XYZ

## What This Is

Library Management System (LMS) for Universitas XYZ is a centralized web application that replaces manual library records kept on paper and spreadsheets. Students use it to search books, check stock, request borrowing, return books, and view their own loan history. Admins or library staff use it to manage the catalog, verify borrow and return activity, monitor overdue items, and review operational status through a dashboard.

## Core Value

Universitas XYZ must have one reliable digital source of truth for catalog availability and the full book lending lifecycle.

## Requirements

### Validated

(None yet - ship to validate)

### Active

- [ ] Admins can create, read, update, and delete book catalog records.
- [ ] Students can search books by title, author, and category.
- [ ] Students can view book stock or availability status before borrowing.
- [ ] Students can borrow books through the web system.
- [ ] Students can return books through a tracked return flow.
- [ ] Admins can verify borrowing and return activity.
- [ ] The system tracks active loans, returned books, overdue items, and student borrowing history.
- [ ] The system notifies users inside the application when book returns are overdue.
- [ ] Admins can monitor key library activity from a dashboard.
- [ ] The system supports authentication and role management for admin and student users.
- [ ] Authentication uses password hashing and JWT-based access control.
- [ ] Role-based authorization protects admin-only operations.
- [ ] Book search responses complete in less than 2 seconds under expected academic project load.
- [ ] The system is designed to be available 24/7 on Docker-capable server infrastructure.
- [ ] The UI is responsive on desktop and mobile browsers.
- [ ] Code is structured and documented enough for maintainability after handover.
- [ ] Borrow and return transactions preserve data integrity with ACID-safe database operations.

### Out of Scope

- Online fine payment - fines may be recorded manually, but money is handled outside the system.
- Native mobile app - the LMS will be a responsive web application only.
- Academic system integration - no integration with student information systems or campus SSO in this scope.
- Email or SMS notifications - overdue notifications are in-app only.
- PDF report generation - dashboards and on-screen reporting are enough for v1.
- Multi-language support - the first version uses a single language.
- Inter-library loans - the system manages only Universitas XYZ library inventory.
- E-book or digital content delivery - the LMS tracks physical library books.

## Context

Universitas XYZ currently relies on paper logs and spreadsheets for library operations. This makes book availability hard for students to confirm, creates duplicate work for library staff, and leaves overdue books difficult to monitor reliably. The project replaces that manual process with a single browser-based system that centralizes catalog data, borrowing records, returns, and overdue tracking.

The primary user groups are:

- **Admin/Petugas Perpustakaan**: manage book data, verify borrowing and returns, inspect reports, and monitor the dashboard.
- **Mahasiswa**: search books, check stock, borrow and return books, and view personal borrowing history.

Existing reference material for the project includes a human-written brief, project specification, and roadmap under `sample-project/library-management/`. The current project definition extends that reference with additional non-functional requirements and explicit scope exclusions from the user brief.

## Constraints

- **Tech stack**: Backend uses FastAPI with Python, frontend uses React with JavaScript, database uses PostgreSQL, and deployment uses Docker - this stack is already selected.
- **Security**: Passwords must be hashed, JWT must be used for authenticated access, and role-based authorization must protect admin functionality - library records and user access depend on correct permission boundaries.
- **Performance**: Search responses must complete in less than 2 seconds - students need quick catalog lookup during normal library use.
- **Availability**: The system should be accessible 24/7 - students and staff may need access outside desk-only operating windows.
- **Responsive UI**: The application must work on desktop and mobile browsers - there will be no native mobile app.
- **Data integrity**: Borrow and return operations must be transactionally safe - stock counts, loan status, and history cannot drift apart.
- **Maintainability**: Code should be structured and documented for handover - the university is expected to maintain it after delivery.
- **Deployment**: Docker is required so the system can run on the university's existing Docker-capable infrastructure.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Build a centralized web LMS instead of extending manual spreadsheet workflows | Manual records are fragmented, slow to reconcile, and make overdue tracking unreliable | - Pending |
| Use FastAPI, React, PostgreSQL, and Docker | The user selected this stack and it fits a maintainable web application with transactional data | - Pending |
| Use JWT and role-based access for admin and student separation | Admin catalog and lending operations must not be available to students | - Pending |
| Keep overdue notification in-app only | Email and SMS are explicitly out of scope for v1 | - Pending |
| Keep fine payment manual | Online payment adds integration and compliance complexity outside the project goal | - Pending |
| Deliver responsive web instead of native mobile | Mobile access is required, but native apps are explicitly out of scope | - Pending |
| Treat borrow and return operations as ACID-safe transactions | Loan status, stock availability, and borrowing history must remain consistent | - Pending |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition** (via `$gsd-transition`):
1. Requirements invalidated? -> Move to Out of Scope with reason
2. Requirements validated? -> Move to Validated with phase reference
3. New requirements emerged? -> Add to Active
4. Decisions to log? -> Add to Key Decisions
5. "What This Is" still accurate? -> Update if drifted

**After each milestone** (via `$gsd-complete-milestone`):
1. Full review of all sections
2. Core Value check - still the right priority?
3. Audit Out of Scope - reasons still valid?
4. Update Context with current state

---
*Last updated: 2026-06-11 after initialization*
