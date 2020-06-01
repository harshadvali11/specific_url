"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
#from app1 import views

#http//127.0.0.1:8000/(suffix)

#as ur connecting specific urls we have import application package directly

import app1
import app2

urlpatterns = [
    path('admin/', admin.site.urls),#app1==admin(no)

    path('app1/',include('app1.urls')),#app1==app1(yes)
    path('app2/',include('app2.urls')),








    #path('read/',views.Read,name='read'),#write==read(no)
    #path('write/',views.Write,name='write'),#write==write(yes)
]
