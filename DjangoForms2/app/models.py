from django.db import models

# Create your models here.

class Topics(models.Model):
    topic_name = models.CharField(max_length=264, primary_key=True)
    
    def __str__(self):
        return self.topic_name
    
class Webpage(models.Model):
    topic_name = models.ForeignKey(Topics, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    
    def __str__(self):
        return self.name