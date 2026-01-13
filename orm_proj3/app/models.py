from django.db import models

# Create your models here.


class Country(models.Model):
    country_id = models.SmallIntegerField(unique=True,primary_key=True)
    country_name = models.CharField(max_length=100,unique=True)
    currency = models.IntegerField(unique=True,null=True)
    
class Capital(models.Model):
    capital_id = models.SmallIntegerField(unique=True,primary_key=True)
    capital_name = models.CharField(max_length=100,unique=True)
    country_id = models.OneToOneField(Country,on_delete=models.CASCADE)