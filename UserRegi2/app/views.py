from django.shortcuts import render
from app.forms import *

# Create your views here.


def Home(request):
    ETMFO = TopicMF()
    EWMFO = WebpageMF()
    d = {'ETMFO' : ETMFO , 'EWMFO' : EWMFO}
    
    if request.method == 'POST' :
        NMTDO = TopicMF(request.POST)
        NMWDO = WebpageMF(request.POST)
        
        if NMTDO.is_valid() and NMWDO.is_valid():
            MTDO = NMTDO.save(commit=False)
            MTDO.save()
            
            MWDO = NMWDO.save(commit=False)
            MWDO.topic_name = MTDO
            MWDO.save()
    return render(request,'Home.html',d)
