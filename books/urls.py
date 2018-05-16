from django.conf.urls import url

from . import views

urlpatterns = [
     url(r'^$', views.index, name='index'),
     url(r'^(\d[1,2])/$', views.show_time, name='show_time'),
     url(r'^add/$', views.add, name='add'),
     url(r'^add/(\d+)/(\d+)/$', views.add2, name='add2'),
     ]
