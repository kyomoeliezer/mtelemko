from django import  forms
from project.models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model=Project
        fields=['title','desc','company','amount','company_type','status','start_date','end_date']

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['title'].widget.attrs['cols'] = '12'
        self.fields['title'].widget.attrs['rows'] = '2'
        self.fields['desc'].widget.attrs['cols'] = '12'
        self.fields['desc'].widget.attrs['rows'] = '2'
        self.fields['end_date'].widget.attrs['class'] = 'datepicker'
        self.fields['start_date'].widget.attrs['class'] = 'datepicker'

class ProjectUpdateForm(forms.ModelForm):
    amount_depostedbyclient=forms.FloatField(required=False,label="Posted by Client")
    class Meta:
        model=Project
        fields=['title','desc','company','amount','company_type','status','start_date','end_date','amount_depostedbyclient']

    def __init__(self, *args, **kwargs):
        super(ProjectUpdateForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['title'].widget.attrs['cols'] = '12'
        self.fields['title'].widget.attrs['rows'] = '2'
        self.fields['desc'].widget.attrs['cols'] = '12'
        self.fields['desc'].widget.attrs['rows'] = '2'
        self.fields['end_date'].widget.attrs['class'] = 'datepicker'
        self.fields['start_date'].widget.attrs['class'] = 'datepicker'


class TaskForm(forms.ModelForm):
    desc=forms.CharField(required=False,label="Task discreption",widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    class Meta:
        model=ProjectTasks
        fields=['name','desc','responsible','start_date','end_date']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'

        self.fields['desc'].widget.attrs['cols'] = '12'
        self.fields['desc'].widget.attrs['rows'] = '2'
        self.fields['end_date'].widget.attrs['class'] = 'datepicker'
        self.fields['start_date'].widget.attrs['class'] = 'datepicker'

class TaskWorkonForm(forms.ModelForm):
    desc=forms.CharField(required=False,label="Task discreption",widget=forms.Textarea(attrs={"rows":5, "cols":20}))
    class Meta:
        model=ProjectTasks
        fields=['desc','end_date','status']

    def __init__(self, *args, **kwargs):
        super(TaskWorkonForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'

        self.fields['desc'].widget.attrs['cols'] = '12'
        self.fields['desc'].widget.attrs['rows'] = '2'
        self.fields['end_date'].widget.attrs['class'] = 'datepicker'

class CostForm(forms.ModelForm):
    class Meta:
        model=ProjectAmounts
        fields=['cost_name','amount']

    def __init__(self, *args, **kwargs):
        super(CostForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
