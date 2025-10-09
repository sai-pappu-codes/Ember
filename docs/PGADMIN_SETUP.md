# pgAdmin Setup (Local PostgreSQL)

This document captures our setup to visualize the Cafe Fausse data in pgAdmin.

## 1) Launch pgAdmin
- Open "pgAdmin 4" from Applications on macOS

## 2) Create a new Server connection
- Right-click "Servers" → Create → Server…
- General → Name: Cafe Fausse Local
- Connection tab:
  - Host: localhost
  - Port: 5432
  - Maintenance DB: postgres (default)
  - Username: your macOS user (e.g., mihai) or postgres if applicable
  - Password: leave empty if your local user has trust/peer auth

Press Save.

## 3) Browse the database
- Expand: Servers → Cafe Fausse Local → Databases
- If you don’t see it yet, create the DB once via terminal:
  ```bash
  createdb cafe_fausse_dev
  ```
- Then expand: Databases → cafe_fausse_dev → Schemas → public → Tables
  - You should see `customers` and `reservations`.

## 4) View data
- Right-click a table → View/Edit Data → All Rows
- You should see real rows after using the web app or running seeds.

## 5) Optional: Run SQL scripts from this repo
- In pgAdmin, open Query Tool
- Load and run:
  - `database/schema.sql` (creates/ensures schema)
  - `database/seed.sql` (adds a sample customer & reservation)
  - `database/queries.sql` (handy demo/debug queries)

## 6) Verifying via Terminal (alternative to pgAdmin)
```bash
psql -d cafe_fausse_dev -c "\\dt"
psql -d cafe_fausse_dev -c "SELECT * FROM customers;"
psql -d cafe_fausse_dev -c "SELECT * FROM reservations;"
```

## Links
- Frontend: http://localhost:5173
- Backend: http://localhost:5000
- Verification script: `./verify_setup.sh`

