from django import forms
from meeting.models import Meeting
from  lead.models import Lead
from django.forms import ModelChoiceField

class MeetingForm(forms.ModelForm):
    lead=ModelChoiceField(queryset=Lead.objects.all())
    class Meta:
        model=Meeting
        fields='__all__'


