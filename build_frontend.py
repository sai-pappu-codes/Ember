#!/usr/bin/env python3
"""
Build script to create the complete Cafe Fausse frontend application
This script creates all necessary React components, pages, and styles
"""

import os
import json

# Base directory for the frontend
BASE_DIR = "/Users/mihai/cafe-fausse/frontend"

# File contents dictionary
files = {
    # Main entry point
    "src/main.jsx": """import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App_cafe.jsx'
import './index.css'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
)""",

    # Main CSS file
    "src/index.css": """/* Global Styles for Cafe Fausse */
:root {
  --primary-color: #8B4513;
  --secondary-color: #D4AF37;
  --dark-bg: #1a1a1a;
  --light-bg: #f5f5f5;
  --text-dark: #333;
  --text-light: #fff;
  --accent: #c9302c;
  --success: #28a745;
  --font-primary: 'Playfair Display', serif;
  --font-secondary: 'Open Sans', sans-serif;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: var(--font-secondary);
  color: var(--text-dark);
  line-height: 1.6;
  background-color: var(--light-bg);
}

h1, h2, h3, h4, h5, h6 {
  font-family: var(--font-primary);
  margin-bottom: 1rem;
  line-height: 1.2;
}

a {
  text-decoration: none;
  color: inherit;
  transition: color 0.3s ease;
}

a:hover {
  color: var(--secondary-color);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
}

.btn {
  display: inline-block;
  padding: 12px 30px;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: all 0.3s ease;
  font-family: var(--font-secondary);
}

.btn:hover {
  background-color: var(--secondary-color);
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0,0,0,0.2);
}

.btn-secondary {
  background-color: transparent;
  border: 2px solid var(--primary-color);
  color: var(--primary-color);
}

.btn-secondary:hover {
  background-color: var(--primary-color);
  color: white;
}

/* Loading Spinner */
.spinner {
  border: 3px solid rgba(0,0,0,0.1);
  border-top-color: var(--primary-color);
  border-radius: 50%;
  width: 40px;
  height: 40px;
  animation: spin 1s linear infinite;
  margin: 20px auto;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Responsive Grid */
.grid {
  display: grid;
  gap: 2rem;
}

.grid-2 {
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
}

.grid-3 {
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

.grid-4 {
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
}

/* Section Styling */
.section {
  padding: 80px 0;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  color: var(--primary-color);
  margin-bottom: 3rem;
}

.section-subtitle {
  text-align: center;
  font-size: 1.2rem;
  color: #666;
  margin-bottom: 2rem;
  font-family: var(--font-secondary);
}

/* Card Styling */
.card {
  background: white;
  border-radius: 10px;
  overflow: hidden;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0,0,0,0.15);
}

.card-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.card-content {
  padding: 1.5rem;
}

.card-title {
  font-size: 1.5rem;
  margin-bottom: 0.5rem;
  color: var(--primary-color);
}

.card-description {
  color: #666;
  margin-bottom: 1rem;
}

.card-price {
  font-size: 1.25rem;
  font-weight: bold;
  color: var(--secondary-color);
}

/* Form Styling */
.form-group {
  margin-bottom: 1.5rem;
}

.form-label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
  color: var(--text-dark);
}

.form-input,
.form-select,
.form-textarea {
  width: 100%;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 5px;
  font-size: 16px;
  transition: border-color 0.3s ease;
}

.form-input:focus,
.form-select:focus,
.form-textarea:focus {
  outline: none;
  border-color: var(--primary-color);
}

.form-textarea {
  resize: vertical;
  min-height: 100px;
}

.form-error {
  color: var(--accent);
  font-size: 14px;
  margin-top: 5px;
}

.form-success {
  color: var(--success);
  font-size: 14px;
  margin-top: 5px;
}

/* Utility Classes */
.text-center { text-align: center; }
.text-left { text-align: left; }
.text-right { text-align: right; }
.mt-1 { margin-top: 0.5rem; }
.mt-2 { margin-top: 1rem; }
.mt-3 { margin-top: 1.5rem; }
.mt-4 { margin-top: 2rem; }
.mb-1 { margin-bottom: 0.5rem; }
.mb-2 { margin-bottom: 1rem; }
.mb-3 { margin-bottom: 1.5rem; }
.mb-4 { margin-bottom: 2rem; }
.p-1 { padding: 0.5rem; }
.p-2 { padding: 1rem; }
.p-3 { padding: 1.5rem; }
.p-4 { padding: 2rem; }

/* Media Queries */
@media (max-width: 768px) {
  .section {
    padding: 60px 0;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .grid-2,
  .grid-3,
  .grid-4 {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 480px) {
  .section {
    padding: 40px 0;
  }
  
  .section-title {
    font-size: 1.75rem;
  }
}""",

    # App-specific CSS
    "src/App_cafe.css": """/* Cafe Fausse App Styles */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700&family=Open+Sans:wght@300;400;600;700&display=swap');

/* Navigation Styles */
.main-nav {
  background-color: var(--dark-bg);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 1000;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo h1 {
  color: var(--secondary-color);
  font-size: 2rem;
  margin: 0;
  font-family: var(--font-primary);
}

.logo .tagline {
  color: var(--text-light);
  font-size: 0.875rem;
  font-family: var(--font-secondary);
  font-style: italic;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.nav-links a {
  color: var(--text-light);
  font-weight: 500;
  transition: color 0.3s ease;
  font-size: 1rem;
}

.nav-links a:hover {
  color: var(--secondary-color);
}

/* Mobile Navigation */
.mobile-menu-toggle {
  display: none;
  background: none;
  border: none;
  color: var(--text-light);
  font-size: 1.5rem;
  cursor: pointer;
}

@media (max-width: 768px) {
  .mobile-menu-toggle {
    display: block;
  }
  
  .nav-links {
    position: fixed;
    top: 70px;
    left: -100%;
    width: 100%;
    height: calc(100vh - 70px);
    background-color: var(--dark-bg);
    flex-direction: column;
    padding: 2rem;
    transition: left 0.3s ease;
  }
  
  .nav-links.active {
    left: 0;
  }
}

/* Footer Styles */
.main-footer {
  background-color: var(--dark-bg);
  color: var(--text-light);
  padding: 3rem 0 1rem;
  margin-top: 80px;
}

.footer-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 20px;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.footer-section h3 {
  color: var(--secondary-color);
  margin-bottom: 1rem;
}

.footer-section p {
  margin-bottom: 0.5rem;
  line-height: 1.8;
}

.footer-bottom {
  text-align: center;
  padding: 2rem 0 1rem;
  margin-top: 2rem;
  border-top: 1px solid rgba(255,255,255,0.1);
  color: rgba(255,255,255,0.6);
}

/* Newsletter Form */
.newsletter-form {
  display: flex;
  gap: 0.5rem;
  margin-top: 1rem;
}

.newsletter-form input {
  flex: 1;
  padding: 10px;
  border: none;
  border-radius: 5px;
}

.newsletter-form button {
  padding: 10px 20px;
  background-color: var(--secondary-color);
  color: var(--dark-bg);
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-weight: 600;
  transition: background-color 0.3s ease;
}

.newsletter-form button:hover {
  background-color: #b8941f;
}

.newsletter-message {
  margin-top: 0.5rem;
  font-size: 0.875rem;
  color: var(--secondary-color);
}

/* Main Content */
.main-content {
  min-height: calc(100vh - 70px);
}

/* Page Transitions */
.page-enter {
  opacity: 0;
  transform: translateY(20px);
}

.page-enter-active {
  opacity: 1;
  transform: translateY(0);
  transition: opacity 300ms, transform 300ms;
}

.page-exit {
  opacity: 1;
}

.page-exit-active {
  opacity: 0;
  transition: opacity 300ms;
}""",
}

# Create files
def create_file(path, content):
    """Create a file with the given content"""
    full_path = os.path.join(BASE_DIR, path)
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, 'w') as f:
        f.write(content)
    print(f"Created: {path}")

# Main execution
if __name__ == "__main__":
    print("Building Cafe Fausse Frontend Application...")
    print("=" * 50)
    
    for file_path, content in files.items():
        create_file(file_path, content)
    
    print("=" * 50)
    print("Frontend foundation created successfully!")
    print("\nNext steps:")
    print("1. Run: cd frontend && npm run dev")
    print("2. Visit: http://localhost:5173")
