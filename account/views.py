from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import login, authenticate,logout
from account.forms import RegistrationForm,RegistrationForm2, AccountAuthenticationForm, ContactForm, RegistrationFormNew
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from account.models import Account
import os
from django.core.files.storage import default_storage
from django.core.files.storage import FileSystemStorage
import json
import base64
from django.core import files
from django.conf import settings

from django.urls import reverse

TEMP_PROFILE_IMAGE_NAME = "temp_profile_image.png"




def getSessionId(request):
    return HttpResponse(request.user.id)

def mail(request):
    send_mail('Registration successful!',"jdsd",'From <edresearch.in@gmail.com>',['bibhu.phy@gmail.com'])
    return HttpResponse('mail sent')


def alreadyAuthenticated(request):
    return render(request,'account/alreadyAthenticated.html')


def register_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            redirectURL=settings.BASE_URL+'/account/alreadyauthenticated'
            return redirect(redirectURL)

        context = {}
        if request.POST:
                form = RegistrationForm(request.POST)
                if form.is_valid():
                        form.save()
                        firstname = form.cleaned_data.get('firstname').lower()
                        lastname = form.cleaned_data.get('lastname').lower()
                        username = form.cleaned_data.get('username')
                        email = form.cleaned_data.get('email').lower()
                        raw_password = form.cleaned_data.get('password1')
                        account = authenticate(email=email, password=raw_password)
                        html_message = render_to_string('account/mail_template.html')
                        plain_message = strip_tags(html_message)
                        send_mail('Registration successful!',plain_message,'From <edresearch.in@gmail.com>',[email],html_message=html_message)
                        #login(request, account)
                        #user.registrationid="123"
                        #registrationid = "ED293872"
                        totalusers = Account.objects.filter().count()
                        currentaccount = Account.objects.get(username=username)
                        regno=1000000 #int(user.id)
                        regid="EDR"+str(regno)
                        currentaccount.registrationid=regid
                        currentaccount.save()
                        os.system("mkdir static/userfiles/%s"%(regid))
                        destination = kwargs.get("next")
                        if destination:
                              return redirect(destination)
                        #registrationsuccess_view(request) 
                        redirectURL=settings.BASE_URL+'/account/registrationsuccess/';
                        return redirect(redirectURL)
                else:
                        context['registration_form'] = form
        else:
                form = RegistrationForm()
                context['registration_form'] = form
        return render(request, 'account/register.html', context)
    

def registrationsuccess_view(request):
    return render(request,"account/successreg.html")


def login_view(request, *args, **kwargs):
    redirectURL=settings.BASE_URL+'/dashboard/general';
    return redirect(redirectURL)



def login_viewOld(request, *args, **kwargs):
        context = {}
        user = request.user
        if user.is_authenticated:
               redirectURL=settings.BASE_URL+'/dashboard/main';              
               return redirect(redirectURL)
                                                               
        destination = get_redirect_if_exists(request)
        #print("destination: " + str(destination))
        
        if request.POST:
                form = AccountAuthenticationForm(request.POST)
                if form.is_valid():
                        email = request.POST['email']
                        password = request.POST['password']
                        user = authenticate(email=email, password=password)
                        if user:
                                login(request, user)
                                if destination:
                                      return redirect(destination)
                                redirectURL=settings.BASE_URL+'/dashboard/main';  
                                return redirect(redirectURL)
                                                                                           
        else:
             form = AccountAuthenticationForm()
                                                                                                                                                       
        context['login_form'] = form

        return render(request, "account/login.html", context)


def get_redirect_if_exists(request):
	redirect = None
	if request.GET:
		if request.GET.get("next"):
			redirect = str(request.GET.get("next"))
	return redirect




def logout_view(request):
        logout(request)
        return redirect("home")



def userprofile_view(request):
        user = request.user
        if user.is_authenticated:
            return render(request,'account/student_userarea_userprofile.html')
        else:
            return redirect('https://edresearch.co.in/account/login')


def requestnewpassword_view(request):
    return render(request,'account/password_reset_email.html')






def employeeregister_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            redirectURL=settings.BASE_URL+'/account/alreadyauthenticated'
            return redirect(redirectURL)

        context = {}
        if request.POST:
                form = RegistrationFormNew(request.POST)
                if form.is_valid():
                        form.save()
                        firstname = form.cleaned_data.get('firstname').lower()
                        lastname = form.cleaned_data.get('lastname').lower()
                        username = form.cleaned_data.get('username')
                        email = form.cleaned_data.get('email').lower()
                        raw_password = form.cleaned_data.get('password1')
                        account = authenticate(email=email, password=raw_password)
                        html_message = render_to_string('account/mail_template.html')
                        plain_message = strip_tags(html_message)
                        send_mail('Registration successful!',plain_message,'From <edresearch.in@gmail.com>',[email],html_message=html_message)
                        #login(request, account)
                        #user.registrationid="123"
                        #registrationid = "ED293872"
                        totalusers = Account.objects.filter().count()
                        currentaccount = Account.objects.get(username=username)
                        regno=1000000 #int(user.id)
                        regid="EDR"+str(regno)
                        currentaccount.registrationid=regid
                        currentaccount.save()
                        os.system("mkdir static/userfiles/%s"%(regid))
                        destination = kwargs.get("next")
                        if destination:
                              return redirect(destination)
                        #registrationsuccess_view(request) 
                        redirectURL=settings.BASE_URL+'/account/registrationsuccess/';
                        return redirect(redirectURL)
                else:
                        context['registration_form'] = form
        else:
                form = RegistrationForm()
                context['registration_form'] = form
        return render(request, 'account/registeremployee.html', context)









def registration_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            redirectURL=settings.BASE_URL+'/account/alreadyauthenticated'
            return redirect(redirectURL)
        #print ("posss")
        context = {}
        if request.POST:
                #print ("Post request")
                form = RegistrationFormNew(request.POST)
                if form.is_valid():
                        form.save()
                        #firstname = form.cleaned_data.get('firstname').lower()
                        #lastname = form.cleaned_data.get('lastname').lower()
                        username = form.cleaned_data.get('username')
                        email = form.cleaned_data.get('email').lower()
                        #raw_password = form.cleaned_data.get('password1')
                        #account = authenticate(email=email, password=raw_password)
                        #html_message = render_to_string('account/mail_template.html')
                        #plain_message = strip_tags(html_message)
                        #send_mail('Registration successful!',plain_message,'From <edresearch.in@gmail.com>',[email],html_message=html_message)
                        #totalusers = Account.objects.filter().count()
                        #currentaccount = Account.objects.get(username=username)
                        #regno=1000000 #int(user.id)
                        #regid="EDR"+str(regno)
                        #currentaccount.registrationid=regid
                        #currentaccount.save()
                        #os.system("mkdir static/userfiles/%s"%(regid))
                        #destination = kwargs.get("next")
                        if destination:
                              return redirect(destination)
                        #registrationsuccess_view(request) 
                        redirectURL=settings.BASE_URL+'/account/registrationsuccess/';
                        return redirect(redirectURL)
                else:
                        context['registration_formnew'] = form
        else:
                form = RegistrationFormNew()
                context['registration_formnew'] = form
        return render(request, 'account/registernew.html', context)









def contactus_view(request, *args, **kwargs):
      context = {}
      if request.POST:
          form = ContactForm(request.POST)
          if form.is_valid():
              form.save()
              #return HttpResponseRedirect(reverse('register_view'))
              destination = kwargs.get("next")
              if destination:
                  return redirect(destination)
              #redirectURL=settings.BASE_URL+'/account/registrationsuccess/';
              #return redirect(redirectURL)
              #return HttpResponseRedirect('/account/registrationsuccess/')
              redirectURL=settings.BASE_URL+'';
              return redirect(redirectURL)
          else:
              context['registration_form'] = form
      else:
          form = ContactForm()
          context['contact_form'] = form
      return render(request,'account/ContactForm.html',context)  


def contact_view(request, *args, **kwargs):
    return render(request,'account/ContactForm.html')





def registration2_view(request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            redirectURL=settings.BASE_URL+'/account/alreadyauthenticated'
            return redirect(redirectURL)

        context = {}
        if request.POST:
                form = RegistrationForm2(request.POST)
                if form.is_valid():
                        form.save()
                        #firstname = form.cleaned_data.get('firstname').lower()
                        #lastname = form.cleaned_data.get('lastname').lower()
                        username = form.cleaned_data.get('username')
                        #email = form.cleaned_data.get('email').lower()
                        #raw_password = form.cleaned_data.get('password1')
                        #account = authenticate(email=email, password=raw_password)
                        #html_message = render_to_string('account/mail_template.html')
                        #plain_message = strip_tags(html_message)
                        #send_mail('Registration successful!',plain_message,'From <edresearch.in@gmail.com>',[email],html_message=html_message)
                        #login(request, account)
                        #user.registrationid="123"
                        #registrationid = "ED293872"
                        #totalusers = Account.objects.filter().count()
                        #currentaccount = Account.objects.get(username=username)
                        #regno=1000000 #int(user.id)
                        #regid="EDR"+str(regno)
                        #currentaccount.registrationid=regid
                        #currentaccount.save()
                        #os.system("mkdir static/userfiles/%s"%(regid))
                        #destination = kwargs.get("next")
                        #if destination:
                        #      return redirect(destination)
                        #registrationsuccess_view(request) 
                        redirectURL=settings.BASE_URL+'/account/registrationsuccess/';
                        return redirect(redirectURL)
                else:
                        context['registration_form'] = form
        else:
                form = RegistrationForm2()
                context['registration_form'] = form
        return render(request, 'account/register2.html', context)





def sendotp_view(request):
    return render(request, 'account/register2.html')



def registrationdone_view(request):
    return render(request, 'account/registration_done.html')


