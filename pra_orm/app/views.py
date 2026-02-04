from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models import *



def EmpToDept(request):
    # QSLEDO = Emp.objects.select_related('deptno').all()
    
    # # All
    # QSLD = Emp.objects.aggregate(Max('sal'))          # default key name = sal__max
    # print(QSLD)
    
    # QSLD = Emp.objects.aggregate(ms=Max('sal'))       # custom key name = ms
    # print(QSLD)
    # print(QSLD['ms'])
    
    # #Group by
    # QSLEachDept = Emp.objects.values('deptno').annotate(ms=Max('sal'))
    # print(QSLEachDept)
    
    # #Particular
    # QSLEachDept = Emp.objects.values('deptno').annotate(ms=Max('sal')).filter(deptno = 1)
    # print(QSLEachDept)
    
    
    # # Sub-query
    # davgsal = Emp.objects.filter(deptno=1).aggregate(asal=Avg('sal'))
    # avgsal = davgsal['asal']
    # subq = Emp.objects.filter(sal__gt = avgsal)
    # print(davgsal)
    # print(avgsal)
    # print(subq)
    
    
    QSLEDO = Emp.objects.select_related('deptno').all()
    d = {'QSLEDO' : QSLEDO}
    
    return render(request,'EmpToDept.html',d)


def DeptToEmp(request):
    QSLDEO = Dept.objects.prefetch_related('emp_set').all()
    # QSLDEO = Dept.objects.prefetch_related(Prefetch('emp_set' , queryset=Emp.objects.filter(sal__gt = 10000)))
    
    
    
    
    
    d = {'QSLDEO' : QSLDEO}
    return render(request,'DeptToEmp.html',d)
