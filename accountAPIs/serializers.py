from rest_framework import serializers
from account.models import Account, EduDegree, Institute, DegreeName, MarkSheet, Certificate, Achievements, Address, UsefullLink
#from course.models import Course
#from noticeboard.models import NoticeBoard
#from chat.models import ChatGroup


#from rest_framework.permissions import IsAuthenticated
#from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
User = get_user_model()

from accountAPIs.mixins import MessageHandler
import random
from threading import Timer
import requests
from django.core.mail import send_mail




class UserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','firstname', 'lastname','usertype','profile_image')



class GetUserFromUserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')




#from meeting.serializers import MeetingSerializerGET

class GeneralMeetingsSerializer(serializers.ModelSerializer):
      class Meta:
          model =  User
          fields = ('id','generalmeetings')
          depth =1 



class ContactAddSerializer(serializers.ModelSerializer):
    contactId = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['contactId']
    def update(self, instance, validated_data):
        #print ("add contact validated data: ", validated_data)
        userId = validated_data.pop('contactId', None)
        contactObj = User.objects.get(pk=int(userId));
        instance.contacts.add(contactObj);
        instance.save();
        return instance


class AchievementsSerializer(serializers.ModelSerializer):
      userId = serializers.CharField(write_only=True)
      class Meta:
           model = Achievements
           fields = ['id','name','description','startDate','endDate','userId']

      def create(self, validated_data):
        userId = validated_data.pop('userId', None)
        instance = Achievements.objects.create(**validated_data);
        instance.save();
        userObj = User.objects.get(pk=int(userId));
        userObj.achievements.add(instance)
        userObj.save()
        
        return instance


class AddressSerializer(serializers.ModelSerializer):
    userId = serializers.CharField(write_only=True)
    class Meta:
        model = Address
        fields = ['id','userId','careof','houseno','streetno','district','pincode','city','state','country','addressType']
    def create(self, validated_data):
        userId = validated_data.pop('userId', None)
        instance = Address.objects.create(**validated_data);
        instance.save();
        userObj = User.objects.get(pk=int(userId));
        userObj.addresses.add(instance)
        userObj.save()

        return instance






class AccountSerializers(serializers.ModelSerializer):
    class Meta:
        model =  Account
        fields = ('id','firstname', 'lastname','email','username','usertype','profile_image','registrationid')


class ProfileImageUploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','profile_image')



class OfficeIDUploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','officeId_doc')


class GovtID1UploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','govtId1_doc')


class GovtID2UploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','govtId2_doc')



class DOBCertUploadSerializer(serializers.ModelSerializer):
    class Meta:
         model = User
         fields = ('id','dobCert_doc')





#govtId1_doc
#dobCert_doc




from threading import Event

class CreateAccountWithPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','username','usertype')
        model = User

    def create(self, validated_data):
        #Event().wait(5)
        #password = validated_data.pop('password', None)
        
        instance = User.objects.create(**validated_data);
        instance.save();
        fullpassword = "OLsbd!@#45"
        instance.set_password(fullpassword)
        instance.save()
        username = instance.username;
        send_mail('Registration successful! : DiCelpip'," We are glad to welcome you to DiCelpip platform!",'From <dicelpip@gmail.com>',[username])
        #print ("instance password: ", instance.password)
        return instance






def changePasswordAfter(userObj):
    return None;




class CreateOTPAccountWithPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','username')
        model = User

    def update(self, instance, validated_data):
        username=validated_data.pop('username', None)
        username = username.replace(" ", "")
        userObj = User.objects.get(username=username)
        otp = random.randint(10000,99999)
        fullpassword = 'OLsbd!@#45'+ str(otp)
        userObj.set_password(fullpassword)
        userObj.save()
        #mob10digitNum= username[3:]
        #url = "https://www.fast2sms.com/dev/bulkV2"
        #payload = "variables_values={0}&route=otp&numbers={1}".format(otp, mob10digitNum);
        #headers = {
        #  'authorization': "CqDtUWF4wjpv5brzxXPlaOic2IZS6GYkNLdy7hKfJM9A10BguEDiG0mLEcxyKnApUqMaCu7Jl1eRbF9o",
        #  'Content-Type': "application/x-www-form-urlencoded",
        #  'Cache-Control': "no-cache",
        #}
        #response = requests.request("POST", url, data=payload, headers=headers)
        #otpObj = MessageHandler(username,otp)
        #otpObj.send_otp_on_phone()
        print ("usename ------------------------",username)
        #html_message = render_to_string('account/mail_template.html')
        #plain_message = strip_tags(html_message)
        #send_mail('Registration successful!',plain_message,'From <edresearch.in@gmail.com>',[email],html_message=html_message)
        send_mail('OTP : DiCelpip',str(otp),'From <dicelpip@gmail.com>',[username])

        return instance


#classes = ClassSerializer(many=True)


class DegreeNameSerializer(serializers.ModelSerializer):
      class Meta:
          model = DegreeName
          fields = '__all__'

class InstituteSerializer(serializers.ModelSerializer):
      class Meta:
          model = Institute
          fields = '__all__'


class MarkSheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkSheet
        fields = '__all__'



class CertificateSerializer(serializers.ModelSerializer):
      class Meta:
        model = Certificate
        fields = '__all__'



class EduDegreeSerializer(serializers.ModelSerializer):
      institute = InstituteSerializer();
      degreename = DegreeNameSerializer();
      #marksheets = MarkSheetSerializer(many=True);
      #certificates = CertificateSerializer(many=True);
      class Meta:
          model = EduDegree
          fields = ['id','institute','degreename', 'startDate','endDate']

      #def get_institute(self, instance):
      #    return instance.institute.name

      #def get_degreename(self,instance):
      #    return instance.degreename



class EduDegreeCreateSerializer(serializers.ModelSerializer):
    #userId = serializers.SerializerMethodField()
    userId = serializers.CharField(write_only=True)
    institute = serializers.CharField(write_only=True)
    class Meta:
        model = EduDegree
        fields = ['userId','institute','degreename', 'startDate','endDate']

    def create(self, validated_data):
        userid = validated_data.pop('userId', None)
        userInstance = User.objects.get(pk=userid)
        #institute=validated_data['institute']
        institute = validated_data.pop('institute', None);
        instance = EduDegree.objects.create(**validated_data);

        if institute.isdigit():
           instituteObj = Institute.objects.get(pk=institute);
           instance.institute=instituteObj
           instance.save()
        if not institute.isdigit():    
           instData = {"name":institute}
           dummyInstitute=Institute.objects.create(**instData)
           dummyInstitute.dummy = "yes"  
           instance.institute=dummyInstitute
           instance.save()
        print ("institute: ", institute)
        print ("type of institute: ", type(institute))   
        userInstance.educationDegrees.add(instance)
        userInstance.save();
        return instance;


#class DegreeNameSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = DegreeName
#        fields = ['id','name']


#class Institute




#Institute, DegreeName, MarkSheet, Certificate



class ContactSerializer(serializers.ModelSerializer):
     class Meta:
         model = User
         fields = '__all__'

#from rest_framework.fields import CurrentUserDefault


class TeacherSerializer2(serializers.ModelSerializer):
     usertitle = serializers.SerializerMethodField() 
     class Meta:
         fields = ('id', 'username','usertitle', 'firstname','lastname','profile_image')
         model = User
     def get_usertitle(self, instance):
        #userObj = self.context['request'].user
        #print ("user: ", userObj)
        if instance.usertitle is None:
            return None;
        return instance.usertitle.name    







#class CourseEnrollRequestObjectSerializer(serializers.Serializer):
#       usertitle = serializers.SerializerMethodField()


class UserSerializer(serializers.ModelSerializer):
   usertitle = serializers.SerializerMethodField()
   educationDegrees = EduDegreeSerializer(many=True)
   contacts = ContactSerializer(many=True)
   achievements = AchievementsSerializer(many=True)
   addresses = AddressSerializer(many=True)

   class Meta:
      model = User
      fields = ['id','usertitle','firstname', 'lastname','email','username','usertype','profile_image','registrationid','gender','position','dateofbirth','institute','city','state','country','officeId_doc','govtId1_doc','govtId2_doc','dobCert_doc','educationDegrees','contacts','achievements','addresses']
   def get_usertitle(self, instance):
        if instance.usertitle is None:
            return None;
        return instance.usertitle.name


            
class UserProfileSerializer(serializers.ModelSerializer):
      #usertitle = serializers.SerializerMethodField()
      class Meta:
          model = User
          fields = ['id','usertitle','firstname', 'lastname','email','username', 'gender','position','dateofbirth', 'institute','city', 'state','country' ]
      #def get_usertitle(self, instance):
      #  if instance.usertitle is None:
      #      return None;
      #  return instance.usertitle.name






class UserSerializerFew(serializers.ModelSerializer):
      class Meta:
          model = User
          fields = ['id','firstname', 'lastname','username','profile_image','usertype']



class InstituteSerializerForSearch(serializers.ModelSerializer):
      class Meta:
          model = Institute
          fields = ['id','name']

















class CreateUseFullLinkSerializer(serializers.ModelSerializer):
      name = serializers.CharField(write_only=True)
      link = serializers.CharField(write_only=True)
      description = serializers.CharField(write_only=True)
      class Meta:
          fields = ('id','name','link','description')
          model = User

      def update(self, instance, validated_data):
        newLinkObj = CourseLink.objects.create(**validated_data)
        instance.courselinks.add(newLinkObj)
        instance.save()
        return instance


class UseFullLinkSerializer(serializers.ModelSerializer):
      class Meta:
          fields = ('id','name','link','description')
          model = UsefullLink 

      def create(self, validated_data):
          loggedInUser = self.context['request'].user;
          newLinkObj = UsefullLink.objects.create(**validated_data)
          loggedInUser.usefull_links.add(newLinkObj)
          loggedInUser.save();
          return newLinkObj;


