from django import  forms
from lead.models import * #  Lead,Lead_status,Campaign,TargetContact
from contact.models import Contact
from django.forms import ModelChoiceField

class LeadForm(forms.ModelForm):
    status=ModelChoiceField(queryset=Lead_status.objects.all())
    contact=ModelChoiceField(queryset=Contact.objects.all())
    campaign=ModelChoiceField(queryset=Campaign.objects.all())
    score=forms.IntegerField(label="Probability of making a sale on this")
    class Meta:
        model=Lead
        fields=['leadmanager','title','desc','expected_sale_amount','expected_closing_date','contact','status','score','next_action_date','next_action','campaign']

    def __init__(self, *args, **kwargs):
        super(LeadForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['desc'].widget.attrs['cols'] = '12'
        self.fields['desc'].widget.attrs['rows'] = '3'
        self.fields['expected_closing_date'].widget.attrs['class'] = 'datepicker'
        self.fields['next_action_date'].widget.attrs['class'] = 'datepicker'
        self.fields['contact'].widget.attrs['id'] = 'contactID'

class CampaignForm(forms.ModelForm):
    class Meta:
        model=Campaign
        fields=['name','desc','script','target_lead_no','campaign_start','campaign_end']

    def __init__(self, *args, **kwargs):
        super(CampaignForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['desc'].widget.attrs['cols'] = '12'
        self.fields['desc'].widget.attrs['rows'] = '3'
        self.fields['script'].widget.attrs['cols'] = '12'
        self.fields['script'].widget.attrs['rows'] = '3'
        self.fields['campaign_start'].widget.attrs['class'] = 'datepicker'
        self.fields['campaign_end'].widget.attrs['class'] = 'datepicker'


class TargetForm(forms.ModelForm):
    location=forms.CharField(required=False)
    main_activity=forms.CharField(required=False)
    mobile=forms.CharField(required=False)
    class Meta:
        model=TargetContact
        fields=['name','location','main_activity','campaign','mobile']

    def __init__(self, *args, **kwargs):
        super(TargetForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['location'].widget.attrs['cols'] = '12'
        self.fields['location'].widget.attrs['rows'] = '3'

class LeadActivityForm(forms.ModelForm):
    class Meta:
        model=LeadActivity
        fields=['followup','followup_by']

    def __init__(self, *args, **kwargs):
        super(LeadActivityForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        #self.fields['followup_date'].widget.attrs['class'] = 'datepicker'



class TargetFormVisitStatus(forms.ModelForm):
    mobile=forms.CharField(required=False,widget=forms.TextInput(attrs={'placeholder': 'Eg  0752350620'}))
    class Meta:
        model=TargetContact
        fields=['visit_desc','next_follup_date','mobile','name','status','contact_name']

    def __init__(self, *args, **kwargs):
        super(TargetFormVisitStatus, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['visit_desc'].widget.attrs['cols'] = '12'
        self.fields['visit_desc'].widget.attrs['rows'] = '3'
        self.fields['next_follup_date'].widget.attrs['class'] = 'datepicker'




class Lead_statusForm(forms.ModelForm):
    class Meta:
        model=Lead_status
        fields=['name','order']
