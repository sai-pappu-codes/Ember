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
git clone <repository-url>
cd responsive-web-app
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

# Initialize database migrations
flask db init
flask db migrate -m "Initial migration"
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
responsive-web-app/
├── backend/              # Flask backend
│   ├── app.py           # Main application file
│   ├── config.py        # Configuration settings
│   ├── models/          # Database models
│   ├── routes/          # API routes
│   └── requirements.txt # Python dependencies
├── frontend/            # React frontend
│   ├── src/
│   │   ├── components/  # React components
│   │   ├── services/    # API services
│   │   ├── App.jsx      # Main app component
│   │   └── main.jsx     # Entry point
│   ├── package.json     # Node dependencies
│   └── vite.config.js   # Vite configuration
├── database/            # Database related files
│   ├── migrations/      # Database migrations
│   ├── seeds/          # Seed data
│   ├── schema.sql      # Application schema (customers, reservations)
│   ├── seed.sql        # Sample data
│   └── queries.sql     # Handy demo/debug queries
├── .env.example        # Environment variables template
└── README.md           # This file
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

### Database Migrations

```bash
cd backend
flask db migrate -m "Description of changes"
flask db upgrade
```

## 🧪 Testing

### Backend Tests
```bash
cd backend
pytest
```

### Frontend Tests
```bash
cd frontend
npm test
```

## 📦 Production Build

### Frontend Build
```bash
cd frontend
npm run build
```

### Backend Deployment
```bash
cd backend
gunicorn -w 4 -b 127.0.0.1:5000 app_cafe:app
```

## 🔧 Configuration

### Environment Variables

See `.env.example` for all available configuration options:

- `DATABASE_URL`: PostgreSQL connection string
- `SECRET_KEY`: Flask secret key for sessions
- `POSTGRES_USER`: PostgreSQL username
- `POSTGRES_PASSWORD`: PostgreSQL password
- `POSTGRES_DB`: Database name

## 📚 API Documentation

### Health Check
- **GET** `/api/health` - Check API status

### API Information
- **GET** `/api` - Get API information and available endpoints

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

For support, please create an issue in the repository or contact the development team.

## 🔄 Next Steps

1. Add authentication and authorization
2. Implement user management
3. Add more API endpoints
4. Set up CI/CD pipeline
5. Add comprehensive test coverage
6. Implement caching strategy
7. Add monitoring and logging
