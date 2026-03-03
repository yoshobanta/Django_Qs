from django.shortcuts import render

# Create your views here.


def filters(request):
    d = {'data' : 'hEllo HoW ArE yOU' , 'c' : 10}
    return render(request,'filters.html',d)