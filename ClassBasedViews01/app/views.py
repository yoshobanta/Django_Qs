from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.generic import View

from app.forms import *

# string , html page with post and one direct html using TemplateView


def fbv_String(requset):
    return HttpResponse('fbv_String')


class Cbv_String(View):
    def get(self,request):
        return HttpResponse('Cbv_String')
    
    

class Cbv_Html(View):
    def get(self,request):
        return render(request,'Cbv_Html.html')
    
class Cbv_Forms(View):
    def get(self,request):
        ESMFO = SchoolMf()
        d= {'ESMFO' : ESMFO}
        
        return render(request,'Cbv_Forms.html',d)
        