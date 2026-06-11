# Research Summary: Library Management System

**Date:** 2026-06-11

## Stack

The selected stack is appropriate for a v1 university library staff application:

- Next.js 14 App Router with TypeScript.
- Server Components for data views.
- Server Actions for form-driven mutations.
- Prisma ORM with SQLite.
- Tailwind CSS for a simple operational UI.

Key source references:

- Next.js updating data / Server Actions: https://nextjs.org/docs/app/getting-started/updating-data
- Next.js authentication and authorization: https://nextjs.org/docs/app/guides/authentication
- Prisma with Next.js: https://www.prisma.io/docs/guides/frameworks/nextjs
- Prisma CRUD and filtering: https://www.prisma.io/docs/orm/prisma-client/queries/crud
- Prisma transactions: https://www.prisma.io/docs/orm/prisma-client/queries/transactions
- Prisma supported databases: https://www.prisma.io/docs/orm/reference/supported-databases

## Table Stakes

- Staff login.
- Admin and librarian roles.
- Book catalog CRUD and search.
- Member registration, editing, and deactivation.
- Loan creation with 7-day default due date.
- Return processing.
- Active loan tracking.
- Overdue loan and overdue member views.
- Dashboard metrics for total books, members, active loans, and overdue loans.

## Recommended Architecture

- Centralize auth and role checks in a DAL.
- Use DTOs or explicit select objects to avoid leaking sensitive staff/member fields.
- Keep a shared Prisma client module.
- Store total book stock, derive availability from active loan count.
- Use transactional server-side mutations for borrowing and returns.
- Keep loan history durable; avoid destructive deletes when records have history.

## Watch Out For

- Race conditions when lending the last available copy.
- Stock drift if available stock is stored separately.
- Admin/librarian role checks being enforced only in UI.
- Deleting books or members that have loan history.
- Overdue date calculations around timezone and date boundaries.
- SQLite becoming a deployment constraint if the app grows beyond a simple single-instance deployment.

## Roadmap Implication

Build as a vertical MVP:

1. Foundation, data model, auth, and staff shell.
2. Book and member management.
3. Borrow/return workflow with transactional consistency.
4. Overdue tracking and dashboard.
5. Polish, validation, and operational hardening.
