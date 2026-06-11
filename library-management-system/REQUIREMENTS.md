# Requirements: Library Management System

**Defined:** 2026-06-11
**Core Value:** Librarians can reliably track which books are available, who has borrowed them, and which loans are overdue.

## v1 Requirements

### Staff Access

- [ ] **AUTH-01**: Staff user can log in with email and password.
- [ ] **AUTH-02**: Staff user can log out from the application.
- [ ] **AUTH-03**: Administrator can access admin-only areas.
- [ ] **AUTH-04**: Librarian can access daily library operations without admin-only privileges.
- [ ] **AUTH-05**: Unauthorized user cannot access dashboard, books, members, loans, overdue, or admin pages.

### Book Management

- [ ] **BOOK-01**: Staff user can add a book with title, author, ISBN, publisher, publication year, category, and stock quantity.
- [ ] **BOOK-02**: Staff user can edit book details.
- [ ] **BOOK-03**: Staff user can delete a book only when deletion will not break loan history.
- [ ] **BOOK-04**: Staff user can search books by title, author, ISBN, or category.
- [ ] **BOOK-05**: Staff user can see each book's total stock, active loans, and available quantity.
- [ ] **BOOK-06**: System prevents a book loan when available quantity is zero.

### Member Management

- [ ] **MEMB-01**: Staff user can register a member with name, student ID, email, phone, and membership status.
- [ ] **MEMB-02**: Staff user can edit member details.
- [ ] **MEMB-03**: Staff user can deactivate a member.
- [ ] **MEMB-04**: Staff user can search members by name, student ID, email, or phone.
- [ ] **MEMB-05**: System prevents new loans for inactive members.
- [ ] **MEMB-06**: System preserves historical loan records for deactivated members.

### Borrowing And Returns

- [ ] **LOAN-01**: Librarian can create a loan for an active member and an available book.
- [ ] **LOAN-02**: System sets the default due date to 7 days after the loan date.
- [ ] **LOAN-03**: Librarian can override the due date when creating a loan.
- [ ] **LOAN-04**: System records who borrowed which book and when.
- [ ] **LOAN-05**: Librarian can process a return for an active loan.
- [ ] **LOAN-06**: System records the return date when a loan is returned.
- [ ] **LOAN-07**: Returned loans no longer count as active loans.
- [ ] **LOAN-08**: Borrowing and return mutations keep stock availability consistent.

### Overdue Tracking

- [ ] **OVER-01**: System automatically identifies active loans whose due date has passed.
- [ ] **OVER-02**: Staff user can view overdue loans.
- [ ] **OVER-03**: Staff user can view members with overdue loans.
- [ ] **OVER-04**: System calculates and displays how many days each active loan is overdue.
- [ ] **OVER-05**: Returned loans do not appear as active overdue loans.

### Dashboard

- [ ] **DASH-01**: Staff user can view total book count.
- [ ] **DASH-02**: Staff user can view total member count.
- [ ] **DASH-03**: Staff user can view active loan count.
- [ ] **DASH-04**: Staff user can view overdue loan count.
- [ ] **DASH-05**: Staff user can navigate from dashboard metrics to the related operational views.

### User Interface

- [ ] **UI-01**: Staff user can navigate between Dashboard, Books, Members, Loans, Overdue, and Admin areas.
- [ ] **UI-02**: Staff user can complete daily workflows using clean, simple screens suitable for repeated librarian use.
- [ ] **UI-03**: Staff user can distinguish active, inactive, returned, active-loan, and overdue states through clear labels or badges.

## v2 Requirements

### Inventory

- **COPY-01**: Staff user can track individual physical copies with copy IDs or barcodes.
- **COPY-02**: Staff user can track per-copy status.

### Member Self-Service

- **SELF-01**: Member can log in to view current loans.
- **SELF-02**: Member can search the catalog from a student-facing interface.

### Notifications

- **NOTF-01**: System can send overdue reminders by email.
- **NOTF-02**: System can notify staff about loans becoming overdue.

### Reporting

- **REPT-01**: Staff user can export book, member, and loan data.
- **REPT-02**: Staff user can view historical borrowing reports.

## Out of Scope

| Feature | Reason |
|---------|--------|
| Student/member self-service portal | v1 is staff-facing to keep initial workflows focused. |
| Individual copy/barcode tracking | User selected quantity-based stock tracking for v1. |
| University SSO or identity integration | Not required for the standalone initial application. |
| Email/SMS overdue notifications | Dashboard-based overdue tracking covers v1. |
| Fines and payment processing | Not part of the stated core workflow. |
| Mobile app | Web application is the requested delivery target. |

## Traceability

Which phases cover which requirements. Updated during roadmap creation.

| Requirement | Phase | Status |
|-------------|-------|--------|
| AUTH-01 | Phase 1 | Pending |
| AUTH-02 | Phase 1 | Pending |
| AUTH-03 | Phase 1 | Pending |
| AUTH-04 | Phase 1 | Pending |
| AUTH-05 | Phase 1 | Pending |
| BOOK-01 | Phase 2 | Pending |
| BOOK-02 | Phase 2 | Pending |
| BOOK-03 | Phase 2 | Pending |
| BOOK-04 | Phase 2 | Pending |
| BOOK-05 | Phase 2 | Pending |
| BOOK-06 | Phase 3 | Pending |
| MEMB-01 | Phase 2 | Pending |
| MEMB-02 | Phase 2 | Pending |
| MEMB-03 | Phase 2 | Pending |
| MEMB-04 | Phase 2 | Pending |
| MEMB-05 | Phase 3 | Pending |
| MEMB-06 | Phase 2 | Pending |
| LOAN-01 | Phase 3 | Pending |
| LOAN-02 | Phase 3 | Pending |
| LOAN-03 | Phase 3 | Pending |
| LOAN-04 | Phase 3 | Pending |
| LOAN-05 | Phase 3 | Pending |
| LOAN-06 | Phase 3 | Pending |
| LOAN-07 | Phase 3 | Pending |
| LOAN-08 | Phase 3 | Pending |
| OVER-01 | Phase 4 | Pending |
| OVER-02 | Phase 4 | Pending |
| OVER-03 | Phase 4 | Pending |
| OVER-04 | Phase 4 | Pending |
| OVER-05 | Phase 4 | Pending |
| DASH-01 | Phase 4 | Pending |
| DASH-02 | Phase 4 | Pending |
| DASH-03 | Phase 4 | Pending |
| DASH-04 | Phase 4 | Pending |
| DASH-05 | Phase 4 | Pending |
| UI-01 | Phase 1 | Pending |
| UI-02 | Phase 5 | Pending |
| UI-03 | Phase 4 | Pending |

**Coverage:**
- v1 requirements: 38 total
- Mapped to phases: 38
- Unmapped: 0

---
*Requirements defined: 2026-06-11*
*Last updated: 2026-06-11 after roadmap creation*
