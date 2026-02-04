from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def htmlforms(request):
    if request.method =="POST":
        sund = request.POST['un']
        return HttpResponse(sund)
    return render(request,'htmlforms.html')