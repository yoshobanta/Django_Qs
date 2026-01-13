from django.db import models

# Create your models here.

class Topics(models.Model):
    topic_name = models.CharField(max_length=264, primary_key=True)
    
    def __str__(self):                # if we do not use this it will still display topic_name as it is primary key
        return self.topic_name
    
class Webpage(models.Model):
    topic_name = models.ForeignKey(Topics, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    
    def __str__(self):             # if we do not use this it will still display [<Webpage: Webpage object (1)>] which is not readable .
        return self.name
    

class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage,on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    date = models.DateField()
    
    def __str__(self):
        return self.author
    
    
    
