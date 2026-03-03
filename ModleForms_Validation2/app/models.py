

# Create your models here.
from django.db import models

# Create your models here.
from django.core.validators import RegexValidator
from django import forms

def validate_for_k(value):
    if value[0].lower() != "y":
        raise forms.ValidationError('Invalid')

class Topic(models.Model):
    topic_name = models.CharField(max_length=100 , primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile = models.CharField(max_length=100 , validators=[RegexValidator([6-9/d[9]])])
    email = models.EmailField()