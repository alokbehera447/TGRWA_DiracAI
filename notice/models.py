from django.db import models


from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth import get_user_model
User = get_user_model()

class NoticeBoard(models.Model):
      #creater = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notice_creater')
      noticeTitle = models.CharField(max_length=250 , default="")
      noticeText = models.TextField( null=True,blank=True);
      creationTime = models.DateTimeField(default=timezone.now)
      globalNoticeID = models.CharField(max_length=15)
      noticefile = models.FileField(max_length=255, upload_to='images/', null=True, blank=True, default=None);

      class Meta:
        ordering = ('-creationTime',)
      
      def __str__(self):
        return str(self.id) or "Unnamed"

