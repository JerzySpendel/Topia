from django.conf.urls import patterns,url
from game import views
urlpatterns = patterns('',
url(r'^main/$',views.main),
url(r'^research/$',views.researches)
)