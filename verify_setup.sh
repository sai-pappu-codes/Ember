#!/bin/bash

echo "========================================="
echo "   CAFE FAUSSE - SYSTEM VERIFICATION"
echo "========================================="
echo ""

# Check Frontend
echo "1. FRONTEND STATUS:"
if lsof -i :5173 > /dev/null 2>&1; then
    echo "   ✅ Frontend is running on http://localhost:5173"
else
    echo "   ❌ Frontend is NOT running"
    echo "   To start: cd frontend && npm run dev"
fi

# Check Backend
echo ""
echo "2. BACKEND STATUS:"
if lsof -i :5000 > /dev/null 2>&1; then
    echo "   ✅ Backend is running on http://localhost:5000"
else
    echo "   ❌ Backend is NOT running"
    echo "   To start: cd backend && source venv/bin/activate && python3 app_cafe.py"
fi

# Check PostgreSQL
echo ""
echo "3. DATABASE STATUS:"
if pg_isready -d cafe_fausse_dev > /dev/null 2>&1; then
    echo "   ✅ PostgreSQL is running and cafe_fausse_dev is accessible"
    
    # Count records
    CUSTOMERS=$(psql -d cafe_fausse_dev -t -c "SELECT COUNT(*) FROM customers;" 2>/dev/null | xargs)
    RESERVATIONS=$(psql -d cafe_fausse_dev -t -c "SELECT COUNT(*) FROM reservations;" 2>/dev/null | xargs)
    
    echo "   📊 Data in database:"
    echo "      - Customers: $CUSTOMERS"
    echo "      - Reservations: $RESERVATIONS"
else
    echo "   ❌ Database is NOT accessible"
    echo "   To create: createdb cafe_fausse_dev"
fi

# Test API
echo ""
echo "4. API TEST:"
if curl -s http://localhost:5000/api/health > /dev/null 2>&1; then
    echo "   ✅ API is responding correctly"
else
    echo "   ❌ API is not responding"
fi

echo ""
echo "========================================="
echo "   QUICK ACCESS LINKS:"
echo "========================================="
echo "   🌐 Frontend: http://localhost:5173"
echo "   🔧 Backend API: http://localhost:5000/api"
echo "   📊 pgAdmin: Open from Applications folder"
echo ""
echo "========================================="
