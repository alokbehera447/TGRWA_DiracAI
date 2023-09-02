from django.db import models

# Create your models here.



def get_default_profile_image():
        return "codingwithmitch/logo_1080_1080.png"


class Registrant(models.Model):
      name = models.CharField(max_length=500, null=True,blank=True);
      photoFile = models.ImageField(max_length=5000, upload_to='images/', null=True, blank=True, default=get_default_profile_image);
      signatureFile = models.ImageField(max_length=5000, upload_to='images/', null=True, blank=True);
      mobileno = models.CharField(max_length=500, null=True,blank=True);
      email = models.CharField(max_length=500, null=True,blank=True);
      address = models.CharField(max_length=500, null=True,blank=True);

      class Meta:
        ordering = ('id',)
