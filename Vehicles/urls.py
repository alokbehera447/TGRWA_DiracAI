from django.urls import path
from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

#DashboardNoticesView

app_name= 'accountAPIs'

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)




urlpatterns = [
        path('search-vehicle/', views.VehiclePermitSearchAPIView.as_view(), name='search-vehicle'),

        path('vehicle-permits/', views.VehiclePermitList.as_view(), name='vehicle-permit-list'),  # List and Create
        path('vehicle-permits/<int:pk>/', views.VehiclePermitDetail.as_view(), name='vehicle-permit-detail'),  # Retrieve, Update, Delete
]

urlpatterns = format_suffix_patterns(urlpatterns)




