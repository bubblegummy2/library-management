# Library Management System

## What This Is

A web application for a university library that helps staff manage the book catalog, members, borrowing, returns, overdue loans, and daily operational statistics. The primary users are librarians and administrators who need a clean, simple interface they can use every day.

The system will be built with Next.js 14 App Router, TypeScript, Prisma ORM, SQLite, and Tailwind CSS.

## Core Value

Librarians can reliably track which books are available, who has borrowed them, and which loans are overdue.

## Requirements

### Validated

(None yet - ship to validate)

### Active

- [ ] Staff can add, edit, delete, and search books by title, author, ISBN, or category.
- [ ] Staff can store book title, author, ISBN, publisher, publication year, category, and stock quantity.
- [ ] Staff can register members, edit member data, and deactivate members.
- [ ] Staff can store member name, student ID, email, phone, and membership status.
- [ ] Librarians can record book loans for active members and set due dates with a default of 7 days.
- [ ] Librarians can process book returns and restore available stock.
- [ ] The system tracks who borrowed which book and when.
- [ ] The system flags overdue loans and calculates days overdue.
- [ ] Staff can view overdue members and overdue loans.
- [ ] Staff can view a dashboard with total books, total members, active loans, and overdue loans.
- [ ] Administrators and librarians have role-based access in v1.

### Out of Scope

- Student/member self-service portal - v1 is staff-facing to keep the daily librarian workflow focused.
- Individual physical copy tracking with barcode or copy IDs - v1 tracks stock as a quantity count per book.
- External integrations with university identity systems - not required for the initial standalone application.
- Email/SMS overdue notifications - useful later, but dashboard-based tracking is enough for v1.
- Fines and payment processing - not part of the stated core library workflow.

## Context

- The application is for a university library, so data entry speed, search clarity, and operational correctness matter more than decorative UI.
- Staff-facing workflows should be simple and predictable: catalog management, member management, loan creation, return processing, overdue tracking, and dashboard review.
- Stock is tracked as a quantity count on each book. Borrowing decrements available stock and returning increments it.
- v1 has administrator and librarian roles. Administrators can manage elevated areas such as staff/role configuration if needed, while librarians handle daily library operations.
- The requested stack is Next.js 14 with App Router, TypeScript, Prisma ORM, SQLite database, and Tailwind CSS.

## Constraints

- **Tech stack**: Next.js 14 App Router, TypeScript, Prisma ORM, SQLite, and Tailwind CSS - chosen by project requirement.
- **Database**: SQLite - suitable for a local/simple deployment, but future multi-user production deployment may require revisiting database choice.
- **Access model**: Admin plus librarian roles - v1 needs role-based access but no student-facing account system.
- **Inventory model**: Quantity count per book - simpler than per-copy tracking and aligned with v1 scope.
- **UI style**: Clean and simple - optimized for repeated librarian use rather than marketing presentation.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Use Next.js 14 App Router with TypeScript | Matches requested stack and supports full-stack web app development. | Pending |
| Use Prisma with SQLite | Matches requested persistence layer and keeps setup simple for v1. | Pending |
| Support admin and librarian roles in v1 | User selected separate admin and librarian access. | Pending |
| Track inventory by book quantity instead of physical copies | User selected quantity-based stock tracking for v1. | Pending |

---
*Last updated: 2026-06-11 after initial project questioning*
