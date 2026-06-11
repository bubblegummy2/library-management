# Stack Research: Library Management System

**Date:** 2026-06-11

## Recommended Stack Shape

- **Framework:** Next.js 14 App Router with TypeScript.
- **Data access:** Prisma ORM with SQLite for v1.
- **Styling:** Tailwind CSS with a restrained, staff-facing dashboard layout.
- **Mutation path:** Server Actions for form-driven create/update/delete workflows.
- **Authorization path:** Centralized data access layer (DAL) that verifies session and role before reads or mutations.

## Findings

### Next.js App Router

Next.js documentation describes Server Functions as async server-side functions that can be invoked from the client through a network request. In mutation contexts they are Server Actions, and form actions are a natural fit for staff workflows such as adding books, registering members, creating loans, and processing returns.

For this project, prefer:

- Server Components for data-heavy list/detail pages.
- Server Actions for form submissions and mutations.
- `revalidatePath` after mutations that affect dashboard counts, catalog lists, member lists, or loan lists.
- Route Handlers only where an explicit API endpoint is needed.

Source: https://nextjs.org/docs/app/getting-started/updating-data

### Authentication And Authorization

Next.js recommends centralizing authorization in a Data Access Layer, using secure checks for sensitive operations, and using DTOs to return only necessary fields. It also notes that Server Actions and Route Handlers should be treated like public-facing endpoints and must verify whether the user can perform the mutation.

For this project:

- Use a `verifySession()` or equivalent DAL function.
- Store staff users with roles: `ADMIN`, `LIBRARIAN`.
- Gate admin-only actions separately from librarian daily operations.
- Do not rely only on hidden UI controls for authorization.
- Avoid returning password hashes or internal fields to client components.

Source: https://nextjs.org/docs/app/guides/authentication

### Prisma With Next.js

Prisma's Next.js guide uses a shared Prisma Client pattern that caches the client on `global` in development to avoid repeated instantiation during hot reloads. The exact adapter setup differs by database, but the pattern remains relevant: keep a single shared Prisma entrypoint.

For this project:

- Put Prisma client setup in a single module, for example `src/lib/prisma.ts`.
- Keep database operations behind domain-level server functions or DAL functions.
- Model relations explicitly: books, members, loans, and staff users.

Source: https://www.prisma.io/docs/guides/frameworks/nextjs

### SQLite

Prisma supports SQLite as a datasource provider. SQLite is appropriate for a simple local or single-instance v1, but it should be treated as a constraint if the app later needs concurrent production use across many staff users or hosted horizontal scaling.

Sources:

- https://www.prisma.io/docs/orm/reference/supported-databases
- https://www.prisma.io/docs/orm/reference/prisma-schema-reference

## Stack Decision

The requested stack is a good fit for an MVP university library app. The main implementation risk is not framework mismatch; it is maintaining consistency between book stock and loan records. That should be handled with transactional server-side mutations.
