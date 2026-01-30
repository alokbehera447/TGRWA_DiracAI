How to Deploy in Backend Ubuntu Server 

## Prerequisites
- SSH access to production server (sammy@139.59.77.118)
- Local changes committed and tested
- Backend running locally without errors

---

## 📋 Deployment Steps

### Step 1: Test Locally First
Before deploying, ensure everything works locally:

```bash
cd ~/Pictures/diracai_backend/Diracai_Backend_By_Me
source myenv/bin/activate
python manage.py check
python manage.py runserver 0.0.0.0:8000
```

Test endpoints:
- http://127.0.0.1:8000/api/gallery/
- http://127.0.0.1:8000/api/team/
- http://127.0.0.1:8000/admin/

---

### Step 2: Create Deployment Package
// turbo
```bash
cd ~/Pictures/diracai_backend/Diracai_Backend_By_Me
tar -czf /tmp/diracai_backend.tar.gz \
    --exclude='myenv' \
    --exclude='node_modules' \
    --exclude='build' \
    --exclude='*.pyc' \
    --exclude='__pycache__' \
    --exclude='db.sqlite3' \
    --exclude='*.log' \
    --exclude='.git' \
    --exclude='media_cdn' \
    --exclude='static_cdn' \
    .
```

Verify package was created:
```bash
ls -lh /tmp/diracai_backend.tar.gz
```

---

### Step 3: Upload to Production Server
```bash
scp /tmp/diracai_backend.tar.gz sammy@139.59.77.118:/tmp/
```
*Enter password when prompted*

---

### Step 4: SSH into Production Server
```bash
ssh sammy@139.59.77.118
```
*Enter password when prompted*

---

### Step 5: Extract and Deploy (On Production Server)
```bash
cd ~/myprojectdir/TGRWA_DiracAI

# Backup current deployment (optional but recommended)
cp -r myproject myproject_backup_$(date +%Y%m%d_%H%M%S) 2>/dev/null || true

# Extract new files
tar -xzf /tmp/diracai_backend.tar.gz

# Activate virtual environment
source myenv/bin/activate
```

---

### Step 6: Run Migrations (If you have database changes)
```bash
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py migrate
```

---

### Step 7: Collect Static Files (If you have static file changes)
```bash
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py collectstatic --noinput
```

---

### Step 8: Restart Backend Service
```bash
sudo systemctl restart diracai_backend
```

---

### Step 9: Verify Deployment
Check service status:
```bash
sudo systemctl status diracai_backend
```

Test API locally on server:
```bash
curl http://127.0.0.1:8001/api/gallery/
curl http://127.0.0.1:8001/api/team/
```

Test public URLs:
- https://diracai.com/api/gallery/
- https://diracai.com/api/team/
- https://diracai.com/admin/

---

## 🔧 Troubleshooting

### Check Logs
```bash
sudo journalctl -u diracai_backend -n 100 --no-pager
```

### Database Connection Error
If you see "password authentication failed for user diracai":
```bash
sudo -u postgres psql -c "ALTER USER diracai WITH PASSWORD 'diracai';"
```

### Test Django Directly
```bash
cd ~/myprojectdir/TGRWA_DiracAI
source myenv/bin/activate
DJANGO_SETTINGS_MODULE=myproject.settings_production python -c "
import django
django.setup()
from account.models import GalleryItem
print('Gallery items count:', GalleryItem.objects.count())
print('Success!')
"
```

### Restart Nginx (if needed)
```bash
sudo systemctl restart nginx
```

---

## 📁 Important Paths

| Description | Path |
|-------------|------|
| **Local Project** | `~/Pictures/diracai_backend/Diracai_Backend_By_Me` |
| **Production Project** | `/home/sammy/myprojectdir/TGRWA_DiracAI` |
| **Production Settings** | `myproject/settings_production.py` |
| **Nginx Config** | `/etc/nginx/sites-enabled/myproject` |
| **Systemd Service** | `/etc/systemd/system/diracai_backend.service` |

---

## 🌐 Server Details

| Setting | Value |
|---------|-------|
| **Server IP** | 139.59.77.118 |
| **SSH User** | sammy |
| **Domain** | diracai.com |
| **Django Port** | 8001 (Gunicorn) |
| **Frontend Port** | 3001 (Next.js) |
| **Database** | PostgreSQL (myproject / diracai / diracai) |
