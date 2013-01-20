# Create your views here.
from django.shortcuts import *
from models.models import *
from django.views.decorators.cache import cache_page
@cache_page(10)
def main(request):
  return render(request,'main.html',{'session':request.session})
@cache_page(10)
def researches(request):
  usr = User.objects.filter(login=request.session['login'])
  res = Research.objects.filter(owner=usr)
  return render(request,'research.html',{'researches':res})
