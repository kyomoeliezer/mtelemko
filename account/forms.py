from django import forms
from django.forms import ModelChoiceField
from account.models import *
from django.db.models import FloatField, F,Sum,Case,When,IntegerField,Value,Min,Q,Count,Max
import datetime

class ExpenseForm(forms.ModelForm):
    amount=forms.CharField(label='Expense Amount')
    trans_account=ModelChoiceField(queryset=Account.objects.filter(Q(is_cashaccount=True)|Q(is_bankaccount=True)))
    account = ModelChoiceField(queryset=Account.objects.filter(Q(is_cashaccount=False) & Q(is_bankaccount=False)))
    invoice = ModelChoiceField(queryset=Invoice.objects.filter(Q(invoice_date__year__gte=2022)).order_by('-id'))

    class Meta:
        model=Expensejournal
        fields=('invoice','champion','account','date','desc')

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'
        self.fields['desc'].widget.attrs['cols'] = '12'
        self.fields['desc'].widget.attrs['rows'] = '3'
        self.fields['date'].widget.attrs['class'] = 'datepicker'
        self.fields['account'].widget.attrs['class'] = 'select2'
        self.fields['invoice'].widget.attrs['class'] = 'select2'
        self.fields['champion'].widget.attrs['id'] = 'contactID'
        self.fields['account'].widget.attrs['class'] = 'select2'
        self.fields['trans_account'].widget.attrs['class'] = 'select2'

        self.fields['invoice'].required = False
        self.fields['champion'].required= False
