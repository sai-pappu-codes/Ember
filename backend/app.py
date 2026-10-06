from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import random

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql://localhost/ember_dev')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'ember-secret-key-change-in-production')

# Initialize extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)

# Import models after db initialization to avoid circular imports

# Routes
@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({"status": "healthy", "message": "API is running"}), 200

@app.route('/api')
def api_home():
    """API home endpoint"""
    return jsonify({
        "message": "Welcome to the Responsive Web App API",
        "version": "1.0.0",
        "endpoints": {
            "/api/health": "Health check",
            "/api": "API information"
        }
    }), 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
