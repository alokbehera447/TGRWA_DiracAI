from django.urls import path,re_path


from .views import ListPaginatedNoticesView

urlpatterns = [

path('list-paginated-notices/', ListPaginatedNoticesView.as_view(), name='list_paginated_notices'),

]
