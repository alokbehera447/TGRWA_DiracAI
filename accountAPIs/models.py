from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.

class Zone(models.Model):
    name = models.CharField(max_length=128);
    chatgroup = models.ManyToManyField(User, related_name='zones',blank=True);



#class Cors(models.Model):
#      name = models.CharField(max_length=128)
#      chatgroups = models.ManyToManyField(ChatGroup, related_name='testchatgroups',blank=True);






