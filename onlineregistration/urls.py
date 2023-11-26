from django.urls import path
from .views import CreateOnlineRegistrationView, CreateOnlineRegistrationGenericView, GetOnlineRegistrationView




app_name = 'onlineregistration_api'






urlpatterns = [

path('create/', CreateOnlineRegistrationGenericView.as_view(), name='create_onlineregistration'),

path('get/', GetOnlineRegistrationView.as_view(), name='get_onlineregistration'),


]



























