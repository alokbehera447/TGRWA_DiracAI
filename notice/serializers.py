from rest_framework import serializers
from .models import NoticeBoard
from django.contrib.auth import get_user_model
User = get_user_model()
from django.shortcuts import get_object_or_404
from django.http import QueryDict








class NoticeBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeBoard
        fields = ('id','noticeTitle','noticeText','creationTime','globalNoticeID','noticefile')


