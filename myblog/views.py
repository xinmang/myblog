from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime

#from .forms import ContactForm
# Create your views here.
#def index(request):
#     return HttpResponse("Hello, World.")
def index(request):
     posts = Post.objects.all()
#     post_lists = []
#     for count,post in enumerate(posts,1):
#          post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
#     return HttpResponse(post_lists)
     now = datetime.now()
     template = get_template('myblog/index.html')
     html = template.render(locals())
     return HttpResponse(html)

def show_post(request,slug):
     template = get_template('myblog/post.html')
     try:
          post = Post.objects.get(slug=slug)
          if post != None:
               html = template.render(locals())
               return HttpResponse(html)
     except:
          return redirect('/')

def search_form(request):
     return render(request,'myblog/search_form.html')
def search(request):
     if request.GET['q'] != '':
          q = request.GET['q']
          posts = Post.objects.filter(title__icontains=q)
          template = get_template('myblog/search_results.html')
          html = template.render(locals())
          return HttpResponse(html)
     else:
          message = 'You submitted an empty form.'
          return HttpResponse(message)

def contact(request):
     form = ContactForm(request.POST)
     template = get_template('myblog/contact_form.html')
     html = template.render(locals())

     return Httpresponse(html)

