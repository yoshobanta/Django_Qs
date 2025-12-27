from django.shortcuts import render

# Create your views here.


def ifBlock(request):
    d = {
        "name":"yosho",
        "age" : 23
    }
    d1= {
        "name":"y",
        "age" : 18,
        "number":986100000
    }
    return render(request,"ifBlock.html",d1)  #pass the dictionary.
