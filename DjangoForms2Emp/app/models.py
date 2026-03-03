from django.db import models

# Create your models here.

class Dept(models.Model):
    dno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=100)
    dloc = models.CharField(max_length=100)
    
    def __str__(self):
        return self.dname
    
class Emp(models.Model):
    eno = models.IntegerField(primary_key=True)
    ename = models.CharField(max_length=100)
    sal = models.IntegerField(null=True,blank=True)
    mgr = models.ForeignKey('self',on_delete=models.SET_NULL , null=True , blank=True)
    dno = models.ForeignKey(Dept,on_delete=models.CASCADE,null=True , blank=True)