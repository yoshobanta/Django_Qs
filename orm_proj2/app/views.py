from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from django.db.models import Prefetch,F

# Create your views here.



def insert_dept(request):
    dno = int(input('Enter Department No: '))
    CDNO = Dept.objects.filter(dept_no=dno)
    if CDNO :
        return HttpResponse('Department Number Already Exists')
    else:
        dname = input('Enter Department Name: ')
        loc = input('Enter Location (or leave blank): ')
        if loc == '':
            loc = None
        dept = Dept.objects.get_or_create(dept_no=dno, dept_name=dname, location=loc)
        return HttpResponse('Department Inserted')
    
def insert_emp(request):
        ENO = int(input('Enter Employee No: '))           #Type and then Check employe number
        CENO = Emp.objects.filter(emp_no=ENO)
        if CENO :
            return HttpResponse('Employee Number Already Exists')
        else:
            ENAME = input('Enter Employee Name: ')
            JOB = input('Enter Job Title: ')
            MGR = input('Enter Manager No (or leave blank): ')     #Manager can be null
            if MGR:
                MGR = int(MGR)
                mgobj = Emp.objects.get(emp_no=MGR)             # Get the manager object as mgr is foreign key .
            else:
                mgobj = None
            HIREDATE = input('Enter Hire Date (YYYY-MM-DD): ')
            SAL = int(input('Enter Salary: '))
            COMM = input('Enter Commission (or leave blank): ')
            if COMM:
                COMM = int(COMM)
            else:
                COMM = None
            DEPTNO = int(input('Enter Department No: '))        # Dept no is foreign key
            deptobj = Dept.objects.get(dept_no=DEPTNO)          # Get the department object as dept_no is foreign key .
            emp = Emp.objects.get_or_create(emp_no=ENO, emp_name=ENAME, job=JOB, mgr=mgobj, hiredate=HIREDATE, sal=SAL, comm=COMM, dept_no=deptobj)
            return HttpResponse('Employe Inserted')
    

def qsleo(request):
    # Using .all() - makes N+1 queries (1 for Emp + N queries for each related Dept)
    qsleo_all = Emp.objects.all()
    
    # Using .select_related() - makes only 1 query with JOIN (much more efficient)
    qsleo_select = Emp.objects.select_related('dept_no')
    
    d = {
        'qsleo_all': qsleo_all,
        'qsleo_select': qsleo_select
    }
    return render(request,'qsleo.html',d)


def EmpToMgr(request):
    QSLEMO = Emp.objects.select_related('mgr').all()
    QSLEMO = Emp.objects.select_related('mgr').filter(mgr__sal__gte = 500)
    QSLEMO = Emp.objects.select_related('mgr').filter(sal__gte = 500)
    QSLEMO = Emp.objects.select_related('mgr').filter(emp_name = 'yosho')
    QSLEMO = Emp.objects.select_related('mgr').filter(job = 'developer')
    QSLEMO = Emp.objects.select_related('mgr').filter(mgr__job = 'intern')
    QSLEMO = Emp.objects.select_related('mgr').filter(mgr__sal__lt = 5000)
    QSLEMO = Emp.objects.select_related('mgr').filter(mgr__emp_name__icontains = 'sho')
    QSLEMO = Emp.objects.select_related('mgr').filter(mgr__isnull = True)
    QSLEMO = Emp.objects.select_related('mgr').filter(mgr__isnull = False)
    QSLEMO = Emp.objects.select_related('mgr').filter(sal__range = (100, 5000))
    QSLEMO = Emp.objects.select_related('mgr').filter(emp_name__iendswith = 'o')
    QSLEMO = Emp.objects.select_related('mgr').all().order_by('-sal')
    QSLEMO = Emp.objects.select_related('mgr').all().order_by('sal')
    QSLEMO = Emp.objects.select_related('mgr').filter(mgr__emp_name__istartswith = 'y')
    QSLEMO = Emp.objects.select_related('mgr').filter(job__in = ['developer', 'clerk'])
    
    QSLEMO = Emp.objects.select_related('mgr').all()
    
    
    
    
    
    
    avgsal = Emp.objects.select_related('mgr').filter(sal__gt = F('mgr__sal'))
    print(avgsal)
    
    
    avgsal = Emp.objects.select_related('mgr').filter(comm__isnull=False,comm__gt = F('sal'))
    print(avgsal)
    
    
    # first letter of emp name , first letter of emp job .
    q = Emp.objects.select_related()
    
    # emp sal < mgr sal
    avgsal = Emp.objects.select_related('mgr').filter(sal__lt = F('mgr__sal'))
    print(avgsal)
    
    # emp sal = mgr sal
    avgsal = Emp.objects.select_related('mgr').filter(sal__lt = F('mgr__sal'))
    print(avgsal)
    
    # emp comm = mgr comm
    q = Emp.objects.select_related('mgr').filter(comm = F('mgr_comm') )
    print(q)
    
    # emp comm > mgr comm
    q = Emp.objects.select_related('mgr').filter(comm__gt = F('mgr_comm') )
    print(q)
    
    # emp comm < mgr comm
    q = Emp.objects.select_related('mgr').filter(comm__lt = F('mgr_comm') )
    print(q)
    
    
    
    
    d = {'QSLEMO' : QSLEMO}
    return render(request,'EmpToMgr.html' , d)


def EmpToDeptToMgr(request):
    QSLEDMO = Emp.objects.select_related('dept_no','mgr').all()
    
    d = {'QSLEDMO' : QSLEDMO}
    return render(request,'EmpToDeptToMgr.html',d)



# Prefetch_releated we use releated name (Default child table name_set) 
def DeptToEmp(request):
    QSLDEO = Dept.objects.prefetch_related('emp_set').all()
    QSLDEO = Dept.objects.prefetch_related('emp_set').filter(dept_name = 'Sales')
    QSLDEO = Dept.objects.prefetch_related(Prefetch('emp_set',queryset=Emp.objects.filter(sal__gt = 20000)))
    d = {'QSLDEO': QSLDEO}
    return render(request,'DeptToEmp.html' , d)