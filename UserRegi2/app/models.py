from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(primary_key=True,max_length=100)
    

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField()
    
    def __str__(self):
        return self.name