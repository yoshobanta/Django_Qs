from django.shortcuts import render
from django.http import HttpResponse

from app.forms import *

# Create your views here.


def contact(request):
    ECFO = ContactForm()
    d = {'ECFO' : ECFO}
    
    # When post is activated by clicking submit
    
    if request.method == "POST":
        CFDO = ContactForm(request.POST)
        if CFDO.is_valid() :
            # return HttpResponse(CFDO.cleaned_data)  this will give nameage
            return HttpResponse(str(CFDO.cleaned_data))
            
        else:
            return HttpResponse('Invalid Data')
    return render(request,'contact.html',d)