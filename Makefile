.PHONY: help install setup-backend setup-frontend db-start db-stop backend frontend build clean test

help: ## Show this help message
	@echo "Usage: make [target]"
	@echo ""
	@echo "Available targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  %-20s %s\n", $$1, $$2}'

install: setup-backend setup-frontend ## Install all dependencies

setup-backend: ## Set up Python backend
	cd backend && python -m venv venv
	cd backend && . venv/bin/activate && pip install -r requirements.txt
	@echo "Backend setup complete. Activate with: source backend/venv/bin/activate"

setup-frontend: ## Set up React frontend
	cd frontend && npm install
	@echo "Frontend setup complete"

db-start: ## Ensure local PostgreSQL database exists
	@createdb cafe_fausse_dev 2>/dev/null || echo "Database cafe_fausse_dev already exists"
	@echo "Ensure your local PostgreSQL service is running (e.g., brew services start postgresql@16 or use Postgres.app)"

db-stop: ## Stop PostgreSQL database (local install)
	@echo "Stop your local PostgreSQL service via your OS tooling (e.g., brew services stop postgresql@16)"

db-migrate: ## Run database migrations
	cd backend && . venv/bin/activate && flask db upgrade
	@echo "Database migrations complete"

backend: ## Run Flask backend
	cd backend && . venv/bin/activate && python app_cafe.py

frontend: ## Run React frontend
	cd frontend && npm run dev

build: ## Build frontend for production
	cd frontend && npm run build
	@echo "Frontend built in frontend/dist"


clean: ## Clean generated files
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf backend/venv
	rm -rf frontend/node_modules
	rm -rf frontend/dist
	@echo "Cleaned all generated files"

dev: ## Start development environment (database + backend + frontend)
	@echo "Starting development environment..."
	@make db-start
	@echo "Starting backend and frontend (in separate terminals)..."
	@echo "Run 'make backend' in one terminal"
	@echo "Run 'make frontend' in another terminal"
