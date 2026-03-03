from django.shortcuts import render


# Create your views here.

from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO = TopicForms()                    #Empty
    d = {'ETFO' : ETFO}
    
    if request.method == "POST":
        TFDO = TopicForms(request.POST)   #with data
        if TFDO.is_valid() :
            TFDO.save()
            return HttpResponse('Created')
        else:
            return HttpResponse('Invalid')
    
    return render(request,'insert_topic.html',d)