from django.forms import forms
from django.db import models
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=300,)
    type=models.CharField(max_length=30)
    description=models.CharField(max_length=500)
    tag=models.CharField(max_length=300,blank=True, null=True)








