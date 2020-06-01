from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#creating function based views
#request will be in the form of http
#so we have to respond back for the request in the form of http only

def Read(request):
    return HttpResponse('<h1><marquee>Ashu is reading a Novel</marquee></h1>')


def Write(request):
    return HttpResponse('Ashu Is Writing His HomeWork')