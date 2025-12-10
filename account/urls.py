from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account import views
from .views import LoginView

from .api import (
    AdminDashboardAPI,
    ProjectAPI,
    GalleryAPI, GalleryDetailAPI,
    ProductAPI, ProductGalleryAPI,
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
    path('api/projects/<int:pk>/', ProjectAPI.as_view(), name='project-detail'),
    path('api/gallery/', GalleryAPI.as_view(), name='gallery-list'),
    path('api/gallery/<int:pk>/', GalleryDetailAPI.as_view(), name='gallery-detail'),
    path('api/contact/submit/', views.contact_api_submission, name='contact_api_submit'),
    
    # Product URLs
    path('api/products/', ProductAPI.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductAPI.as_view(), name='product-detail'),
    
    # ✅ FIXED: Product Gallery URLs - Add the missing endpoints
    path('api/products/gallery/', ProductGalleryAPI.as_view(), name='product-gallery-list'),  # For getting all gallery images
    path('api/products/<int:product_pk>/gallery/', ProductGalleryAPI.as_view(), name='product-gallery-by-product'),  # For product-specific gallery
    path('api/products/gallery/<int:gallery_pk>/', ProductGalleryAPI.as_view(), name='product-gallery-detail'),  # For individual gallery item operations

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