# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.http import Http404
from django import forms
from django.shortcuts import render
class RegisterForm(forms.Form):
    login = forms.CharField(max_length=20)
    password= forms.CharField(max_length=50)
    email = forms.EmailField()
def register(request):
  template = loader.get_template('register.html')
  if request.method == "POST":
    form = RegisterForm(request.POST)
    if form.is_valid():
      return HttpResponse("Registered")
    else:
      form  = RegisterForm()
  return render(request, 'register.html', {'form':form, })
def index(request):
  return render(request,'index.html',None)
def testView(request):
  return HttpResponse('NOSZ KURNA')