from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.



def instamart_str(request):
    return HttpResponse("This is instamart string")

def instamart(request):
    return render(request,'instamart.html')
