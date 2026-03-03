from django.db import models

# Create your models here.


class School(models.Model):
    scname = models.CharField(max_length=100)
    scloc = models.CharField(max_length=100)