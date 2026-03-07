#!/bin/bash
# Quick Setup Script for Employee OTP Authentication System
# Run this script in the backend directory after activation venv

echo "==============================================="
echo "Employee OTP Authentication - Quick Setup"
echo "==============================================="
echo ""

# Step 1: Migrate
echo "Step 1: Creating database migrations..."
python manage.py makemigrations account
echo "✓ Migrations created"
echo ""

# Step 2: Apply migrations
echo "Step 2: Applying migrations to database..."
python manage.py migrate account
echo "✓ Migrations applied"
echo ""

# Step 3: Create superuser (if needed)
echo "Step 3: Do you want to create a superuser? (y/n)"
read -r create_superuser
if [ "$create_superuser" = "y" ]; then
    python manage.py createsuperuser
    echo "✓ Superuser created"
else
    echo "Skipping superuser creation"
fi
echo ""

# Step 4: Test API
echo "Step 4: Starting development server..."
echo "Server will run on http://localhost:8000"
echo "Admin panel: http://localhost:8000/admin"
echo ""
echo "Open another terminal and test the API:"
echo ""
echo "curl -X POST http://localhost:8000/api/employee/login/request/ \\"
echo "  -H 'Content-Type: application/json' \\"
echo "  -d '{\"login_id\": \"employee@example.com\", \"password\": \"password123\"}'"
echo ""

python manage.py runserver
