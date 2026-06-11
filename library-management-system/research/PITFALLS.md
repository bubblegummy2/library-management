# Pitfalls Research: Library Management System

**Date:** 2026-06-11

## Primary Risks

### Stock Drift

If the app stores both `stockQuantity` and `availableQuantity`, they can diverge. Prefer storing total stock and deriving availability from active loans. If availability is stored later for performance, update it only inside transactions.

### Race Conditions On Borrowing

Two staff users could try to lend the last available copy at the same time. Use transactional borrow logic and validate availability inside the transaction. Prisma notes that transactions should be kept short, and SQLite uses serializable isolation, which helps but does not remove the need for careful mutation design.

Source: https://www.prisma.io/docs/orm/prisma-client/queries/transactions

### Hard Deletes Breaking History

Deleting books or members can break loan history or create confusing reports. Prefer deactivation/soft-delete for members and restrict book deletion when historical loans exist.

### Authorization By UI Only

Hiding admin buttons is not enough. Next.js recommends verifying authorization for Server Actions and Route Handlers because they should be treated like public-facing endpoints.

Source: https://nextjs.org/docs/app/guides/authentication

### Overdue Date Ambiguity

Due dates need consistent handling:

- Store timestamps in UTC or consistently normalized dates.
- Decide whether a loan is overdue at the start of the day after `dueAt`, not at an arbitrary local-time boundary.
- Display dates in the librarian's local timezone.

### Search Quality

Basic Prisma filters support v1 title/author/ISBN/category search, but SQLite search can feel limited for large catalogs. Keep the v1 search simple and add full-text search later only if real catalog size requires it.

Source: https://www.prisma.io/docs/orm/prisma-client/queries/crud

### SQLite Deployment Limits

SQLite is simple and appropriate for v1, but a university-wide production deployment with multiple concurrent users may eventually need PostgreSQL. Keep Prisma models portable and avoid SQLite-specific assumptions where possible.

Source: https://www.prisma.io/docs/orm/reference/supported-databases

## Testing Focus

- Borrowing rejects inactive members.
- Borrowing rejects unavailable books.
- Borrowing creates due date 7 days out by default.
- Returning marks loan returned and removes it from active/overdue counts.
- Overdue calculations handle today, yesterday, and returned overdue loans correctly.
- Role checks block unauthorized mutations.
