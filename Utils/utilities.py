import random,string
import hashlib
from models.models import *
def link():
  def gen():
    return random.choice(string.ascii_letters) 
  a = ''
  for i in range(10):
    a = a+gen()
  return a
def md5(ciag):
  result = hashlib.md5(ciag.encode()).hexdigest()
  return result
def addStandardResearches(user):
  res1 = Research(name="Economy",level=1,owner=user,cost=10)
  res2 = Research(name="Health",level=1,owner=user,cost=10)
  res1.save()
  res2.save()
def initializeSessionVariables(user,request):
  request.session['login'] = user.login
  request.session['empire_name'] = user.empire_name
  request.session['population'] = user.population
  request.session['money'] = user.money
def sessionAsList(request):
  result = []
  for i in request.session:
    result.append(i)
  return result