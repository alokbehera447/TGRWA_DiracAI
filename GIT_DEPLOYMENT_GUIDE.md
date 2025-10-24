# Git Deployment Guide - DiracAI Backend

## 🎯 **Problem**
You have code changes in GitHub that need to be deployed to the production server.

## 💡 **Solutions**

---

## ✅ **Option 1: Deploy Directly from GitHub (RECOMMENDED)**

### **One-Time Setup**

```bash
# 1. SSH to server
ssh sammy@139.59.77.118

# 2. Navigate to project directory
cd ~/myprojectdir/TGRWA_DiracAI

# 3. Initialize git (if not already done)
git init

# 4. Add your GitHub repository
git remote add origin https://github.com/YOUR_USERNAME/TGRWA_DiracAI.git

# 5. Fetch all branches
git fetch origin

# 6. Set up main branch tracking
git checkout -b main
git branch --set-upstream-to=origin/main main

# 7. Reset to match GitHub
git reset --hard origin/main
```

### **For Future Deployments**

```bash
# On local machine - just run:
./update_from_github.sh

# OR manually on server:
ssh sammy@139.59.77.118
cd ~/myprojectdir/TGRWA_DiracAI
git pull origin main
source myenv/bin/activate
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py migrate
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py collectstatic --noinput
sudo systemctl restart diracai_backend
```

---

## ✅ **Option 2: Pull Locally, Then Deploy**

### **Steps**

```bash
# 1. On local machine - pull from GitHub
cd /home/tushar/Music/TGRWA_DiracAI
git pull origin main

# 2. Create deployment package
tar -czf /tmp/diracai_backend.tar.gz \
    --exclude='myenv' \
    --exclude='node_modules' \
    --exclude='build' \
    --exclude='*.pyc' \
    --exclude='__pycache__' \
    --exclude='db.sqlite3' \
    --exclude='*.log' \
    --exclude='.git' \
    .

# 3. Upload to server
scp /tmp/diracai_backend.tar.gz sammy@139.59.77.118:/tmp/

# 4. Deploy on server
ssh sammy@139.59.77.118 << 'ENDSSH'
cd ~/myprojectdir/TGRWA_DiracAI
tar -xzf /tmp/diracai_backend.tar.gz
source myenv/bin/activate
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py migrate
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py collectstatic --noinput
sudo systemctl restart diracai_backend
ENDSSH
```

---

## 🔐 **GitHub Authentication**

### **For Public Repositories**
No authentication needed! Just use HTTPS URL:
```bash
git remote add origin https://github.com/YOUR_USERNAME/TGRWA_DiracAI.git
```

### **For Private Repositories**

#### **Method 1: Personal Access Token**

1. **Create Token on GitHub**:
   - Go to: https://github.com/settings/tokens
   - Click "Generate new token (classic)"
   - Select scopes: `repo` (full control)
   - Copy the token (you won't see it again!)

2. **Use Token on Server**:
   ```bash
   # Clone with token
   git clone https://YOUR_TOKEN@github.com/YOUR_USERNAME/TGRWA_DiracAI.git
   
   # Or set remote URL with token
   git remote set-url origin https://YOUR_TOKEN@github.com/YOUR_USERNAME/TGRWA_DiracAI.git
   
   # Pull
   git pull origin main
   ```

#### **Method 2: SSH Keys (More Secure)**

1. **Generate SSH Key on Server**:
   ```bash
   ssh sammy@139.59.77.118
   ssh-keygen -t ed25519 -C "sammy@diracAIwebsiteMachine1"
   # Press Enter for all prompts (default location, no passphrase)
   
   # Display public key
   cat ~/.ssh/id_ed25519.pub
   ```

2. **Add Key to GitHub**:
   - Copy the output from above
   - Go to: https://github.com/settings/ssh/new
   - Paste key and save

3. **Use SSH URL**:
   ```bash
   # Set remote to SSH
   git remote set-url origin git@github.com:YOUR_USERNAME/TGRWA_DiracAI.git
   
   # Test connection
   ssh -T git@github.com
   
   # Pull
   git pull origin main
   ```

---

## 📋 **Complete Setup Instructions**

### **Step 1: Initial Git Setup on Server**

```bash
# SSH to server
ssh sammy@139.59.77.118

# Navigate to project
cd ~/myprojectdir/TGRWA_DiracAI

# Check current status
ls -la .git  # If .git exists, it's already initialized

# Initialize if needed
git init

# Check current remotes
git remote -v

# Add GitHub remote (replace with your repo URL)
git remote add origin https://github.com/YOUR_USERNAME/TGRWA_DiracAI.git

# Fetch repository
git fetch origin

# List branches
git branch -a

# Create and checkout main branch
git checkout -b main

# Set upstream
git branch --set-upstream-to=origin/main main

# Pull latest
git pull origin main
```

### **Step 2: Verify Setup**

```bash
# Check status
git status

# Check remote
git remote -v

# Check branch
git branch

# View recent commits
git log -3
```

### **Step 3: Test Deployment**

```bash
# Pull latest changes
git pull origin main

# Deploy
source myenv/bin/activate
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py migrate
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py collectstatic --noinput
sudo systemctl restart diracai_backend

# Verify
curl https://diracai.com/api/team/
```

---

## 🚀 **Automated Deployment Script**

I've created `update_from_github.sh` for you. Use it like this:

```bash
# On your local machine
cd /home/tushar/Music/TGRWA_DiracAI
./update_from_github.sh
```

It will:
1. ✅ SSH to server
2. ✅ Pull latest code from GitHub
3. ✅ Run migrations
4. ✅ Collect static files
5. ✅ Restart backend service
6. ✅ Test the API

---

## 🔄 **Development Workflow**

### **Recommended Workflow**

```bash
# 1. Make changes locally
cd /home/tushar/Music/TGRWA_DiracAI
# ... edit files ...

# 2. Test locally
source myenv/bin/activate
DJANGO_SETTINGS_MODULE=myproject.settings_local python manage.py runserver

# 3. Commit and push to GitHub
git add .
git commit -m "Your commit message"
git push origin main

# 4. Deploy to production
./update_from_github.sh

# OR manually on server:
ssh sammy@139.59.77.118
cd ~/myprojectdir/TGRWA_DiracAI
git pull origin main
source myenv/bin/activate
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py migrate
DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py collectstatic --noinput
sudo systemctl restart diracai_backend
```

---

## ⚠️ **Important Notes**

### **1. Files to Exclude from Git**
Make sure your `.gitignore` includes:
```
myenv/
*.pyc
__pycache__/
db.sqlite3
*.log
.env
*.sqlite3
media_cdn/
static_cdn/
```

### **2. Environment-Specific Files**
These files should NOT be in Git (contain sensitive info):
- Database credentials
- Secret keys
- API keys
- Environment variables

### **3. Files to Keep in Git**
These files SHOULD be in Git:
- `myproject/settings_production.py`
- `gunicorn_config.py`
- `deployment/` directory
- All Python source code
- `requirements.txt`

---

## 🐛 **Troubleshooting**

### **Problem: Git Not Installed on Server**
```bash
ssh sammy@139.59.77.118
sudo apt update
sudo apt install git
```

### **Problem: Permission Denied**
```bash
# Make sure you have access to the repo
# Check SSH keys or use access token
ssh -T git@github.com
```

### **Problem: Merge Conflicts**
```bash
# On server - discard local changes
cd ~/myprojectdir/TGRWA_DiracAI
git fetch origin
git reset --hard origin/main
```

### **Problem: Wrong Branch**
```bash
# Switch to correct branch
git checkout main
git pull origin main
```

---

## 📊 **Comparison: Git vs SCP**

| Feature | Git Deploy | SCP Deploy |
|---------|-----------|------------|
| Speed | ⚡ Fast (only changes) | 🐌 Slow (entire codebase) |
| Version Control | ✅ Yes | ❌ No |
| Rollback | ✅ Easy (`git reset`) | ❌ Difficult |
| Automation | ✅ Easy | ⚠️ Manual |
| File Size | 📦 Small (diffs only) | 📦 Large (173MB) |
| Best For | ✅ Production | 📝 Initial setup |

**Recommendation**: Use Git for all deployments after initial setup.

---

## 🎯 **Summary**

### **First Time Setup**
1. SSH to server
2. Run `git init` in project directory
3. Add GitHub remote
4. Pull latest code

### **Every Deployment After That**
1. Make changes locally
2. Push to GitHub
3. Run `./update_from_github.sh` OR pull on server
4. Service automatically restarts

---

## 📝 **Quick Commands Reference**

```bash
# Setup (one time)
ssh sammy@139.59.77.118
cd ~/myprojectdir/TGRWA_DiracAI
git init
git remote add origin https://github.com/YOUR_USERNAME/TGRWA_DiracAI.git
git fetch origin
git reset --hard origin/main

# Deploy (every time)
./update_from_github.sh

# Manual deploy
ssh sammy@139.59.77.118 "cd ~/myprojectdir/TGRWA_DiracAI && git pull origin main && source myenv/bin/activate && DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py migrate && DJANGO_SETTINGS_MODULE=myproject.settings_production python manage.py collectstatic --noinput && sudo systemctl restart diracai_backend"

# Check status
ssh sammy@139.59.77.118 "cd ~/myprojectdir/TGRWA_DiracAI && git status"
```

---

**Created**: October 22, 2025  
**Purpose**: Guide for deploying code from GitHub to production server

