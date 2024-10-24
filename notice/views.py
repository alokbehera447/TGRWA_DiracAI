from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from .models import NoticeBoard
from .serializers import NoticeBoardSerializer 
from rest_framework import pagination
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
User = get_user_model() 
from django.shortcuts import get_object_or_404 
from django.db import models
#from django.core.mail import EmailMultiAlternatives
#from io import BytesIO
#from django.core.files.storage import default_storage
#import mimetypes
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
#try:
#    from reportlab.pdfgen import canvas
#    from reportlab.lib.pagesizes import letter
#except ImportError:
#    import pip
#    pip.main(['install', 'reportlab'])
#    from reportlab.pdfgen import canvas
#    from reportlab.lib.pagesizes import letter
from rest_framework.pagination import PageNumberPagination

# Create your views here.


class NoticeBoardPagination(PageNumberPagination):
    page_size = 20  # Default number of items per page
    page_size_query_param = 'page_size'  # Allow clients to set custom page size via query param
    max_page_size = 100  # Maximum page size



class ListPaginatedNoticesViewOld(generics.ListAPIView):
    queryset = NoticeBoard.objects.all()
    pagination_class = NoticeBoardPagination  # Add this line for pagination
    # permission_classes = [IsAuthenticated]
    serializer_class = NoticeBoardSerializer  # Add this line to specify the serializer

    def get_queryset(self):
        # Order by creationTime in descending order to show the latest notices at the top
        queryset = super().get_queryset().order_by('-creationTime')
        return queryset



class ListPaginatedNoticesView(generics.ListAPIView):
    queryset = NoticeBoard.objects.all()
    pagination_class = NoticeBoardPagination
    serializer_class = NoticeBoardSerializer

    def get_queryset(self):
        # Order by creationTime in descending order to show the latest notices at the top
        queryset = super().get_queryset().order_by('-creationTime')
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        pagination = self.paginator.page.paginator
        
        # Add pagination data
        response.data['total_pages'] = pagination.num_pages
        response.data['total_items'] = pagination.count
        return response









