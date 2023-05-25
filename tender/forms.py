from django import  forms
from tender.models import *


class TenderForm(forms.ModelForm):

    class Meta:
        model=Tender
        fields=['desc','tender_no','company','amount','company_type','status','submission_date']

    def __init__(self, *args, **kwargs):
        super(TenderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['desc'].widget.attrs['cols'] = '12'
        self.fields['desc'].widget.attrs['rows'] = '3'
        self.fields['submission_date'].widget.attrs['class'] = 'datepicker'
