from django.db import models
from user.models import User
from datetime import  datetime


class Tender(models.Model):
    desc=models.TextField(max_length=400)
    tender_no=models.CharField(max_length=300,null=True)
    company=models.CharField(max_length=300)
    amount=models.FloatField()
    company_type=models.CharField(max_length=500,choices=(('Government','Government'),('Private','Private')))
    status=models.CharField(max_length=500,choices=(('Evaluation','Evaluation'),('Worn','Worn'),('Failed','Failed')))
    submission_date=models.DateTimeField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='tender_user')
    def __str__(self):
        return self.desc


