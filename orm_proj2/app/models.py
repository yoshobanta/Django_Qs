from django.db import models

# Create your models here.


class Dept(models.Model):
    dept_no = models.SmallIntegerField(primary_key=True)
    dept_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100,null=True, blank=True)
    
    
    
    
class Emp(models.Model):
    emp_no = models.SmallIntegerField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100, null=True, blank=True)
    mgr = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True) # self-referential foreign key
    hiredate = models.DateField(null=True, blank=True)
    sal = models.IntegerField(null=True, blank=True)
    comm = models.IntegerField(null=True, blank=True) # this is commission field or bonus .
    dept_no = models.ForeignKey(Dept, on_delete=models.CASCADE)   # deptno
    
    
# This an independent salary grade table.
class Salary(models.Model):
    grade = models.SmallIntegerField(primary_key=True, default=1)
    low_sal = models.IntegerField(null=True, blank=True) # This is lower salary for that grade
    high_sal = models.IntegerField(null=True, blank=True) # This is higher salary for that grade



# This is complete individual/indepedent bonus table does not have any relation with emp table    
class Bonus(models.Model):
    ename = models.CharField(max_length=100, null=True, blank=True)
    job = models.CharField(max_length=100, null=True, blank=True)
    sal = models.IntegerField(null=True, blank=True)
