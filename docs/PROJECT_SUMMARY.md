# Project Summary (Cafe Fausse)

This summarizes what we built and how to run/verify it.

## Architecture
- Frontend: React + Vite (port 5173), React Router, CSS Grid/Flexbox, lightbox gallery
- Backend: Flask (port 5000), SQLAlchemy ORM, Flask-Migrate ready, CORS
- Database: PostgreSQL (local), DB name `cafe_fausse_dev`

## Core Features Implemented
- Five pages: Home, Menu, Reservations, About, Gallery
- Menu data via `/api/menu`
- Reservation system with validation and 30-table management
- Newsletter signup stored in `customers`
- Gallery with lightbox, awards, and reviews

## How to Run
```bash
# Backend
cd backend
source venv/bin/activate
python3 app_cafe.py

# Frontend (separate terminal)
cd frontend
npm run dev
```

- Frontend: http://localhost:5173
- Backend: http://localhost:5000

## Database
- Create DB: `createdb cafe_fausse_dev`
- Verify: `psql -d cafe_fausse_dev -c "\\dt"`
- Schema/Seeds: `database/schema.sql`, `database/seed.sql`

## Verify Everything
Run `./verify_setup.sh` from repo root. It checks:
- Frontend server (5173)
- Backend server (5000)
- PostgreSQL availability and row counts
- API health endpoint

## Where to Look in Code
- Backend API: `backend/app_cafe.py`
- Models: in `app_cafe.py` (inline) and `backend/models/`
- Frontend pages: `frontend/src/pages/`
- Service layer (axios): `frontend/src/services/api.js`

## Extras
- Docs for pgAdmin: `docs/PGADMIN_SETUP.md`
- AI tooling usage: `AI_TOOLS_USAGE.md`
- WARP instructions: `WARP.md`
