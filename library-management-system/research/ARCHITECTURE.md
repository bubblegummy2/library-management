# Architecture Research: Library Management System

**Date:** 2026-06-11

## Recommended Domain Model

### StaffUser

- `id`
- `name`
- `email` unique
- `passwordHash`
- `role`: `ADMIN` or `LIBRARIAN`
- `status`: `ACTIVE` or `INACTIVE`
- timestamps

### Book

- `id`
- `title`
- `author`
- `isbn` unique
- `publisher`
- `year`
- `category`
- `stockQuantity`
- timestamps

Derived values:

- `activeLoanCount`
- `availableQuantity = stockQuantity - activeLoanCount`

Do not store `availableQuantity` unless there is a strong reason; deriving it avoids drift.

### Member

- `id`
- `name`
- `studentId` unique
- `email`
- `phone`
- `status`: `ACTIVE` or `INACTIVE`
- timestamps

### Loan

- `id`
- `bookId`
- `memberId`
- `borrowedAt`
- `dueAt`
- `returnedAt` nullable
- `createdById` staff user
- `returnedById` nullable staff user
- timestamps

Computed states:

- Active: `returnedAt == null`
- Overdue: `returnedAt == null && dueAt < today`
- Days overdue: difference between today and `dueAt`

## Transaction Boundaries

Borrow and return workflows should run in transactions because they combine validation, loan writes, and stock availability checks. Prisma supports sequential and interactive transactions, and interactive transactions are appropriate for conditional logic between reads and writes.

Recommended borrow flow:

1. Verify staff role.
2. In one transaction, read active member and book.
3. Count active loans for that book.
4. Reject if member inactive or available quantity is 0.
5. Create loan with due date defaulting to 7 days.

Recommended return flow:

1. Verify staff role.
2. In one transaction, find active loan.
3. Reject if already returned.
4. Set `returnedAt` and `returnedById`.

Source: https://www.prisma.io/docs/orm/prisma-client/queries/transactions

## App Router Structure

Suggested route groups:

- `app/(auth)/login`
- `app/(dashboard)/dashboard`
- `app/(dashboard)/books`
- `app/(dashboard)/members`
- `app/(dashboard)/loans`
- `app/(dashboard)/overdue`
- `app/(dashboard)/admin/staff`

Suggested server modules:

- `src/lib/prisma.ts`
- `src/lib/auth/session.ts`
- `src/lib/auth/dal.ts`
- `src/lib/books/actions.ts`
- `src/lib/members/actions.ts`
- `src/lib/loans/actions.ts`
- `src/lib/dashboard/queries.ts`

## UI Architecture

- Use dense but readable tables for books, members, loans, and overdue items.
- Use forms in pages or dialogs for CRUD.
- Use badges for member status, loan status, role, and overdue state.
- Make dashboard metric cards actionable links to filtered views.
- Keep navigation stable: Dashboard, Books, Members, Loans, Overdue, Admin.

## Data Access Rule

All sensitive queries and mutations should pass through DAL/server-side functions that verify session and role. Next.js docs recommend centralizing authorization in a DAL and using DTOs to avoid exposing unnecessary data.

Source: https://nextjs.org/docs/app/guides/authentication
