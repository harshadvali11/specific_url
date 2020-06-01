from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def Playing(request):
    return HttpResponse('Nikky is playing Cricket')