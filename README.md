# Café Fausse - Fine Dining Web Application

A sophisticated, full-stack web application for Café Fausse, an elegant fine-dining restaurant. This project features a React frontend with responsive design, Flask REST API backend, and PostgreSQL database for managing reservations and customer data.

## 🏗️ Architecture

- **Frontend**: React with Vite for fast development and optimal production builds
- **Backend**: Flask REST API with SQLAlchemy ORM
- **Database**: PostgreSQL with Docker containerization
- **Development**: Hot module replacement, CORS enabled, and database migrations

## 📋 Prerequisites

- Node.js (v16 or higher)
- Python 3.8+
- Docker and Docker Compose
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

### 3. Start the database
```bash
docker-compose up -d postgres
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
python app.py
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
- pgAdmin (optional): http://localhost:5050

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
│   └── init.sql        # Initial database setup
├── docker-compose.yml   # Docker services configuration
├── .env.example        # Environment variables template
└── README.md           # This file
```

## 🛠️ Development

### Backend Development

```bash
cd backend
source venv/bin/activate
python app.py
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
# Start PostgreSQL
docker-compose up -d postgres

# Stop PostgreSQL
docker-compose down

# View logs
docker-compose logs postgres

# Access PostgreSQL CLI
docker-compose exec postgres psql -U postgres -d responsive_web_app_dev

# Start pgAdmin (optional)
docker-compose --profile tools up -d pgadmin
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
gunicorn -w 4 -b 0.0.0.0:5000 app:app
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
