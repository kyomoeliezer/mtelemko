from django import forms
from meeting.models import Meeting
from  lead.models import Lead
from django.forms import ModelChoiceField

class MeetingForm(forms.ModelForm):
    lead=ModelChoiceField(queryset=Lead.objects.all())
    class Meta:
        model=Meeting
        exclude=('user',)
    def __init__(self, *args, **kwargs):
        super(MeetingForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['date'].widget.attrs['class'] = 'datepicker'
        self.fields['meeting_time'].widget.attrs['id'] = 'timepicker'



