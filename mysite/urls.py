"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
'''
from django.conf.urls import url,include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('myblog.urls')),
    url(r'^polls', include('polls.urls')),
]
'''
from django.conf.urls import url, include
from django.contrib import admin

from myblog import views


# 需要先导入对应app的views
urlpatterns = [
    # 参数第一部分为url的正则表达式，后面的是业务逻辑函数
    
    # admin后台路由
    url(r'^admin/', admin.site.urls),
    url(r'^myblog/', include('myblog.urls')),
    url(r'^books/', include('books.urls')),
]
