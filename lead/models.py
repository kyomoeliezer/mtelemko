from django.db import models
from datetime import  datetime
from django.contrib.auth.models import User
from contact.models import Contact
from customuser.models import CustomUser


# Create your models here.
class Lead_status(models.Model):
    name=models.CharField(max_length=30)
    order=models.IntegerField()


class Lead(models.Model):
    title=models.CharField(max_length=300)
    desc=models.TextField(max_length=400)
    reg_date=models.DateTimeField(default=datetime.now())
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    expected_sale_amount=models.FloatField()
    expected_closing_date=models.DateTimeField(null=True)
    status=models.ForeignKey(Lead_status,on_delete=models.DO_NOTHING)
    status_desc=models.CharField(max_length=50,null=True)
    score=models.IntegerField(max_length=20, blank=True,null=True,default=10)
    contact=models.ForeignKey(Contact,on_delete=models.CASCADE)




