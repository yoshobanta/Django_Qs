from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def htmlforms(request):
    if request.method =="POST":
        sund = request.POST['un']
        return HttpResponse(sund)
    return render(request,'htmlforms.html')


def insert_topic(request):
    # To handel when POST is activated
    if request.method == "POST":
        topic = request.POST['topic']
        TTO = Topic.objects.get_or_create(topic_name=topic)   #Topic Table Object (TTO)
        if TTO[1]:
            return HttpResponse('Topic is created')
        else:
            return HttpResponse('Topic is alread present')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    QLTO = Topic.objects.all()
    d = {'QLTO':QLTO}
    if request.method == "POST":
        tn = request.POST['topicname']
        TO = Topic.objects.get( topic_name = tn)
        na = request.POST['name']
        ur = request.POST['url']
        TWO = Webpage.objects.get_or_create(topic_name = TO , name = na , url = ur)
        if TWO[1]:
            return HttpResponse('Topic is created')
        else :
            return HttpResponse("Topic is already present")
    return render(request,'insert_webpage.html',d)


def select_multiple(request):
    QLTO= Topic.objects.all()
    d= {'QLTO':QLTO}
    
    #After post method gets activated after clicking submit .
    if request.method == 'POST':
        LST = request.POST.getlist('topic')                      #List of Selected topics
        print(LST)
        EWQS = Webpage.objects.none()       #Empty Webpage Query Set    we have to declare it as we will get the obj in form of ['Cricket','Football'] .
        for st in LST :
            EWQS = EWQS | Webpage.objects.filter(topic_name = st)
        print(EWQS)
        d1 ={'EWQS' : EWQS}
        return render(request,'display_webpages.html',d1)
    
    return render(request,'select_multiple.html',d)


def checkbox(request):
    QLTO = Topic.objects.all()
    d = {'QLTO' : QLTO}
    return render(request,'checkbox.html',d)



















def insert_dept(request):
    if request.method == 'POST':
        dno = request.POST['dno']
        dn = request.POST['dn']
        dl = request.POST['dl']
        DTO = Dept.objects.get_or_create(deptno=dno,dname = dn , dloc = dl)
        if DTO[1]:
            return HttpResponse("Dept Object is created")
        else:
            return HttpResponse("Dept Object is already present ")
    return render(request,'insert_dept.html')