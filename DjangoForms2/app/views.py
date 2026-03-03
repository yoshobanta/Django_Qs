from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse


# Create your views here.

def insert_topic(request):
    ETFO = TopicForm()              #Empty topic form object
    d = {'ETFO' : ETFO}
    
    if request.method == "POST":
        TFDO = TopicForm(request.POST)
        if TFDO.is_valid():
            tn = TFDO.cleaned_data['topicname']   #this if form forms.py not models
            TO,created = Topics.objects.get_or_create(topic_name = tn) 
            # Here we do not need TO we can use create = ..[1] but for readebility we are using it . we can use _ also in stead of TO .
            
            if created :
                return HttpResponse('Topic is created')
            else:
                return HttpResponse('Topic is alredy present')
            
            # TO.save()   Topics.objects.get_or_create this automatically saves no need to save aging
    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO = WebpageForm()
    d = {'EWFO' : EWFO}
    
    if request.method == 'POST':
        WFDO = WebpageForm(request.POST)
        if WFDO.is_valid():
            tn = WFDO.cleaned_data['topicname']
            name = WFDO.cleaned_data['name']
            url = WFDO.cleaned_data['url']
        
            
            TWO,created = Webpage.objects.get_or_create(topic_name = tn , name = name , url = url)
            
            if created :
                return HttpResponse('Webpage is been Created')
            else :
                return HttpResponse('Webpage  been  already Created')

    return render(request,'insert_webpage.html',d)




def insert_topic_mf(request):
    ETMFO = TopicModelForm()
    d = {"ETMFO" : ETMFO}
    
    if request.method == 'POST':
        TMFDO = TopicModelForm(request.POST)
        
        if TMFDO.is_valid():
            TMFDO.save()
            return HttpResponse("Topic through model forms created")
        else :
            return HttpResponse("Invalid")
    return render(request,'insert_topic_mf.html',d)




def insert_webpage_mf(request):
    
    EWMFO = WebpageModelForm()
    d = {'EWMFO' : EWMFO}
    
    if request.method == "POST":
        WMFDO = WebpageModelForm(request.POST)
        if WMFDO.is_valid():
            WMFDO.save()
            return HttpResponse("Webpage is created through model froms")
        else :
            return HttpResponse("Invalid")
    return render(request,'insert_webpage_mf.html',d)
    
