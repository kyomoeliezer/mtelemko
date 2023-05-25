from django.db import models
from datetime import  datetime
#from django.contrib.auth.models import User
from contact.models import Contact
from user.models import User


# Create your models here.
class Lead_status(models.Model):
    name=models.CharField(max_length=30)
    order=models.IntegerField()
    def __str__(self):
        return self.name

# Create your models here.
class Campaign(models.Model):
    name=models.CharField(max_length=300)
    desc=models.CharField(max_length=200,null=True)
    script=models.CharField(max_length=200,null=True)
    target_lead_no=models.IntegerField(null=True)
    campaign_start=models.DateField(null=True)
    campaign_end=models.DateField(null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_campaign')
    def __str__(self):
        return self.name

# Create your models here.
class TargetContact(models.Model):
    statuschoice=(('','-------------'),('contact','Contact'),('finding','Finding'),('dropped','Dropped'))
    name=models.CharField(max_length=300,verbose_name='Company/Person name')
    location=models.CharField(max_length=200,null=True)
    contact_name=models.CharField(max_length=200,null=True)
    mobile=models.CharField(null=True,max_length=13)
    main_activity=models.CharField(max_length=200,null=True,verbose_name="Its main activity")
    campaign=models.ForeignKey(Campaign,on_delete=models.DO_NOTHING,null=True)
    worked_on=models.BooleanField(default=False)
    next_follup_date=models.DateField(null=True)
    status=models.CharField(choices=statuschoice,default='finding',max_length=30)
    visit_desc=models.CharField(max_length=300,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_target')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

class Lead(models.Model):
    choices=(('','-----'),('call','Call'),('meeting','Meeting'),('reminder','Reminder'))
    title=models.CharField(max_length=300)
    desc=models.TextField(max_length=400)
    reg_date=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='lead_user')
    expected_sale_amount=models.FloatField()
    expected_closing_date=models.DateTimeField(null=True)
    next_action=models.CharField(choices=choices,max_length=30,default='call')
    next_action_date=models.DateTimeField(null=True)
    status=models.ForeignKey(Lead_status,on_delete=models.DO_NOTHING)
    status_desc=models.CharField(max_length=50,null=True)
    score=models.IntegerField(blank=True,null=True,default=10)
    contact=models.ForeignKey(Contact,on_delete=models.CASCADE)
    campaign=models.ForeignKey(Campaign,on_delete=models.DO_NOTHING,null=True)
    leadmanager=models.ForeignKey(User,on_delete=models.CASCADE,related_name='leadmanager',null=True)
    status_info=models.CharField(max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title


class LeadActivity(models.Model):
    lead=models.ForeignKey(Lead,on_delete=models.DO_NOTHING)
    followup=models.TextField(max_length=200,verbose_name='Follup Note')
    followup_date=models.DateField(verbose_name='Follup date')
    followup_by=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='responsible')
    created_by=models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='FiledBy')
    created_date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.followup


