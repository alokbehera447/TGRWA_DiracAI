from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,HttpResponse, redirect
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.conf import settings
from django.http import HttpResponseNotFound
from django.template import TemplateDoesNotExist
from pathlib import Path



from django.http import HttpResponseRedirect
#reactapp=never_cache(TemplateView.as_view(template_name="index.html"))

def reactapp(request):
        try:
            return render(request, "index.html")
        except TemplateDoesNotExist:
            base_dir = Path(getattr(settings, "BASE_DIR", Path(__file__).resolve().parent.parent))
            for candidate in (base_dir / "build" / "index.html", base_dir / "public" / "index.html"):
                if candidate.exists():
                    content = candidate.read_text(encoding="utf-8", errors="ignore")
                    if "%PUBLIC_URL%" in content:
                        content = content.replace("%PUBLIC_URL%", "")
                    return HttpResponse(content)
            return HttpResponseNotFound("index.html not found")



def reactappPar(request,pk):
    return reactapp(request)


def reactappPkGk(request,gk, pk):
    return reactapp(request)



def reactappvideomeet(request,meetingroomstring):
    return reactapp(request)


#        user = request.user
#        if user.is_authenticated:
#            return render(request,'index.html')
#        else:
#            redirectURL=settings.BASE_URL+'/account/login';
#            return redirect(redirectURL)





def index(request):
    return render(request, 'djangoIndex.html')


def newindex(request,  *args, **kwargs):
    return render(request, 'djangoIndex1.html')
    #return HttpResponseNotFound(" Page not found ")





def newindexteam(request):
    return render(request, 'djangoIndex1Team.html')











def privacypolicy(request):
    return render(request, 'privacypolicy.html')


def joinus(request):
    return render(request,'joinus.html') 

def joinusscienceanalystI(request):
    return render(request,'scienceanalystI.html')

def joinusscienceanalystII(request):
        return render(request,'scienceanalystII.html')



def bibhutiparida(request):
    return render(request,'BibhutiParida.html');

def rasmitasahoo(request):
    return render(request,'RasmitaSahoo.html');

def bibhuprasadmahakud(request):
    return render(request,'BibhuprasadMahakud.html');

def ipsitpanda(request):
    return render(request,'IpsitPanda.html');


def jackysingla(request):
    return render(request,'JackySingla.html');

def reetasingla(request):
    return render(request,'ReetaSingla.html');


def kiran(request):
    return render(request,'Kiran.html');



def debaprasadmahakud(request):
    return render(request,'DebaprasadMahakud.html');


def demoteacher(request):
    return render(request,'DemoTeacher.html');


def demostudent(request):
    return render(request,'DemoStudent.html');


def demomanager(request):
    return render(request,'DemoManager.html');


def demoinstitute(request):
    return render(request,'DemoInstitute.html');

def careeredr(request):
    return render(request,'CarrerEDResearch.html');


def applyjob(request):
    return redirect('https://docs.google.com/forms/d/e/1FAIpQLSfNsVaYUiI9uG3wicTVmPAA_8L2VeGHMnAlp5cDmKxH0Dps3A/viewform');







