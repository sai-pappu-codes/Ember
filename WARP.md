# WARP.md

This file provides guidance to WARP (warp.dev) when working with code in this repository.

## Project Overview

This is a full-stack web application with a React frontend, Flask backend, and PostgreSQL database. The architecture follows a clean separation between frontend and backend, with the backend serving as a REST API.

## Essential Commands

### Quick Start
```bash
# First-time setup
make install        # Install all dependencies
cp .env.example .env  # Configure environment variables
make db-start       # Ensure local PostgreSQL database exists
make db-migrate     # Run database migrations

# Development workflow
make backend        # Start Flask API on port 5001
make frontend       # Start React dev server (default Vite)
make frontend-fixed # Start React dev server on 127.0.0.1:5176 with strictPort
make frontend-preview # Build and serve static bundle on 127.0.0.1:5177
```

### Database Management
```bash
# PostgreSQL operations
brew services start postgresql@16  # or launch Postgres.app
# Stop via OS tooling, e.g., brew services stop postgresql@16
# View logs via your OS service manager or Postgres.app

# Access PostgreSQL CLI
psql -d cafe_fausse_dev

# Database migrations
cd backend && flask db migrate -m "Description"  # Create new migration
cd backend && flask db upgrade                   # Apply migrations
cd backend && flask db downgrade                 # Rollback migration
```


### Building & Deployment
```bash
# Frontend production build
cd frontend && npm run build  # Creates dist/ directory

# Backend production server (uses port 5001)
cd backend && gunicorn -w 4 -b 127.0.0.1:5001 app_cafe:app
```

### Code Quality
```bash
# Frontend linting
cd frontend && npm run lint

# Backend linting (when configured)
cd backend && flake8 .
cd backend && black .  # Auto-format Python code
```

## Architecture & Code Organization

### Frontend Architecture (React + Vite)

The frontend uses Vite for fast development with hot module replacement. Key architectural decisions:

- **API Communication**: All API calls go through `frontend/src/services/api.js` which configures axios with interceptors for authentication and error handling
- **API Base URL**: axios client uses `VITE_API_URL` (e.g., http://127.0.0.1:5001/api). Vite proxy is optional.
- **Component Structure**: Components are organized in `frontend/src/components/` (to be created as needed)
- **Routing**: React Router is installed for client-side routing (implementation pending)

### Backend Architecture (Flask + SQLAlchemy)

The Flask backend serves as a REST API with the following structure:

- **Application Factory**: Main app initialization in `backend/app.py` with Flask extensions (CORS, SQLAlchemy, Migrate)
- **Configuration Management**: Environment-specific configs in `backend/config.py` (Development, Production, Testing)
- **Database Models**: SQLAlchemy models in `backend/models/` directory, currently includes User model
- **Database Migrations**: Flask-Migrate handles schema changes through Alembic
- **CORS**: Enabled for cross-origin requests from frontend

### Database Architecture

PostgreSQL running locally with:
- Database migrations tracked in `backend/migrations/` (optional; `db.create_all` also supported)
- Connection managed through SQLAlchemy ORM

### Cross-Component Communication Flow

1. **Frontend → Backend**: Axios requests through proxy in development, direct API calls in production
2. **Backend → Database**: SQLAlchemy ORM handles all database operations
3. **Authentication Flow**: JWT tokens stored in localStorage, added to requests via axios interceptor
4. **Error Handling**: Centralized error handling in axios response interceptor, automatic redirect on 401

## Development Patterns

### API Endpoint Structure
Backend API endpoints follow RESTful conventions:
- Health check: `GET /api/health`
- API info: `GET /api`
- Future endpoints should follow: `/api/<resource>/<action>`

### Database Model Pattern
Models inherit from `db.Model` and include:
- Timestamps (created_at, updated_at)
- `to_dict()` method for JSON serialization
- Proper `__repr__` for debugging

### Frontend Service Layer
All API calls should go through the service layer (`frontend/src/services/`) which handles:
- Authentication token injection
- Error response handling
- Base URL configuration

## Environment Configuration

Key environment variables (defined in `.env`):
- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Flask session secret
- `FLASK_ENV`: Set to 'development' for debug mode
- `VITE_API_URL`: Frontend API base URL, e.g. `http://127.0.0.1:5001/api`

## Database

This project uses your local PostgreSQL installation (no Docker required):
- Database name: `cafe_fausse_dev`
- Optional GUI: pgAdmin 4 desktop app (install via Homebrew Cask or Postgres.app)

## Common Development Tasks

### Adding a New API Endpoint
1. Create route handler in `backend/app.py` or new route file
2. Add database model if needed in `backend/models/`
3. Create and run migration if database schema changes
4. Update frontend service in `frontend/src/services/`
5. Implement React component to consume the API

### Adding a New Database Model
1. Create model file in `backend/models/`
2. Import model in `backend/app.py`
3. Generate migration: `flask db migrate -m "Add <model> table"`
4. Apply migration: `flask db upgrade`

### Debugging Database Issues
1. Check service status (macOS): `brew services list | grep postgres` or open Postgres.app
2. View tables/rows: `psql -d cafe_fausse_dev -c "\\dt"`
3. Access database directly: `psql -d cafe_fausse_dev`
4. Check migration status: `cd backend && flask db current`
