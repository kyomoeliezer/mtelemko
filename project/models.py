from django.db import models
from user.models import User
from datetime import  datetime


class Project(models.Model):
    title=models.TextField(max_length=400)
    desc=models.TextField(max_length=400)
    company=models.CharField(max_length=300)
    amount=models.FloatField()
    amount_depostedbyclient=models.FloatField(verbose_name='Payment after Tax',null=True)
    company_type=models.CharField(max_length=500,choices=(('Government','Government'),('Private','Private')))
    status=models.CharField(max_length=500,choices=(('Onprogress','Onprogress'),('Completed','Completed'),('Pending','Pending')))
    start_date=models.DateTimeField(null=True)
    end_date=models.DateTimeField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='project_user')
    def __str__(self):
        return self.title

class ProjectTasks(models.Model):
    name=models.CharField(max_length=400,verbose_name='Task')
    desc=models.CharField(max_length=400,verbose_name='Desc',null=True)
    status=models.CharField(max_length=20,verbose_name='Status',null=True)
    end_date=models.DateField(verbose_name='Task End date',null=True)
    start_date=models.DateField(verbose_name='Task start date',null=True)
    responsible=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='Taskresponsible')
    project=models.ForeignKey(Project,on_delete=models.PROTECT,related_name='task_proj')

    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return self.name

class ProjectAmounts(models.Model):
    cost_name=models.CharField(max_length=400)
    amount=models.FloatField()
    project=models.ForeignKey(Project,on_delete=models.PROTECT,related_name='project_amount')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='amount_user')
    def __str__(self):
        return self.cost_name




