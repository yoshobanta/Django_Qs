from django.db import models

# Create your models here.

class Topic(models.Model):
    topic_name = models.CharField(primary_key=True)
    
    def __str__(self):
        return self.topic_name
    
class Webpage(models.Model):
    topic_name = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    
    def __str__(self):             # if we do not use this it will still display [<Webpage: Webpage object (1)>] which is not readable .
        return self.name
    
    
class Dept(models.Model):
    deptno = models.IntegerField(primary_key=True)
    dname = models.CharField(max_length=10,unique=True)
    dloc = models.CharField(max_length=10)
    
    def __str__(self):
        return self.dname
    

