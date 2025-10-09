-- Database initialization script
-- This script runs when the PostgreSQL container is first created

-- Create database if it doesn't exist (optional, as docker-compose creates it)
-- CREATE DATABASE responsive_web_app_dev;

-- Connect to the database
\c responsive_web_app_dev;

-- Create extensions if needed
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Initial schema setup can go here
-- Example: Create a sessions table for user sessions
CREATE TABLE IF NOT EXISTS sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id INTEGER,
    token VARCHAR(255) UNIQUE NOT NULL,
    expires_at TIMESTAMP NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create an index for better performance
CREATE INDEX IF NOT EXISTS idx_sessions_token ON sessions(token);
CREATE INDEX IF NOT EXISTS idx_sessions_expires_at ON sessions(expires_at);

-- You can add more initial setup here as needed
COMMENT ON DATABASE responsive_web_app_dev IS 'Responsive Web Application Development Database';
