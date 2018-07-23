from django import  forms
from lead.models import Lead,Lead_status
from contact.models import Contact
from django.forms import ModelChoiceField

class LeadForm(forms.ModelForm):
    status=ModelChoiceField(queryset=Lead_status.objects.all())
    contact=ModelChoiceField(queryset=Contact.objects.all())
    class Meta:
        model=Lead
        fields=['title','desc','expected_sale_amount','expected_closing_date','contact','status','score']

class Lead_statusForm(forms.ModelForm):
    class Meta:
        model=Lead_status
        fields=['name','order']