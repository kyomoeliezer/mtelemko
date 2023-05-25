from django.db import models
from datetime import datetime
from user.models import User


class Company(models.Model):
    name=models.CharField(max_length=100)
    street=models.CharField(max_length=300,null=True)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=200,null=True)
    active_status=models.NullBooleanField()
    user=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='company_user')

class Contact(models.Model):
    first_name=models.CharField(max_length=30)
    middle_name=models.CharField(max_length=30, default="None", null=True)
    last_name=models.CharField(max_length=100)
    company=models.CharField(max_length=30, default="None", null=True)#models.ForeignKey(Company,on_delete=models.CASCADE)
    city=models.CharField(default="",max_length=20,blank=True,null=True)
    mobile=models.CharField(max_length=20)
    email=models.EmailField(max_length=200)
    mobile_two=models.CharField(max_length=20,default="",blank="",null=True)
    address=models.CharField(max_length=200,null=True)
    date_added=models.DateTimeField(auto_now_add=True,blank="",null=True)
    city=models.CharField(max_length=100,default=None)
    has_a_company=models.BooleanField(default=False)
    def __str__(self):
        return self.first_name




