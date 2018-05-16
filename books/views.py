from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def current_datetime(request):
     now = datetime.now()
     html = "<html><body>It is now %s.</body></html>"%now
     return HttpResponse(html)

def show_time(request,offset):
     offset=int(offset)
     dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
     html = "<html><body>In %s hour(s), time is %s.</body></html>"%(offset,dt)
     return HttpResponse(html)

def add(request):
     a=request.GET['a']
     b=request.GET['b']
     c=int(a)+int(b)
     return HttpResponse(str(c))
def add2(request,a,b):
     c=int(a)+int(b)
     return HttpResponse(str(c))

def index(request):
     return render(request,'books/home.html')
