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
make db-start       # Start PostgreSQL container
make db-migrate     # Run database migrations

# Development workflow
make backend        # Start Flask API on port 5000
make frontend       # Start React dev server on port 5173
```

### Database Management
```bash
# PostgreSQL operations
docker-compose up -d postgres    # Start database
docker-compose down              # Stop database
docker-compose logs postgres     # View database logs

# Access PostgreSQL CLI
docker-compose exec postgres psql -U postgres -d responsive_web_app_dev

# Database migrations
cd backend && flask db migrate -m "Description"  # Create new migration
cd backend && flask db upgrade                   # Apply migrations
cd backend && flask db downgrade                 # Rollback migration
```

### Testing
```bash
# Run backend tests (when implemented)
cd backend && pytest
cd backend && pytest tests/test_specific.py::TestCase::test_method  # Run single test

# Run frontend tests (when implemented)  
cd frontend && npm test
cd frontend && npm test -- --watch  # Watch mode
```

### Building & Deployment
```bash
# Frontend production build
cd frontend && npm run build  # Creates dist/ directory

# Backend production server
cd backend && gunicorn -w 4 -b 0.0.0.0:5000 app:app
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
- **Proxy Configuration**: Development server proxies `/api` requests to `localhost:5000` (configured in `vite.config.js`)
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

PostgreSQL running in Docker container with:
- Database migrations tracked in `backend/migrations/` (created after first migration)
- Initial setup script in `database/init.sql` (if provided)
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
- `VITE_API_URL`: Frontend API base URL (optional, defaults to proxy)

## Docker Services

The application uses Docker Compose for database services:
- **postgres**: Main PostgreSQL database on port 5432
- **pgadmin**: Optional database GUI on port 5050 (use `--profile tools` to enable)

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
1. Check container status: `docker-compose ps`
2. View logs: `docker-compose logs postgres`
3. Access database directly: `docker-compose exec postgres psql -U postgres -d responsive_web_app_dev`
4. Check migration status: `flask db current`
