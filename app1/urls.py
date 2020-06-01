#path function
#we need views of app
#we need urlpatterns list

from django.urls import path
from app1 import views

app_name='app1'

urlpatterns=[

    path('read/',views.Read,name='read'),#read==read
    path('write/',views.Write,name='write'),


]
