#path function
#we need views of app
#we need urlpatterns list

from django.urls import path

from app2 import views

app_name='app2'

urlpatterns=[
    path('playing/',views.Playing,name='playing'),
]