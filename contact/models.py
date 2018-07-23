from django.db import models
from datetime import datetime


class Company(models.Model):
    name=models.CharField(max_length=100)
    street=models.CharField(max_length=300,null=True)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=200,null=True)
    active_status=models.NullBooleanField()

class Contact(models.Model):
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30, default="None", null=True)
    last_name=models.CharField(max_length=100)
    company=models.ForeignKey(Company,on_delete=models.CASCADE)
    city=models.CharField(default="",max_length=20,blank=True,null=True)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=200)
    mobile_two=models.CharField(max_length=20,default="",blank="",null=True)
    date_added=models.DateTimeField(default=datetime.now(),blank="",null=True)
    has_a_company=models.BooleanField()




