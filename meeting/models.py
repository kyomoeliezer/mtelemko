from django.forms import forms
from django.db import models
from lead.models import Lead
# Create your models here.
class Meeting(models.Model):
    date=models.DateTimeField()
    meeting_time=models.TimeField(null=True,blank=True)
    agenda=models.CharField(max_length=300)
    desc=models.CharField(max_length=500,null=True)
    meeting_status=models.CharField(max_length=10,null=True,default='scheduled')
    #next_meeting_date=models.DateTimeField( null=True)
    #next_agenda=models.CharField(max_length=300,null=True)
    lead=models.ForeignKey(Lead,on_delete=models.CASCADE)





