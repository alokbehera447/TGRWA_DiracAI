from django.shortcuts import render

# Create your views here.

from rest_framework import generics,status
from .serializers import AccountSerializers,UserSerializer, ProfileImageUploadSerializer, CreateAccountWithPhoneSerializer, GetUserFromUserNameSerializer,  InstituteSerializerForSearch
#DashboardNoticeSerializer


from .serializers import CreateOTPAccountWithPhoneSerializer, UserProfileSerializer, OfficeIDUploadSerializer, GovtID1UploadSerializer, GovtID2UploadSerializer, DOBCertUploadSerializer, EduDegreeSerializer, UserSearchSerializer, ContactAddSerializer,EduDegreeCreateSerializer, DegreeNameSerializer, InstituteSerializer, AchievementsSerializer,AddressSerializer, UserSerializerFew


from .serializers import  UseFullLinkSerializer


from account.models import Account, EduDegree, DegreeName, Institute,Achievements, Address,UserType, UsefullLink
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser,IsAuthenticatedOrReadOnly, DjangoModelPermissions, AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser, FormParser
from django.contrib.auth import get_user_model
import requests
from django.http import Http404
from rest_framework import filters
from rest_framework import pagination
#from django_filters import FilterSet, AllValuesFilter

#from django_filters.rest_framework import FilterSet, filters


User = get_user_model()


#authentication_classes = (TokenAuthentication, SessionAuthentication)
#permission_classes = (IsAuthenticated,)


class AccountView(APIView): #ListCreateAPIView
    permission_classes = [IsAuthenticated]
    #parser_classes = [MultiPartParser, FormParser]
    #queryset = Account.objects.all()
    #serializer_class = AccountSerializers
    def get(self, request):
        #context={'request':request}
        serializer = UserSerializer(request.user)
        #print ("-------------------", serializer.context['request'].user)
        return Response(serializer.data)
    def put(self, request):
        print(request.data)
        serializer = UserSerializer(request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserCheckFromUserNameView(APIView):

     def get(self , request, username, format=None):
          #userObj = User.objects.get(username=username);
          #serializer = GetUserFromUserNameSerializer(userObj)
          try:
            user = User.objects.get(username=username) # retrieve the user using username
          except User.DoesNotExist:
               return Response(data={'message':False}) # return false as user does not exist
          else:
            return Response(data={'message':True}) 




class ChangeUserTypeView(APIView):
      def put(self, request, usertypeId):
          userObject = request.user;
          #print ('userObject: ', userObject.usertype);
          userTypeObject=UserType.objects.get(name="Teacher");
          if usertypeId==2:
             userTypeObject=UserType.objects.get(name="Student");
          if usertypeId==1:
              userTypeObject=UserType.objects.get(name="Teacher");
          #print ("user Type Object: ", type(userTypeObject));
          userObject.usertype=userTypeObject;
          userObject.save();
          #print ("userObject.usertype: ",userObject.usertype)

          return Response(data={'message':True})
 



class VerifyCaptchaView(APIView):
    def post(self, request):
        try:
             r = requests.post(
                'https://www.google.com/recaptcha/api/siteverify',
                data={
                'secret': '6LcGJiMlAAAAANc_TZZRTZfvMtyrfwTiaxKh6igX',
                'response': request.data['captcha_value'],
                }
             )
             return Response({'captcha': r.json()})
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class UserProfileGETPUTView(APIView):
    #permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    def put(self, request):
        #print(request.data)
        serializer = UserProfileSerializer(request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContactAddPUTView(APIView):
      permission_classes = [IsAuthenticated]
      def get(self, request):
        serializer = ContactAddSerializer(request.user)
        return Response(serializer.data)
      def put(self, request):
        #print("request.data: ",request.data)
        serializer = ContactAddSerializer(request.user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class ProfileImageUploadAPIView(APIView):
      permission_classes = [IsAuthenticated]
      parser_classes = [MultiPartParser, FormParser]
      def put(self, request, format=None):
          serializer = ProfileImageUploadSerializer(request.user, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status = status.HTTP_200_OK)
          else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# OfficeIDUploadSerializer, GovtID1UploadSerializer, GovtID2UploadSerializer, DOBCertUploadSerializer

class OfficeIDUploadAPIView(APIView):
      permission_classes = [IsAuthenticated]
      parser_classes = [MultiPartParser, FormParser]
      def put(self, request, format=None):
          #print ("office Id doc upload: ", request.data)
          serializer = OfficeIDUploadSerializer(request.user, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status = status.HTTP_200_OK)
          else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GovtID1UploadAPIView(APIView):
      permission_classes = [IsAuthenticated]
      parser_classes = [MultiPartParser, FormParser]
      def put(self, request, format=None):
          serializer = GovtID1UploadSerializer(request.user, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status = status.HTTP_200_OK)
          else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class GovtID2UploadAPIView(APIView):
      permission_classes = [IsAuthenticated]
      parser_classes = [MultiPartParser, FormParser]
      def put(self, request, format=None):
          serializer = GovtID2UploadSerializer(request.user, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status = status.HTTP_200_OK)
          else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DOBCertUploadAPIView(APIView):
      permission_classes = [IsAuthenticated]
      parser_classes = [MultiPartParser, FormParser]
      def put(self, request, format=None):
          serializer = DOBCertUploadSerializer(request.user, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data, status = status.HTTP_200_OK)
          else:
              return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)










class AccountViewwPk(APIView):
    #permission_classes = [IsAuthenticated]    
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        UserObject = self.get_object(pk)
        serializer = UserSerializer(UserObject)
        return Response(serializer.data)




class EduDegreeDeleteView(APIView):
      def get_object(self, pk):
        try:
            return EduDegree.objects.get(pk=pk)
        except EduDegree.DoesNotExist:
            raise Http404

      def delete(self, request, pk, format=None):
        Object = self.get_object(pk)
        Object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 13
    page_size_query_param = 'page_size'
    max_page_size = 100






class UsersView(generics.ListCreateAPIView):
    #permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #pagination_class = StandardResultsSetPagination




class FewUsersView(generics.ListAPIView):#generics.ListAPIView
    permission_classes = [IsAuthenticated]    
    #def get_objects(self, num):
    #    try:
    #        #return User.objects.get(pk=num)
    #        return User.objects.filter(firstname__icontains="b") #order_by("-date_joined")[:10]
    #    except User.DoesNotExist:
    #        raise Http404

    #def get(self, request, num, format=None):
    #    UserObject = self.get_objects(num)
    #    serializer = UserSerializerFew(UserObject)
    #    return Response(serializer.data)

    serializer_class = UserSerializerFew
    def get_queryset(self):
          loggedInUserId = self.request.user.id;
          chatgroups = self.request.user.generalchatgroups;

          print ("loggedInUser: ", loggedInUserId)
          num = self.kwargs['num']
          #return User.objects.order_by("-date_joined")[num:num+10];
          return User.objects.filter(firstname__icontains="b")[num:num+10];
          #return 



class UserSearchView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializerFew
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'firstname','lastname','email']
    pagination_class = StandardResultsSetPagination
        


class InstituteSearchView(generics.ListAPIView):
    queryset = Institute.objects.all().filter(dummy="no")
    serializer_class = InstituteSerializerForSearch
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    pagination_class = StandardResultsSetPagination


class CheckUsedAddedView(APIView):
      def get_object(self, pk):
         try:
            return User.objects.get(pk=pk)
         except User.DoesNotExist:
            raise Http404

      def get(self, request, pk, format=None):
         chatgroups = self.request.user.generalchatgroups.all();
         #print ("chat groups: ", chatgroups)
         userAdded=False;
         groupId=None;
         for group in chatgroups:
            if group.groupType == "oneoone":
                #print ( "OneOOneGroups: ", group.groupuserObjects.all())
                for oneChatgroupuser in group.groupuserObjects.all():
                    #print ("userId: ", oneChatgroupuser.id)
                    if oneChatgroupuser.id == pk:
                       groupId=group.id;
                       userAdded=True
         if userAdded:              
             return Response(data={'exists':True, 'groupId':groupId})
         else:
            return Response(data={'exists':False, 'groupId':groupId})





class AchievementsView(generics.ListCreateAPIView):
      queryset = Achievements.objects.all()
      serializer_class = AchievementsSerializer


class AddressView(generics.ListCreateAPIView):
      queryset = Address.objects.all()
      serializer_class = AddressSerializer



class EduDegreeView(generics.ListCreateAPIView):
      queryset = EduDegree.objects.all()
      serializer_class = EduDegreeSerializer


class EduDegreeCreateView(generics.ListCreateAPIView):
      queryset = EduDegree.objects.all()
      serializer_class = EduDegreeCreateSerializer



class DegreeNamesView(generics.ListCreateAPIView):
      queryset = DegreeName.objects.all()
      serializer_class = DegreeNameSerializer

class InstituteNamesView(generics.ListCreateAPIView):
      queryset = Institute.objects.all()
      serializer_class = InstituteSerializer




class CreateAccountBasicView(generics.ListCreateAPIView):
      queryset = User.objects.all()
      serializer_class = CreateAccountWithPhoneSerializer


      






class CreateOTPAccountWithPhoneView(APIView):
     queryset = User.objects.all()
     serializer_class = CreateOTPAccountWithPhoneSerializer
     
     def put(self, request, username, format=None):
        #print(request.data)
        userObj = User.objects.get(username=username);
        serializer = CreateOTPAccountWithPhoneSerializer(userObj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     def get(self , request, username, format=None):
         userObj = User.objects.get(username=username);
         serializer = CreateOTPAccountWithPhoneSerializer(userObj)
         return Response(serializer.data)









class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)





class SearchUserView(generics.ListAPIView):
      
      serializer_class = UserSearchSerializer
      def get_queryset(self):
          firstname = self.kwargs['speakername']
          return User.objects.filter(firstname__icontains=firstname)



      
      #def get(self, request, *args, **kwargs):
      #    author = kwargs.get('speakername', None)
      #    print ("fffffffffffffffffffffff:  ", author)
      #
      #    userObjects = User.objects.filter(firstname='Bibhuprasad');
      #    serializer = UserSearchSerializer(userObjects)
      #    return Response(serializer.data)
      

class CreateUseFullLinkView(APIView):
      def get_object(self, linkId):
        try:
            return UsefullLink.objects.get(pk=linkId)
        except UsefullLink.DoesNotExist:
            raise Http404

      #def get(self, request, format=None):
      #  loggedInUser = request.user;
      #  usefull_linkObjects = loggedInUser.usefull_links.all();
      #  return usefull_linkObjects

      def post(self, request, format=None):
        serializer = UseFullLinkSerializer(data=request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class LinksPageSetPagination(pagination.PageNumberPagination):
      page_size = 100
      page_size_query_param = 'page_size'
      max_page_size = 500

class GetUseFullLinksView(generics.ListAPIView):
      serializer_class = UseFullLinkSerializer
      pagination_class = LinksPageSetPagination

      def get_queryset(self):
        loggedInUser = self.request.user;
        #courseId = self.kwargs['pk']
        #courseObj=self.get_object(pk=courseId)
        #linkObjs=courseObj.courselinks.all()
        usefull_linkObjects = loggedInUser.usefull_links.all().order_by('id');
        return usefull_linkObjects





class EditDeleteUseFullLinkView(APIView):
      def get_object(self, linkId):
        try:
            return UsefullLink.objects.get(pk=linkId)
        except UsefullLink.DoesNotExist:
            raise Http404

      def get(self, request, linkId, format=None):
        Object = self.get_object(linkId)
        serializer = UseFullLinkSerializer(Object)
        return Response(serializer.data)

      def put(self, request, linkId, format=None):
        Object = self.get_object(linkId)
        serializer = UseFullLinkSerializer(Object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

      def delete(self, request, linkId, format=None):
        linkObject = self.get_object(linkId)
        linkObject.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)












