# Demo Script (Presenter Notes Only)

Target length: 5–10 minutes. This file is for your use; you don’t need to include it in submission.

## 1) Intro (20–30s)
- State name.
- Project: Café Fausse — full‑stack web app (React frontend, Flask backend, PostgreSQL DB).
- What you’ll show: pages, reservations flow, newsletter, and DB verification.

## 2) Start/Verify Services (30–45s)
- Mention services are already running.
- If needed: `./verify_setup.sh` shows frontend (5173), backend (5000), DB reachability, API health.

## 3) UI Walkthrough (3–4 min)
- Home page: restaurant name, hours, address, call‑to‑action → Reserve / View Menu.
- Menu page: categories and items; show filtering if you added it (optional).
- Gallery: lightbox images, awards, and reviews.
- About Us: founders and philosophy.
- Reservations page: show the form fields (name, email, phone, date, time, guests, newsletter opt‑in, special requests).

## 4) Make a Reservation (1–2 min)
- Fill the form (pick a date/time within hours; 17:00–23:00 Mon–Sat; 17:00–21:00 Sun).
- Submit → Success message with assigned table number (random from available 30).

## 5) Newsletter Signup (30–45s)
- In the footer, enter an email and subscribe.
- Explain that it creates/updates the customer record with newsletter_signup=true.

## 6) Verify Data in pgAdmin (1–2 min)
- Show pgAdmin: Servers → Cafe Fausse Local → Databases → cafe_fausse_dev → Schemas → public → Tables.
- Open customers and reservations via View/Edit Data → All Rows.
- Point out the inserted reservation row, table number, time slot, and the customer link.

## 7) Tech Overview (45–60s)
- Frontend: React + Vite, routes in `frontend/src/App_cafe.jsx`, pages in `frontend/src/pages`, proxy to /api.
- Backend: Flask app (`backend/app_cafe.py`) exposes REST endpoints; SQLAlchemy models; availability checks and validation; random table selection.
- DB: Postgres local; schema and seed scripts in `database/`.
- Local‑only setup; pgAdmin desktop for DB visibility.

## 8) Close (15–20s)
- Confirm that the demo matched the SRS: 5 pages, reservation system with validation and table assignment, newsletter, gallery and awards, menu with categories.
- Thank you.