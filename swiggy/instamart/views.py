from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def coffee(request):
    return HttpResponse("Welcome to Insta Coffee Mart!")

def tea(request):
    return HttpResponse("Welcome to Insta Tea Mart!")
