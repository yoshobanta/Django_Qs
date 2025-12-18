from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def captain(request):
    return HttpResponse("Kl Rahul")


def vice_captain(request):
    return HttpResponse("Axar Patel")


