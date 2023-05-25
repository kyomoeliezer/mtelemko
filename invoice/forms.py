from django import forms
from invoice.models import *

class QouteForm(forms.ModelForm):
    desc=forms.CharField(required=False)
    qty=forms.CharField(required=False)
    price=forms.CharField(required=False)
    antetion_person=forms.CharField(required=False)
    ismain=forms.CharField(required=False)
    order=forms.CharField(required=False)
    stock_info=forms.CharField(required=False)
    tag=forms.CharField(required=False)
    comment=forms.CharField(required=False)


    
    class Meta:
        model=Invoice
        fields=('category','currency','start_date','end_date','company','pobox','city','antetion_person','campaign','deposittype','stock_info','tag','show_tax','comment','champion')

    def __init__(self, *args, **kwargs):
        super(QouteForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'

        self.fields['start_date'].widget.attrs['class'] = 'datepicker'
        self.fields['end_date'].widget.attrs['class'] = 'datepicker'
        self.fields['category'].widget.attrs['class'] = 'select2'
        self.fields['champion'].widget.attrs['class'] = 'select2'
        self.fields['champion'].required  = False

class QouteUploadForm(forms.ModelForm):
    #file=forms.FileField(label='File to Import',required=False)
    antetion_person=forms.CharField(required=False,min_length=6)
    file=forms.FileField(label='File to Import',required=False)
    stock_info=forms.CharField(required=False)
    tag=forms.CharField(required=False)

    class Meta:
        model=Invoice
        fields=('currency','start_date','end_date','company','pobox','city','antetion_person','campaign','file','deposittype','stock_info','tag','category','champion')

    def __init__(self, *args, **kwargs):
        super(QouteUploadForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'

        self.fields['start_date'].widget.attrs['class'] = 'datepicker'
        self.fields['end_date'].widget.attrs['class'] = 'datepicker'


class JobcardForm(forms.ModelForm):
    desc=forms.Textarea(attrs={'required':'false'})
    order=forms.CharField(required=False)
    status1=forms.CharField(required=False)


    class Meta:
        model=Jobcard
        fields=('project','device','client','address','city','technician','job_date')

    def __init__(self, *args, invoice,**kwargs):

        super(JobcardForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['client'].initial = invoice.company
        self.fields['address'].initial = invoice.pobox
        self.fields['city'].initial = invoice.city
        self.fields['job_date'].initial = invoice.start_date

        self.fields['job_date'].widget.attrs['class'] = 'datepicker'


class JobcardUpdateForm(forms.ModelForm):
    desc=forms.Textarea(attrs={'required':'false'})
    order=forms.CharField(required=False)
    status1=forms.CharField(required=False)


    class Meta:
        model=Jobcard
        fields=('project','device','client','address','city','technician','job_date')

    def __init__(self, *args,**kwargs):

        super(JobcardUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'


        self.fields['job_date'].widget.attrs['class'] = 'datepicker'

class InvoiceDistributionForm(forms.ModelForm):
    class Meta:
        model=InvoiceDistribution
        fields=('desc','expected_amount')