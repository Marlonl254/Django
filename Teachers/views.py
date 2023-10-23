from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# This is where we'll create all our functions.

def default(request):
    return HttpResponse("This is the default page")

def about(request):
    return HttpResponse("About Emobilis")

def services(request):
    return HttpResponse("This page has our services")