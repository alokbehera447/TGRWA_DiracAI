# Employee OTP Authentication System - Setup Guide

## Overview

This is a complete OTP (One-Time Password) based authentication system for employees. The flow is:
1. Employee enters email/phone + password
2. System validates credentials and sends OTP to email
3. Employee enters OTP
4. System returns JWT tokens for authenticated session

---

## Backend Setup

### Step 1: Create Django Migrations

Run these commands in your Django backend directory:

```bash
cd C:\Users\Oppen\OneDrive\Desktop\Backend\Backend_TGRWA_DiracAI

# Activate virtual environment
venv311\Scripts\activate

# Make migrations
python manage.py makemigrations account

# Apply migrations
python manage.py migrate account
```

### Step 2: Configure Environment Variables

Create or update your `.env` file in the backend root with:

```env
# Email Configuration (Gmail example)
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password  # Use Gmail App Password, not regular password

# Optional: SMS Configuration (Twilio)
TWILIO_ACCOUNT_SID=your_twilio_account_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+1234567890
```

**For Gmail:**
1. Enable 2-factor authentication on your Google account
2. Generate an "App Password" at https://myaccount.google.com/apppasswords
3. Use that password in EMAIL_HOST_PASSWORD

### Step 3: Update Django Settings

In `myproject/settings.py`, add:

```python
# Email Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')

# Installed Apps - Make sure these are in INSTALLED_APPS:
INSTALLED_APPS = [
    # ... other apps
    'rest_framework',
    'rest_framework_simplejwt',
    'account',
    'accountAPIs',
    # ... other apps
]

# JWT Settings
from datetime import timedelta

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(hours=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}
```

### Step 4: Create Admin User (Optional)

```bash
python manage.py createsuperuser
```

### Step 5: Test the Backend

Start the development server:

```bash
python manage.py runserver 0.0.0.0:8000
```

Test the API using curl or Postman:

```bash
# Step 1: Request OTP
curl -X POST http://localhost:8000/api/employee/login/request/ \
  -H "Content-Type: application/json" \
  -d '{
    "login_id": "employee@example.com",
    "password": "employee_password"
  }'

# Response:
{
  "success": true,
  "message": "OTP sent successfully",
  "employee_id": "DI10001",
  "employee_name": "John Doe",
  "phone": "91****5678",
  "email": "employee@example.com",
  "email_sent": true,
  "sms_sent": true,
  "otp_expires_in_minutes": 10
}

# Step 2: Verify OTP
curl -X POST http://localhost:8000/api/employee/otp/verify/ \
  -H "Content-Type: application/json" \
  -d '{
    "employee_id": "DI10001",
    "otp_code": "123456"
  }'

# Response:
{
  "success": true,
  "message": "OTP verified successfully",
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "employee": {
    "id": 1,
    "employee_id": "DI10001",
    "phone": "919876543210",
    "designation": "Full Stack Developer",
    "location": "Bhubaneswar",
    "status": "active"
  }
}
```

---

## Frontend Integration

### API Endpoints

#### 1. Request OTP
```
POST /api/employee/login/request/
Content-Type: application/json

{
  "login_id": "email@company.com or +919876543210",
  "password": "password123"
}

Response:
{
  "success": true,
  "message": "OTP sent successfully",
  "employee_id": "DI10001",
  "employee_name": "John Doe",
  "phone": "91****5678",
  "email": "john@company.com",
  "email_sent": true,
  "sms_sent": true,
  "otp_expires_in_minutes": 10
}
```

#### 2. Verify OTP
```
POST /api/employee/otp/verify/
Content-Type: application/json

{
  "employee_id": "DI10001",
  "otp_code": "123456"
}

Response:
{
  "success": true,
  "message": "OTP verified successfully",
  "access": "JWT_ACCESS_TOKEN",
  "refresh": "JWT_REFRESH_TOKEN",
  "employee": {
    "id": 1,
    "employee_id": "DI10001",
    "phone": "919876543210",
    "designation": "Full Stack Developer",
    "location": "Bhubaneswar",
    "status": "active"
  }
}
```

#### 3. Resend OTP
```
POST /api/employee/otp/resend/
Content-Type: application/json

{
  "employee_id": "DI10001"
}

Response:
{
  "success": true,
  "message": "OTP resent successfully",
  "otp_expires_in_minutes": 10
}
```

#### 4. Employee Registration
```
POST /api/employee/register/
Content-Type: application/json

{
  "name": "Full Name",
  "email": "employee@company.com",
  "phone": "+919876543210",
  "password": "securepassword",
  "location": "Bhubaneswar (optional)",
  "designation": "Full Stack Developer (optional)"
}

Response:
{
  "success": true,
  "message": "Registration successful. Please wait for admin approval.",
  "employee_id": "DI10001",
  "status": "inactive"
}
```

### Frontend Login Flow (Already Implemented in app/login/page.tsx)

The frontend has been updated to show:

**Step 1: Credentials Form**
- Email/Phone input
- Password input (with toggle visibility)
- "Continue to OTP" button

**Step 2: OTP Verification Form**
- Masked phone number (91****5678)
- 6-digit OTP input
- "Verify OTP" button
- "Resend OTP" link
- "Back" link to go back to credentials

---

## Database Models

### EmployeeProfile Model
```python
Fields:
- user (OneToOne→User)
- employee_id (unique, e.g., "DI10001")
- phone (e.g., "+919876543210")
- designation (choice field)
- location (optional)
- status (active/inactive/on_leave)
- created_at, updated_at
```

### OTPVerification Model
```python
Fields:
- employee (ForeignKey→EmployeeProfile)
- otp_code (6-digit string)
- is_verified (boolean)
- created_at
- expires_at
- attempts (for rate limiting)
- max_attempts (default: 3)

Methods:
- is_expired(): Check if OTP is expired
- is_valid(): Check if OTP is still usable
- generate_otp(): Generate random 6-digit OTP
```

---

## Security Features

✅ **OTP Expiration**: OTP expires after 10 minutes

✅ **Rate Limiting**: Max 3 attempts per OTP

✅ **Phone Masking**: Phone is masked in responses (91****5678)

✅ **JWT Tokens**: Secure token-based authentication

✅ **Password Security**: Passwords are hashed using Django's built-in hashing

✅ **Email/SMS OTP**: OTP sent to both email and SMS (configurable)

---

## Admin Interface

After running migrations, you can manage OTPs and employees from Django admin:

```
http://localhost:8000/admin/

Login with superuser credentials, then navigate to:
- Account > Employee Profiles
- Account > OTP Verifications
```

---

## Troubleshooting

### "Module not found: employee_models"
Make sure the `account/employee_models.py` file exists in the correct location.

### "OTP not sending via email"
- Check EMAIL configuration in `.env` and `settings.py`
- Check Gmail "Less secure apps" is enabled (if using Gmail)
- Check server logs for email errors

### "CORS error when calling API"
Add to `settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

### "Employee account is inactive"
Admin needs to approve the employee from Django admin panel.

---

## Next Steps

1. **Email Templates**: Customize OTP email template in `send_otp_via_email()` function
2. **SMS Integration**: Integration Twilio or any SMS provider in `send_otp_via_sms()` function
3. **Two-Factor Auth**: Can be extended for additional security
4. **Session Management**: Implement employee dashboard after login
5. **Brute Force Protection**: Add IP-based rate limiting

---

## Support

For issues or questions, check:
- Backend logs: `python manage.py runserver` output
- Django admin panel: Debug models and records
- Frontend console: Browser DevTools → Console tab
