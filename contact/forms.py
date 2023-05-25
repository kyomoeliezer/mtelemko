from django import  forms
from contact.models import Contact,Company
from django.forms import ModelChoiceField

class ContactForm(forms.ModelForm):
    #company=ModelChoiceField(queryset=Company.objects.all())
    middle_name=forms.CharField(required=False)
    last_name=forms.CharField(required=False)
    company=forms.CharField(required=False)
    address=forms.CharField(label='Address/Location',required=False)
    email=forms.EmailField(required=False)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':'12','rows':'4'}),required=False)
    class Meta:
        model=Contact
        fields=['first_name','middle_name','last_name','has_a_company','mobile','email','company','address','city']
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'




class CompanyForm(forms.ModelForm):
    class Meta:
        model=Company
        fields=['name','street','city','address']

