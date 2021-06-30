from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return HttpResponse("<h1> Homepage </h1>")

def siteInformation(request):
    return HttpResponse("<h1> This is the information about my blog </h1>")