#!/bin/bash

# This script sets up the complete Cafe Fausse frontend application
echo "Setting up Cafe Fausse Frontend..."

# Create necessary directories
mkdir -p frontend/src/pages
mkdir -p frontend/src/components
mkdir -p frontend/src/services
mkdir -p frontend/src/styles
mkdir -p frontend/public/images

# Copy images from Downloads if they exist
if [ -d "/Users/mihai/Downloads/Web Application and Interface Design - Cafe Fausse SRS  - Project nr. 2" ]; then
    echo "Copying images..."
    cp -r "/Users/mihai/Downloads/Web Application and Interface Design - Cafe Fausse SRS  - Project nr. 2"/*.jpg frontend/public/images/ 2>/dev/null || true
    cp -r "/Users/mihai/Downloads/Web Application and Interface Design - Cafe Fausse SRS  - Project nr. 2"/*.png frontend/public/images/ 2>/dev/null || true
    cp -r "/Users/mihai/Downloads/Web Application and Interface Design - Cafe Fausse SRS  - Project nr. 2"/*.jpeg frontend/public/images/ 2>/dev/null || true
fi

echo "Frontend directories created successfully!"
echo "Now run: cd frontend && npm install && npm run dev"
