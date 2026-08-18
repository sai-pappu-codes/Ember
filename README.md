# Café Fausse - Fine Dining Web Application

A sophisticated, full-stack web application for Café Fausse, an elegant fine-dining restaurant. This project features a React frontend with responsive design, Flask REST API backend, and PostgreSQL database for managing reservations and customer data.

## 🏗️ Architecture

- **Frontend**: React with Vite for fast development and optimal production builds
- **Backend**: Flask REST API with SQLAlchemy ORM
- **Database**: PostgreSQL (local install)
- **Development**: Hot module replacement, CORS enabled, and database migrations

## 📋 Prerequisites

- Node.js (v16 or higher)
- Python 3.8+
- PostgreSQL (local install)
- pgAdmin 4 (optional)
- Git

## 🚀 Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/chindris-mihai-alexandru/cafe-fausse.git
cd cafe-fausse
```

### 2. Set up environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Prepare the database
```bash
# Ensure PostgreSQL is running (e.g., Homebrew: brew services start postgresql@16 or use Postgres.app)
createdb cafe_fausse_dev || true
psql -d cafe_fausse_dev -c "\\dt"
```

### 4. Set up the backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Initialize database
flask db upgrade

# Run the Flask server
python app_cafe.py
```

### 5. Set up the frontend
```bash
# In a new terminal
cd frontend
npm install
npm run dev
```

The application will be available at:
- Frontend: http://localhost:5173
- Backend API: http://localhost:5000
- pgAdmin (optional): use the desktop app (Applications → pgAdmin 4) or `brew install --cask pgadmin4`

## 📁 Project Structure

```
cafe-fausse/
├── backend/              # Flask backend
│   ├── app_cafe.py      # Main Flask application
│   ├── config.py        # Configuration settings
│   ├── models/          # Database models
│   ├── migrations/      # Database migrations
│   └── requirements.txt # Python dependencies
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── pages/       # Page components  
│   │   ├── services/    # API services
│   │   └── App_cafe.jsx # Main app component
│   ├── public/
│   │   └── images/      # Restaurant images (21 images)
│   ├── package.json     # Node dependencies
│   └── vite.config.js   # Vite configuration
├── database/            # Database files
│   ├── schema.sql       # PostgreSQL schema
│   ├── seed.sql         # Sample data
│   └── queries.sql      # Demo queries
├── docs/                # Documentation
│   └── AI_TOOLS_USAGE.md # AI tools documentation (required)
├── .env.example         # Environment variables template
├── README.md            # Project documentation
├── WARP.md              # Development guidelines
└── Makefile             # Build automation
```

## 🛠️ Development

### Backend Development

```bash
cd backend
source venv/bin/activate
python app_cafe.py
```

The Flask API will run on `http://localhost:5000` with hot-reloading enabled.

### Frontend Development

```bash
cd frontend
npm run dev
```

The React app will run on `http://localhost:5173` with hot module replacement.

### Database Management

```bash
# Ensure PostgreSQL is running (macOS examples)
brew services start postgresql@16  # or launch Postgres.app

# Create the dev database (idempotent)
createdb cafe_fausse_dev || true

# Access PostgreSQL CLI and run quick checks
psql -d cafe_fausse_dev -c "\\dt"
psql -d cafe_fausse_dev -c "SELECT COUNT(*) FROM customers;" || true
psql -d cafe_fausse_dev -c "SELECT COUNT(*) FROM reservations;" || true
```



## 📦 Production Build

### Frontend Build
```bash
cd frontend
npm run build
```

### Backend Deployment
```bash
# Backend now uses port 5001 by default
cd backend
gunicorn -w 4 -b 127.0.0.1:5001 app_cafe:app
```

## 🔄 Updated Notes (2025-09-15)

- Backend Flask API runs on port 5001 to avoid macOS AirPlay conflicts on 5000
- Frontend calls the API directly via axios using VITE_API_URL
- Recommended local setups:
  - Dev (fixed IPv4 + port):
    ```bash
    # Frontend
    cd frontend
    npm run dev -- --host 127.0.0.1 --port 5176 --strictPort
    # Backend
    cd backend && source venv/bin/activate && python app_cafe.py  # http://127.0.0.1:5001
    ```
  - Static preview (no dev proxy needed):
    ```bash
    # Build and serve the production bundle
    cd frontend && npm run build
    python3 -m http.server 5177 --bind 127.0.0.1 --directory frontend/dist
    # App: http://127.0.0.1:5177  |  API: http://127.0.0.1:5001
    ```

### Frontend API configuration

- Set the API base URL in `frontend/.env.local`:
  ```bash
  VITE_API_URL=http://127.0.0.1:5001/api
  ```
- All UI API calls go through `src/services/api.js` (axios). The Vite dev proxy is optional fallback.

## 🔧 Configuration

### Environment Variables

See `.env.example` for all available configuration options:

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Flask secret key for sessions
- `POSTGRES_USER`: PostgreSQL username
- `POSTGRES_PASSWORD`: PostgreSQL password
- `POSTGRES_DB`: Database name

## 📝 Course Project

This is a student submission for the Web Application and Interface Design course, demonstrating a full-stack restaurant website with React, Flask, and PostgreSQL.
