"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)





urlpatterns = [
    #admin    
    path('admin/', admin.site.urls),

    #home app paths
    path('',include('home.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #path('api/user/', include('users.urls', namespace='users')),

    #account app
    path('account/',include('account.urls')),
    path('api/',include('accountAPIs.urls',namespace='account-api')),
    path('api/onlineregistration/',include('onlineregistration.urls')),

    #tickets app
    #path('api/tickets/',include('tickets.urls')),

    #dashboard app
    #path('dashboardapp/',include('dashboardapp.urls')),

    #all notifications api
    #path('api/allnotification/', include('allnotification.urls')),

    #message app paths
    #path('messageapp/',include('messageapp.urls')),

    #path('api/chat/', include('chat.urls')),

    #path('api/course/',include('course.urls')),

    #path('api/syllabus/',include('syllabus.urls')),

    #path('api/noticeboard/',include('noticeboard.urls')),
    #class app
    #path('api/class/',include('eclass.urls')),

    #path('api/meeting/',include('meeting.urls')),
    #path('api/assignment/', include('assignment.urls')),
    # book app

    #path('api/book/',include('book.urls')),
    #path('api/exam/', include('exam.urls')),


    # teacher app
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

