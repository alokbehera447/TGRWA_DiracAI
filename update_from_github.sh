#!/bin/bash
# Quick deployment script - Pull from GitHub and restart

set -e  # Exit on error

echo "🚀 DiracAI Backend - GitHub Deployment"
echo "========================================"
echo ""

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# SSH to server and deploy
echo -e "${YELLOW}Connecting to server...${NC}"
ssh sammy@139.59.77.118 << 'ENDSSH'

set -e

echo "📂 Navigating to project directory..."
cd ~/myprojectdir/TGRWA_DiracAI

echo "📥 Pulling latest changes from GitHub..."
git pull origin main

echo "🔧 Activating virtual environment..."
source myenv/bin/activate

echo "🗄️  Running database migrations..."
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py migrate

echo "📦 Collecting static files..."
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py collectstatic --noinput

echo "🔄 Restarting backend service..."
sudo systemctl restart diracai_backend

echo ""
echo "✅ Deployment complete!"
echo ""
echo "Checking service status..."
sudo systemctl status diracai_backend --no-pager -l

echo ""
echo "🌐 Testing API..."
sleep 3
curl -s https://diracai.com/api/team/ | head -5

ENDSSH

echo ""
echo -e "${GREEN}✅ Deployment successful!${NC}"
echo ""
echo "Your backend has been updated from GitHub and is running."
echo ""

