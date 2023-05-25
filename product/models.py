from django.forms import forms
from django.db import models
from user.models import User
# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=300,)
    type=models.CharField(max_length=30)
    description=models.CharField(max_length=500)
    tag=models.CharField(max_length=300,blank=True, null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='product_user')
    created_at=models.DateTimeField(auto_now_add=True)








