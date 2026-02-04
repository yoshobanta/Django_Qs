from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.


def insert_topicName(request):
    print("These are existing topics names")
    for to in Topics.objects.all():
        print(to.topic_name)
        
    tn = input("Enter topic name - ")                                    # topic name
    
    CTNP = Topics.objects.filter(topic_name = tn)                        #Check topic name present
    if not CTNP :
        TO = Topics.objects.get_or_create(topic_name = tn )                #Topic Object
        return HttpResponse('New Topic is been added')
    else :
        return HttpResponse('Topic is already there ')
        
    
    
def insert_webpage(request):
    print("The current Topics-Webpage are :")
    # for to,wo in Topics.objects.all() , Webpage.objects.all():
    #     print(f"The Webpage {wo.name} is of {to.topic_name} topic")
    # It will give error better appoach would be to use wo as it have relationship with topics
    
    for wo in Webpage.objects.all():
        print(f"The Webpage {wo.name} is of {wo.topic_name} topic")
    
    wn = input("Enter name of person/webpage - ")
    CWPNP = Webpage.objects.filter(name = wn)                      # Check Webpage name present  or not
    
    # One thing is that there can be 2 same name in Webpage . We have to change it to unique in models
    # Here i will ask the user the webpage if it exist then no need to add if not then we need to add . But we also have to check if that webpage is of which topic .
    
    if not CWPNP :
        tn = input("Enter topic name - ")
        Check_TopicName = Topics.objects.filter(topic_name = tn)
        if Check_TopicName:
            data_name = input('Enter name of the webpage - ')
            data_url = input("Enter name of the url -")
            WPO = Webpage.objects.get_or_create(topic_name = Check_TopicName[0]  , name = data_name , url = data_url)
            return HttpResponse("New webpage added")
        else :
            return HttpResponse('For given webpage suitable topic not exist pls add ')
    
    else :
        return HttpResponse("Webpage already existed")
        
    
    
# Problem with my approach is if i have give unique = True in the models then itna nahi kar na padta .

# So . my approach - ask webpage if present exit if not then ask topic name of this webpage then add .

# Ideal approach - ask topic name first then add webpage .



def insert_accessRecord(request):
    webpage_name = input('Enter webpage name')
    check_webname = Webpage.objects.filter(name = webpage_name)
    
    if not check_webname :
        author_name = print("Author Name")
        for aro in AccessRecord.objects.all():
            print(aro.author)
        if not author_name :
            data_date = print("Enter data")
            aro = AccessRecord.objects(name = webpage_name , author = author_name , date = data_date)
            return HttpResponse('Author Added ')
            
        else :
            return HttpResponse('Author exist')
        
    else:
        return HttpResponse("The Webpage not exits")
    
    
    
    
def display_topics(request):
    QSTO = Topics.objects.all()                           #Query set of List of topic objects
    d = {'QSTO': QSTO}
    return render(request,'display_topics.html', d)


def display_webpages(request):
    QSWO = Webpage.objects.all()
    d = {'QSWO' : QSWO}
    return render(request,'display_webpages.html',d)

def update_webpages(request):
    QSWO = Webpage.objects.all()
    
    # Webpage.objects.filter(name='Virat').update(url='https//virat.in')
    # Webpage.objects.filter(topic_name='Cricket').update(name='Gege')
    # Webpage.objects.filter(topic_name='Cards').update(name='Gege')
    
    #Webpage.objects.update_or_create(topic_name = 'Football' , defaults={'name':'CR9','url' : 'https://cr9.com'})
    
    #Webpage.objects.update_or_create(topic_name = 'Rugb' , defaults={'name':'Hitesh',}) Error as ptc is not present
    
    # Webpage.objects.update_or_create(topic_name = 'Cricket' , defaults={'name':'Hitesh'}) Error multiple objects
    
    # we have to pass object here instead of topic_name .
    
    WO = Webpage.objects.filter(topic_name = 'games')
    # Webpage.objects.update_or_create(name = 'Rdr2', defaults={'topic_name':'Games'})
    Webpage.objects.update_or_create(name = 'Rdr2', defaults={WO:'Games'})
    
    
    
    
    d = {'QSWO' : QSWO}
    return render(request,'display_webpages.html',d)
    

