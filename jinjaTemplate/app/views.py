from django.shortcuts import render

# Create your views here.

def jinja_print(request):
    d = {"name":"Yosho","age":23}
    return render(request,'jprint.html',context=d)
