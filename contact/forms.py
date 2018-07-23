from django import  forms
from contact.models import Contact,Company
from django.forms import ModelChoiceField

class ContactForm(forms.ModelForm):
    company=ModelChoiceField(queryset=Company.objects.all())
    class Meta:
        model=Contact
        fields=['first_name','middle_name','last_name','has_a_company','mobile','email','company']

class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=['name','street','city','address']

