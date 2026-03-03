from django.shortcuts import render
from app.forms import *

# Create your views here.


def insert_dept(request):
    EDFO = DeptForm()        #Empty Dept Form object
    d = {'EDFO':EDFO}
    return render(request,'insert_dept.html',d)