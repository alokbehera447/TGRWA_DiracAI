from django.urls import path
from .views import AccountView,AccountViewwPk,BlacklistTokenUpdateView,UsersView, ProfileImageUploadAPIView, CreateAccountBasicView, UserCheckFromUserNameView,  ChangeUserTypeView,InstituteSearchView


from .views import CreateOTPAccountWithPhoneView, UserProfileGETPUTView, OfficeIDUploadAPIView, GovtID1UploadAPIView, GovtID2UploadAPIView, DOBCertUploadAPIView, EduDegreeView, SearchUserView, ContactAddPUTView, EduDegreeCreateView, DegreeNamesView, InstituteNamesView, EduDegreeDeleteView,AchievementsView, AddressView, VerifyCaptchaView, FewUsersView, UserSearchView


from .views import  CreateUseFullLinkView, GetUseFullLinksView, EditDeleteUseFullLinkView







from django.conf.urls import include, url
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


#DashboardNoticesView

app_name= 'accountAPIs'

#router = routers.DefaultRouter()
#router.register(r'users', UserViewSet)
#router.register(r'groups', GroupViewSet)




urlpatterns = [

        path('', AccountView.as_view()),
        path('<int:pk>/',AccountViewwPk.as_view()),
        path('logout/blacklist/',  BlacklistTokenUpdateView.as_view(),name='blacklist'),
        path('allusers/',UsersView.as_view()),
        path('fewusers/<int:num>/',FewUsersView.as_view()),

        path('usersearch/',UserSearchView.as_view()),

        path('institutesearch/',InstituteSearchView.as_view()),

        
        path('profileimageupload/',ProfileImageUploadAPIView.as_view()),

        path('officeidupload/', OfficeIDUploadAPIView.as_view()),
        path('govtid1upload/', GovtID1UploadAPIView.as_view()),
        path('govtid2upload/', GovtID2UploadAPIView.as_view()),
        path('dobcertupload/', DOBCertUploadAPIView.as_view()),

        path('edudegreecreate/', EduDegreeCreateView.as_view()),

        path('edudegreedelete/<int:pk>/', EduDegreeDeleteView.as_view()),

        path('degreenames/', DegreeNamesView.as_view()),

        path('institutenames/', InstituteNamesView.as_view()),


        #path('sendotpforfirsttime/', SendOTPfirsttimeView().as_view()),

        path('createaccountwithphonenum/',CreateAccountBasicView.as_view()),



        path('setotpaspswd/<username>/',CreateOTPAccountWithPhoneView.as_view()),


        path('getuserfromusername/<username>', UserCheckFromUserNameView.as_view()),

        path('userprofilegetput/',UserProfileGETPUTView.as_view()),


        path('searchusersstr/<str:speakername>/',SearchUserView.as_view()),

        path('addcontact/',ContactAddPUTView.as_view(),name='addcontact_view'),


        path('createachievement/',AchievementsView.as_view()),

        path('addnewaddress/', AddressView.as_view()),
        

        path('verifycaptcha/',VerifyCaptchaView.as_view()),



        path('changeusertype/<int:usertypeId>/', ChangeUserTypeView.as_view(),name="changeUsertype_view"),

 
        path('createusefulllink/', CreateUseFullLinkView.as_view(), name="create_personal_link"),
        path('getusefulllinks/', GetUseFullLinksView.as_view(),name="personal_useful_links"),
     
        path('editdeletelink/<int:linkId>/',EditDeleteUseFullLinkView.as_view(), name="create_usefull_link"),
        #path('deletelink/<int:linkId>/', EditDeleteUseFullLinkView.as_view(),name="delete_usefull_link"),


]

urlpatterns = format_suffix_patterns(urlpatterns)




