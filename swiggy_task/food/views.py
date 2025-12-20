from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def food_str(request):
    return HttpResponse("This is food string")

def food(request):
    return render(request,'food.html')
