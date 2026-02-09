from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from account import views
from .views import LoginView
from .views import BlogAdminViewSet
from .api import (
    AdminDashboardAPI,
    ProjectAPI,
    GalleryAPI, GalleryDetailAPI,
    ProductAPI, ProductGalleryAPI,
    ServiceAPI,
    TestimonialAPI,
    TestimonialDetailAPI,
)
from rest_framework.routers import DefaultRouter
from .views import (
    LoginView,
    TeamMemberViewSet,
    BlogViewSet,
    BlogListAPI,
    BlogDetailAPI,
    BlogCategoryViewSet,
    BlogCategoryAdminViewSet,
    BlogCommentListCreateAPI,
    BlogCommentAdminViewSet,
)


router = DefaultRouter()
router.register(r'team', TeamMemberViewSet , basename='team')
router.register(r'blog', BlogViewSet , basename='blog')
router.register(r'blogs', BlogViewSet , basename='blogs')
router.register(r"admin/blogs", BlogAdminViewSet, basename="admin-blogs")
router.register(r"blog-categories", BlogCategoryViewSet, basename="blog-categories")
router.register(r"admin/blog-categories", BlogCategoryAdminViewSet, basename="admin-blog-categories")
router.register(r"admin/blog-comments", BlogCommentAdminViewSet, basename="admin-blog-comments")
app_name = 'account'

urlpatterns = [
    path("api/blogs/", BlogListAPI.as_view(), name="public-blog-list"),
    path("api/blogs/<slug:slug>/", BlogDetailAPI.as_view(), name="public-blog-detail"),
    path("api/blogs/<slug:slug>/comments/", BlogCommentListCreateAPI.as_view(), name="public-blog-comments"),
    path("api/blogs", BlogListAPI.as_view(), name="public-blog-list-noslash"),
    path("api/blogs/<slug:slug>", BlogDetailAPI.as_view(), name="public-blog-detail-noslash"),
    path("api/blogs/<slug:slug>/comments", BlogCommentListCreateAPI.as_view(), name="public-blog-comments-noslash"),
    
      
    # Testimonials
    path('api/testimonials/', TestimonialAPI.as_view(), name='testimonial-list'),
    path('api/testimonials/<int:pk>/', TestimonialDetailAPI.as_view(), name='testimonial-detail'),

        # Services
    path('api/services/', ServiceAPI.as_view(), name='service-list'),
    path('api/services/<str:pk>/', ServiceAPI.as_view(), name='service-detail'),
    
    # Admin Dashboard
    path('api/admin/dashboard/', AdminDashboardAPI.as_view(), name='admin-dashboard'),
    
    # Projects
    path('api/projects/', ProjectAPI.as_view(), name='project-list'),
    path('api/projects/<int:pk>/', ProjectAPI.as_view(), name='project-detail'),
    
    # Gallery
    path('api/gallery/', GalleryAPI.as_view(), name='gallery-list'),
    path('api/gallery/<int:pk>/', GalleryDetailAPI.as_view(), name='gallery-detail'),
    
    # ✅ PRODUCT ENDPOINTS - These are CRITICAL
    path('api/products/', ProductAPI.as_view(), name='product-list'),
    path('api/products/<int:pk>/', ProductAPI.as_view(), name='product-detail'),
    
    # Product Gallery
    path('api/products/gallery/', ProductGalleryAPI.as_view(), name='product-gallery-list'),
    path('api/products/gallery/<int:gallery_pk>/', ProductGalleryAPI.as_view(), name='product-gallery-detail'),
    path('api/products/<int:product_pk>/gallery/', ProductGalleryAPI.as_view(), name='product-specific-gallery'),

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
    path('api/', include(router.urls)),
] 

# Add static files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
