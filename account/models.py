from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
import datetime
from django.contrib.postgres.fields import ArrayField
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError
from django.utils import timezone
#from django.contrib.auth import get_user_model
#User = get_user_model()



class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError('Users must have an email address')
		if not username:
			raise ValueError('Users must have a username')

		user = self.model(
			email=self.normalize_email(email),
			username=username,
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, username, password):
		user = self.create_user(
			email=self.normalize_email(email),
			password=password,
			username=username,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user





class MyAccountManagerWEmail(BaseUserManager):
        def create_user(self, email, password=None):
                if not email:
                        raise ValueError('Users must have an email address')

                user = self.model(
                        email=self.normalize_email(email),
                        #username=username,
                )

                user.set_password(password)
                user.save(using=self._db)
                return user

        def create_superuser(self, email, password):
                user = self.create_user(
                        email=self.normalize_email(email),
                        password=password,
                        #username=username,
                )
                user.is_admin = True
                user.is_staff = True
                user.is_superuser = True
                user.save(using=self._db)
                return user





class MyAccountManagerWUsername(BaseUserManager):
        def create_user(self,  username, password=None):
                if not username:
                        raise ValueError('Users must have a username')

                user = self.model(
                        username=username,
                )

                user.set_password(password)
                user.save(using=self._db)
                return user

        def create_superuser(self,  username, password):
                user = self.create_user(
                        #email=self.normalize_email(email),
                        password=password,
                        username=username,
                )
                user.is_admin = True
                user.is_staff = True
                user.is_superuser = True
                user.save(using=self._db)
                return user







def get_profile_image_filepath(self, filename):
	return 'profile_images/' + str(self.pk) + '/profile_image.png'

def get_default_profile_image():
	return "codingwithmitch/logo_1080_1080.png"

def get_default_institute_logo():
       return "codingwithmitch/instlogodefault.png"



class UserType(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name


class UserTitle(models.Model):
    name=models.CharField(max_length=25)
    def __str__(self):
        return self.name


class Institute(models.Model):
      dummyoptions = (('yes','YES'),('no','NO'),)
      name = models.CharField(max_length=300,null=True, blank=True);
      city = models.CharField(max_length=300,null=True, blank=True);
      state = models.CharField(max_length=300,null=True, blank=True);
      country = models.CharField(max_length=300,null=True, blank=True);
      instlogo = models.ImageField(max_length=255, upload_to='images/', null=True, blank=True, default=get_default_institute_logo);
      dummy  = models.CharField(max_length=10, choices=dummyoptions, default='no',null=True,blank=True) 
      #def __str__(self):
      #  return "hello"


                
class DegreeName(models.Model):
      name = models.CharField(max_length=300,null=True, blank=True);
      def __str__(self):
        return self.name



class DocumentCopy(models.Model):
      name = models.CharField(max_length=300);
      doc = models.FileField(max_length=255, upload_to='images/', null=True, blank=True);
      def __str__(self):
        return self.name



class MarkSheet(models.Model):
      name = models.CharField(max_length=300,null=True, blank=True);
      doc = models.FileField(max_length=255, upload_to='images/', null=True, blank=True);
      def __str__(self):
        return self.name


class Certificate(models.Model):
      name = models.CharField(max_length=300,null=True, blank=True);
      doc = models.FileField(max_length=255, upload_to='images/', null=True, blank=True);
      def __str__(self):
        return self.name





class EduDegree(models.Model):
      institute = models.ForeignKey(Institute, on_delete=models.CASCADE,null=True, default=None,blank=True);
      degreename = models.ForeignKey(DegreeName, on_delete=models.CASCADE,null=True, default=None,blank=True);
      startDate = models.DateField(default=datetime.date.today,null=True,blank=True);
      endDate = models.DateField(default=datetime.date.today,null=True,blank=True);
      marksheets = models.ManyToManyField(MarkSheet, blank=True,default=None);
      certificates = models.ManyToManyField(Certificate, blank=True, default=None);
      #def __str__(self):
      #  return self.degreename 

      class Meta:
        ordering = ('startDate',)


class Achievements(models.Model):
      name = models.CharField(max_length=300,null=True, blank=True);
      description = models.CharField(max_length=1000,null=True, blank=True);
      startDate = models.DateField(default=datetime.date.today,null=True,blank=True);
      endDate = models.DateField(default=datetime.date.today,null=True,blank=True);
      def __str__(self):
          return str(self.name)



class Address(models.Model):
      addOptions = (('present','PRESENT'),('permanent','PERMANENT'),)
      careof = models.CharField(max_length=200,null=True, blank=True);
      houseno = models.CharField(max_length=100,null=True, blank=True);
      streetno = models.CharField(max_length=200,null=True, blank=True);
      placename = models.CharField(max_length=200,null=True, blank=True);
      postoffice = models.CharField(max_length=200,null=True, blank=True);
      district = models.CharField(max_length=200,null=True, blank=True);
      policestn = models.CharField(max_length=200,null=True, blank=True);
      pincode = models.CharField(max_length=200,null=True, blank=True);
      city = models.CharField(max_length=200,null=True, blank=True);
      state = models.CharField(max_length=200,null=True, blank=True);
      country = models.CharField(max_length=200,null=True, blank=True);
      addressType  = models.CharField(max_length=50, choices=addOptions, default='present',null=True,blank=True);
      def __str__(self):
          return str(self.id)




class UsefullLink(models.Model):
      name = models.CharField(max_length=200, null=True,blank=True)
      link = models.CharField(max_length=1000, null=True,blank=True)
      description = models.CharField(max_length=500, null=True,blank=True)
      creationDateTime = models.DateTimeField(default=timezone.now)
      def __str__(self):
        return self.name
      class Meta:
        ordering = ('creationDateTime',)













class Account(AbstractBaseUser, PermissionsMixin):
    usertitle = models.ForeignKey(UserTitle, on_delete=models.CASCADE,null=True, default=None,blank=True)
    firstname = models.CharField(verbose_name="firstname", max_length=20, unique=False,default="",blank=True)
    lastname = models.CharField(verbose_name="lastname", max_length=20, unique=False,default="",blank=True)
    email = models.EmailField(verbose_name="email", max_length=60, null=True, default=None,blank=True)
    username = models.CharField(max_length=200, unique=True)
    usertype = models.ForeignKey(UserType, on_delete=models.CASCADE,null=True, default=None)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    profile_image = models.ImageField(max_length=255, upload_to='images/', null=True, blank=True, default=get_default_profile_image);
    hide_email = models.BooleanField(default=True);
    registrationid = models.CharField(verbose_name="regid", max_length=60, unique=False,default="");
    gender = models.CharField(verbose_name="gender", max_length=20, unique=False,default="",blank=True); 
    position = models.CharField(verbose_name="position", max_length=20, unique=False,default="",blank=True);
    dateofbirth = models.DateField(verbose_name="dob",max_length=8,unique=False,default=datetime.date.today)
    institute = models.CharField(verbose_name="institute", max_length=20, unique=False,default="",blank=True);
    city = models.CharField(verbose_name="city", max_length=20, unique=False,default="",blank=True);
    state = models.CharField(verbose_name="state", max_length=20, unique=False,default="",blank=True);
    country = models.CharField(verbose_name="country", max_length=20, unique=False,default="",blank=True);
    officeId_doc = models.FileField(max_length=1055, upload_to='images/', null=True, blank=True);#, default=get_default_profile_image);
    govtId1_doc = models.FileField(max_length=1055, upload_to='images/', null=True, blank=True);#, default=get_default_profile_image);
    govtId2_doc = models.FileField(max_length=1055, upload_to='images/', null=True, blank=True);#, default=get_default_profile_image);
    dobCert_doc = models.FileField(max_length=1055, upload_to='images/', null=True, blank=True);#, default=get_default_profile_image);
    educationDegrees = models.ManyToManyField(EduDegree, blank=True);
    contacts = models.ManyToManyField("self", blank=True,symmetrical=False);
    addresses =  models.ManyToManyField(Address, blank=True);
    achievements = models.ManyToManyField(Achievements, blank=True);
    usefull_links = models.ManyToManyField(UsefullLink, blank=True);             



    USERNAME_FIELD = 'username';
    REQUIRED_FIELDS = [];
    objects = MyAccountManagerWUsername()
    def __str__(self):
       return self.username
    def get_profile_image_filename(self):
       return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]
    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
       return self.is_admin
    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
       return True



class FutureCustomerContacts(models.Model):
    name = models.CharField(max_length=100);
    email = models.CharField(max_length=100);
    subject = models.CharField(max_length=100);
    message = models.CharField(max_length=1000);
    postdate = models.DateField(default=datetime.date.today);
    def __str__(self):
        return self.name




class Subscribers(models.Model):
     email = models.CharField(max_length=100);
     postdate = models.DateField(default=datetime.date.today);






