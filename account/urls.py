from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account import views
from .views import LoginView
from .api import (
    AdminDashboardAPI,
    ProjectAPI, ProjectDetailAPI,
    GalleryAPI, GalleryDetailAPI,
)
from rest_framework.routers import DefaultRouter
from .views import TeamMemberViewSet

router = DefaultRouter()
router.register(r'team', TeamMemberViewSet)

app_name = 'account'

urlpatterns = [
    # -------- API ENDPOINTS --------
    path('api/admin/dashboard/', AdminDashboardAPI.as_view(), name='admin-dashboard'),
    
    # Include router URLs under /api/
    path('api/', include(router.urls)),
    
    path('api/projects/', ProjectAPI.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectDetailAPI.as_view(), name='project-detail'),
    path('api/gallery/', GalleryAPI.as_view(), name='gallery-list'),
    path('api/gallery/<int:pk>/', GalleryDetailAPI.as_view(), name='gallery-detail'),

    # -------- REGULAR ACCOUNT VIEWS --------
    path('alreadyauthenticated/', views.alreadyAuthenticated, name="alreadyAuthenticated"),
    path("mail", views.mail, name='mail'),
    path('register/', views.register_view, name="register"),
    path('registration/', views.registration2_view, name="registration"),
    path('registrationdone/', views.registrationdone_view, name="registrationdone"),
    path('login/', views.login_view, name="login"),
    path('sendotp/', views.sendotp_view, name="send_otp"),
    path('registeremployee/', views.employeeregister_view, name="registeremployee"),
    path('contactus/', views.contact_view, name="contactusview"),
    path('registrationsuccess/', views.registrationsuccess_view, name="registersuccess"),
    path('logout/', views.logout_view, name="logout"),
    path('requestnewpassword/', views.requestnewpassword_view, name="requestnewpassword"),

    path('password_reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'),
         name='password_reset'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name='password_reset_complete'),

    path('api/login/', LoginView.as_view(), name='login'),
] 

# Add static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)