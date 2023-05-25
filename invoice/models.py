import os
from django.db import models
from contact.models import Contact
from user.models import User
from lead.models import Campaign
import datetime
# Create your models here.
class ServiceCategory(models.Model):
    name=models.CharField(max_length=20)
    desc=models.TextField(null=True,verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

def content_file_name_invo(instance, filename):
    words=(instance.pname).split()
    #shule=(instance.school.pname).split()
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.invoice_no, ext)
    if instance.plogo.storage.exists(instance.plogo.name):
        os.remove(os.path.join('/invo_import', filename))
        filename =  "%s.%s" % (instance.invoice_no, ext)
        return os.path.join('/invo_import', filename)
    return os.path.join('/invo_import', filename)


class Invoice(models.Model):
    date=str(datetime.datetime.today().date())
    date_1 = datetime.datetime.strptime(date,"%Y-%m-%d")
    end_date = date_1 + datetime.timedelta(days=30)
    choices=(('QOUTE','QOUTATION'),('INVOICE','INVOICE'))
    deposittype=(('BANK','BANK'),('BOTH','M-PESA/BANK'))
    categoryl=(('GOVERNMENT','GOVERNMENT'),('WEBSITE','WEBSITE'),('SOFTWARE','SOFTWARE'))
    #category=models.CharField(max_length=500,default='WEBSITE',choices=categoryl)
    curr=(('TZS','TZS'),('USD','USD'))
    no=models.IntegerField(default=1)
    invoice_no=models.CharField(max_length=50,verbose_name='Invoice No',null=True)
    invoice_date=models.DateField(verbose_name='Invoice Date',auto_now_add=True)
    invoice_status=models.CharField(max_length=300,choices=choices)

    #contact=models.ForeignKey(Contact,on_delete=models.PROTECT,verbose_name='Contact/Company')
    campaign=models.ForeignKey(Campaign,on_delete=models.PROTECT,verbose_name='Campaign',null=True)
    
    currency=models.CharField(max_length=500,default='TZS',choices=curr)
    deposittype=models.CharField(max_length=500,default='BANK',choices=deposittype)
    start_date=models.DateField(null=True,verbose_name='Invoice Start date')
    end_date=models.DateField(null=True,verbose_name='Invoice End date')
    #contact=models.ForeignKey(Contact,on_delete=models.PROTECT,verbose_name='Contact/Company')

    antetion_person=models.CharField(max_length=500,null=True)
    city=models.CharField(max_length=500,null=True)
    pobox=models.CharField(max_length=500,null=True)
    company=models.CharField(max_length=500,null=True)
    is_aninvoice=models.BooleanField(default=False)
    stock_info=models.CharField(max_length=500,null=True)
    tag=models.CharField(max_length=500,null=True)
    is_cancelled=models.BooleanField(default=False)
    show_tax=models.BooleanField(default=True,verbose_name='Inclued VAT')
    invoice_start_date=models.DateField(null=True,verbose_name='Invoice Date')
    champion = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Championsaleperson',null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='invoice_user')
    category=models.ForeignKey(ServiceCategory,on_delete=models.CASCADE,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    file=models.FileField(null=True,upload_to=content_file_name_invo)
    comment=models.TextField(max_length=500,null=True,verbose_name='Comments descriptions, also state payment history')
    def __str__(self):
        return self.invoice_no+' '+self.company+' '+str(self.invoice_date)

class InvoiceLine(models.Model):
    ismain=models.BooleanField(default=False)
    order=models.IntegerField(default=1)
    invoice=models.ForeignKey(Invoice,on_delete=models.PROTECT)
    desc=models.TextField(max_length=2000,verbose_name='Description')
    qty=models.FloatField(max_length=40,verbose_name='Quantity')
    price=models.FloatField(max_length=40,verbose_name='Price')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.desc


class Jobcard(models.Model):
    project=models.CharField(verbose_name='Project Title',max_length=300)
    device=models.CharField(verbose_name='Device(s)',max_length=300)
    client=models.CharField(verbose_name='Client Name',max_length=300)
    address=models.CharField(verbose_name='Client Address',max_length=300)
    city=models.CharField(verbose_name='Client City',max_length=300)
    technician=models.CharField(verbose_name='Technician/Engineer',max_length=300)
    job_date=models.DateField(null=True,verbose_name='Activities End Date')
    jobno=models.CharField(verbose_name='Job no',max_length=30)
    jobcard_no=models.CharField(verbose_name='Jobcard Number',max_length=30)
    status=models.CharField(verbose_name='Status',max_length=20,default='done')
    invoice=models.ForeignKey(Invoice,on_delete=models.PROTECT)
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='job_user')
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.jobcard_no


class JobcardLine(models.Model):
    order=models.IntegerField(default=1)
    jobcard=models.ForeignKey(Jobcard,on_delete=models.PROTECT)
    #device=models.CharField(max_length=200,verbose_name='Devices')
    desc=models.TextField(max_length=200,verbose_name='Description')
    status=models.IntegerField(default=1,verbose_name="1:done,0:onprogress, 10:is a device")
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.desc


class InvoiceDistribution(models.Model):
    desc = models.CharField(verbose_name='Description',max_length=100)
    expected_amount = models.FloatField(max_length=40, verbose_name='Amount expected to be given',null=True)
    actual_amount = models.FloatField(max_length=40, verbose_name='Amount expected to be given', null=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.DO_NOTHING, related_name='invoiceiddist')
    created_at = models.DateTimeField(auto_now_add=True)
    created_by=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='createdby009',null=True)
    def __str__(self):
        return self.desc




