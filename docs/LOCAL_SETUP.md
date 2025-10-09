# Local Setup & Verification

## Start Services
```bash
# Terminal 1 - Backend
cd backend
source venv/bin/activate
python3 app_cafe.py

# Terminal 2 - Frontend
cd frontend
npm run dev
```

## Verify with Script
From repo root:
```bash
./verify_setup.sh
```
It checks:
- Frontend on 5173
- Backend on 5000
- PostgreSQL database `cafe_fausse_dev`
- API health endpoint

## Useful URLs
- Frontend: http://localhost:5173
- Backend API root: http://localhost:5000/api
- Backend health: http://localhost:5000/api/health

## Database Commands (psql)
```bash
createdb cafe_fausse_dev
psql -d cafe_fausse_dev -c "\\dt"
psql -d cafe_fausse_dev -c "SELECT * FROM customers;"
psql -d cafe_fausse_dev -c "SELECT * FROM reservations;"
```

## pgAdmin
See `docs/PGADMIN_SETUP.md` for GUI steps.

