# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import  loader
from django import forms
from Utils.utilities import *
from django.shortcuts import *
from datetime import datetime
from index.validators import validate_password
from django.core.mail import send_mail
from models.models import User
from django.views.decorators.cache import cache_page
import time
class RegisterForm(forms.Form):
    login = forms.CharField(max_length=20)
    password= forms.CharField(max_length=50,validators=[validate_password])
    email = forms.EmailField()
class LoginForm(forms.Form):
  login = forms.CharField(max_length=20)
  password = forms.CharField(max_length=50)
@cache_page(100)
def index(request):
  return render(request,'index.html')
@cache_page(100)
def register(request):
  template = loader.get_template('register.html')
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      login = request.POST['login']
      if User.objects.filter(login=login).count() == 0:
        password = md5(str(request.POST['password']))
        email = request.POST['email']
        user = User(tax=10,last_act=time.mktime(datetime.now().timetuple()),login=login,activated=False,pass_md5=password,empire_name='',population=0,reg_date=datetime.now(),money=0,pop_money=10000000)
        code = link()
        user.save()
        addStandardResearches(user)
        activation = Activation(code=code,email=email)
        activation.usr = user
        activation.save()
        print(email)
        activating_link = "212.106.166.37:8000/index/activation/"+code
        send_mail("KURDE NOOOOOO",activating_link,"jspendel@gmail.com",[email],fail_silently=False)
        return HttpResponse("User {0} has been registered, activation code: {1}".format(login,code))
      else:
        return HttpResponse("There is already user with that nickname, sorry.")
  else:
      form = RegisterForm()
  return render(request, 'register.html', {'form':form, })
@cache_page(100)
def login(request):
  if request.method == "POST":
    login = request.POST['login']
    password = md5(request.POST['password'])
    usr = User.objects.get(login=login)
    if usr.pass_md5 == password and usr.activated:
      initializeSessionVariables(usr,request)
      return HttpResponseRedirect('/game/main')
    else:
      return HttpResponse("Niepoprawne haslo badz konto nieaktywowane")
  else:
    return render(request,"login.html",{'form':LoginForm()})
def activation(request,link):
  if len(link)<10:
    return HttpResponse("Wrong link")
  else:
    act = Activation.objects.get(code=link)
    user = act.usr;
    user.activated = True
    user.save()
    act.delete()
    return HttpResponse("User {0} has been activated".format(user.login))
  
  