# Feature Research: Library Management System

**Date:** 2026-06-11

## Table-Stakes Features For v1

### Staff Access

- Staff login.
- Role-based access for administrator and librarian.
- Logout.
- Basic staff account seed or admin-created staff accounts.

### Book Management

- Add, edit, delete or soft-delete books.
- Search books by title, author, ISBN, and category.
- Store title, author, ISBN, publisher, year, category, and stock quantity.
- Show available quantity, active-loan quantity, and total quantity.
- Prevent lending when no stock is available.

### Member Management

- Register members.
- Edit member details.
- Deactivate members.
- Store name, student ID, email, phone, and status.
- Prevent new loans for inactive members.
- Keep historical loan records when members are deactivated.

### Borrowing And Returns

- Create a loan for an active member and available book.
- Default due date to 7 days from loan date.
- Allow due date override during loan creation if needed.
- Return a loan and record return date.
- Keep loan history after returns.
- Update available stock consistently when loans and returns happen.

### Overdue Tracking

- Flag active loans whose due date is before the current date.
- Calculate days overdue.
- Show overdue loans and overdue members.
- Provide overdue status on loan list and dashboard.

### Dashboard

- Total books.
- Total active members.
- Active loans.
- Overdue loans.
- Links from metrics to filtered operational views.

## Differentiators To Defer

- Student self-service portal.
- Per-copy barcode tracking.
- Email or SMS reminders.
- Fines and payments.
- Book reservation / hold queue.
- Import/export from university systems.
- Audit logs beyond basic created/updated timestamps.

## Requirement Implications

- Role-based access belongs in v1 because the user selected admin plus librarian.
- Quantity-based stock means v1 does not need `BookCopy`, barcode, or per-copy status tables.
- Loan records should remain durable even if a book/member is deactivated, so destructive deletes should be limited.
- Search should be useful on day one; Prisma filtering supports multi-condition search patterns.

Source: https://www.prisma.io/docs/orm/prisma-client/queries/crud
