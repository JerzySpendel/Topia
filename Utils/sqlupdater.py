from models.models import *
from datetime import datetime
import time
class SessionChecker(object):
  def process_request(self,request):
    pass
class ResourceUpdater(object):
  def process_request(self,request):
    if 'login' in request.session and request.session['login'] != None:
      usr = User.objects.get(login=request.session['login'])
      if usr.last_act:
        now = time.mktime(datetime.now().timetuple())
        date1 = usr.last_act
        date2 = now
        delta = abs(date2-date1)
        usr.money+=(usr.population*delta/usr.tax)
        usr.last_act = now
        usr.population+=(delta/10)
        usr.save()

        request.session['money']=usr.money
        request.session['population'] = int(usr.population)
      else:
        usr.last_act = time.mktime(datetime.now().timetuple)
        usr.save()



