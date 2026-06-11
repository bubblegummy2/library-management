# Roadmap: Library Management System

**Created:** 2026-06-11
**Project mode:** Vertical MVP
**Requirements covered:** 38/38 v1 requirements

## Phase Overview

| Phase | Name | Goal | Requirements |
|-------|------|------|--------------|
| 1 | Foundation, Auth, and Staff Shell | Establish the application foundation, database model, staff authentication, role gates, and core navigation. | AUTH-01, AUTH-02, AUTH-03, AUTH-04, AUTH-05, UI-01 |
| 2 | Catalog and Member Records | Deliver staff-facing book and member management with searchable operational records. | BOOK-01, BOOK-02, BOOK-03, BOOK-04, BOOK-05, MEMB-01, MEMB-02, MEMB-03, MEMB-04, MEMB-06 |
| 3 | Borrowing and Returns | Deliver the core librarian workflow for loan creation, due dates, returns, and stock consistency. | BOOK-06, MEMB-05, LOAN-01, LOAN-02, LOAN-03, LOAN-04, LOAN-05, LOAN-06, LOAN-07, LOAN-08 |
| 4 | Overdue Tracking and Dashboard | Make overdue work visible and provide daily operational metrics. | OVER-01, OVER-02, OVER-03, OVER-04, OVER-05, DASH-01, DASH-02, DASH-03, DASH-04, DASH-05, UI-03 |
| 5 | Operational Polish and Verification | Harden the daily librarian experience and verify the MVP against all scoped requirements. | UI-02 |

## Phases

### Phase 1: Foundation, Auth, and Staff Shell

**Goal:** Establish the application foundation, database model, staff authentication, role gates, and core navigation.
**Mode:** mvp

**Requirements:** AUTH-01, AUTH-02, AUTH-03, AUTH-04, AUTH-05, UI-01

**Success Criteria**:
1. A staff user can log in and log out.
2. Unauthenticated users cannot access protected library pages.
3. Admin-only pages are blocked for librarian users.
4. Staff users can navigate between Dashboard, Books, Members, Loans, Overdue, and Admin areas.
5. Prisma and SQLite are configured with the initial domain schema and seedable staff accounts.

**UI hint:** yes

### Phase 2: Catalog and Member Records

**Goal:** Deliver staff-facing book and member management with searchable operational records.
**Mode:** mvp

**Requirements:** BOOK-01, BOOK-02, BOOK-03, BOOK-04, BOOK-05, MEMB-01, MEMB-02, MEMB-03, MEMB-04, MEMB-06

**Success Criteria**:
1. Staff can create, edit, and search book records by title, author, ISBN, or category.
2. Staff can see total stock, active loan count, and available quantity for each book.
3. Staff can register, edit, search, and deactivate members.
4. Historical member and book relationships are preserved when records are deactivated or protected from unsafe deletion.

**UI hint:** yes

### Phase 3: Borrowing and Returns

**Goal:** Deliver the core librarian workflow for loan creation, due dates, returns, and stock consistency.
**Mode:** mvp

**Requirements:** BOOK-06, MEMB-05, LOAN-01, LOAN-02, LOAN-03, LOAN-04, LOAN-05, LOAN-06, LOAN-07, LOAN-08

**Success Criteria**:
1. Librarians can create loans only for active members and books with available quantity.
2. New loans default to a due date 7 days after the loan date while still allowing due date override.
3. Loan records show which member borrowed which book and when.
4. Librarians can return active loans and returned loans no longer count as active.
5. Borrow and return flows keep availability consistent through server-side validation and transactional updates.

**UI hint:** yes

### Phase 4: Overdue Tracking and Dashboard

**Goal:** Make overdue work visible and provide daily operational metrics.
**Mode:** mvp

**Requirements:** OVER-01, OVER-02, OVER-03, OVER-04, OVER-05, DASH-01, DASH-02, DASH-03, DASH-04, DASH-05, UI-03

**Success Criteria**:
1. Active loans past their due date are flagged as overdue.
2. Staff can view overdue loans and members with overdue loans.
3. The app displays how many days each active overdue loan is overdue.
4. Returned loans do not appear as active overdue loans.
5. Dashboard metrics show total books, total members, active loans, and overdue loans with navigation to related views.

**UI hint:** yes

### Phase 5: Operational Polish and Verification

**Goal:** Harden the daily librarian experience and verify the MVP against all scoped requirements.
**Mode:** mvp

**Requirements:** UI-02

**Success Criteria**:
1. Daily workflows are clean, simple, and efficient for repeated librarian use.
2. Forms provide useful validation and error states for common mistakes.
3. Tables, filters, and status labels remain readable on desktop and mobile widths.
4. Seed data and verification steps cover staff access, catalog management, member management, loans, returns, overdue tracking, and dashboard counts.
5. All 38 v1 requirements have verification evidence before the MVP is considered complete.

**UI hint:** yes

## Coverage

| Requirement Area | Total | Covered |
|------------------|-------|---------|
| Staff Access | 5 | 5 |
| Book Management | 6 | 6 |
| Member Management | 6 | 6 |
| Borrowing And Returns | 8 | 8 |
| Overdue Tracking | 5 | 5 |
| Dashboard | 5 | 5 |
| User Interface | 3 | 3 |

**All v1 requirements covered:** yes
