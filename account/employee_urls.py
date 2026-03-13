from django.urls import path
from account.employee_views import (
    EmployeeLoginRequestView,
    EmployeeOTPVerifyView,
    EmployeeLoginView,
    EmployeeRegisterView,
    EmployeeResendOTPView,
)

app_name = 'employee'

urlpatterns = [
    # New OTP-based login flow
    path('login/request/', EmployeeLoginRequestView.as_view(), name='login-request'),
    path('otp/verify/', EmployeeOTPVerifyView.as_view(), name='otp-verify'),
    path('otp/resend/', EmployeeResendOTPView.as_view(), name='otp-resend'),
    
    # Legacy login endpoint (without OTP)
    path('login/', EmployeeLoginView.as_view(), name='login'),
    
    # Registration
    path('register/', EmployeeRegisterView.as_view(), name='register'),
]
