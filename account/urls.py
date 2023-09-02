from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from account import views

from django.contrib.auth import views as auth_views



from account.views import (
    register_view,login_view,logout_view,
    userprofile_view,requestnewpassword_view,
    registrationsuccess_view, employeeregister_view, 
    contactus_view, contact_view, registration_view, registration2_view, sendotp_view, registrationdone_view
)



app_name = 'account'


urlpatterns = [


path('alreadyauthenticated/',views.alreadyAuthenticated,name="alreadyAuthenticated"),

path("mail",views.mail,name='mail'),

path('register/', register_view, name="register"),


path('registration/', registration2_view, name="registration"),



path('registrationdone/',registrationdone_view, name="registrationdone"),


path('sendotp/',sendotp_view,name="send_otp"),



path('registeremployee/',employeeregister_view, name="registeremployee"),


path('contactus/',contact_view,name="contactusview"),


path('registrationsuccess/', registrationsuccess_view, name="registersuccess"),
path('login/', login_view, name="login"),
path('logout/', logout_view, name="logout"),
path('requestnewpassword/',requestnewpassword_view,name="requestnewpassword"),

#path('userprofile/',userprofile_view,name="userprofile"),

# Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)

#path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), 
#        name='password_change_done'),

#path('password_change/', auth_views.PasswordChangeView.as_view(template_name='account/newTest/password_change.html'), name='password_change'),



path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_done.html'),
     name='password_reset_done'),

#path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'), name='password_reset_confirm'),

 path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),


path('password_reset/', auth_views.PasswordResetView.as_view(template_name='account/password_reset_form.html'), name='password_reset'), 


path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),name='password_reset_complete'),



#path('<user_id>/', account_view, name="view"),
#path('<user_id>/edit/', edit_account_view, name="edit"),
#path('<user_id>/edit/cropImage/', crop_image, name="crop_image"),










]





if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




