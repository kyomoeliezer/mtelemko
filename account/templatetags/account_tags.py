from django import template
from django.db.models import Max,Min,Sum,F,FloatField
from account.models import *
from django.db.models import * #Q,Count,F,Max,ProtectedError,IntegerField
import datetime
register = template.Library()


@register.simple_tag
def borrowed_paid(id):
    exp=Expensejournal.objects.filter(borrowed_id=id)
    if exp:
        return  exp.aggregate(total_group=Sum('dr'))['total_group']
    return exp.count()

@register.simple_tag
def borrowed_balance(id):
    exp=Expensejournal.objects.filter(borrowed_id=id)
    loan=WeBorrowed.objects.get(pk=id)
    if exp:
        pid = exp.aggregate(total_group=Sum('dr'))['total_group']
        return loan.amount - pid
    return loan.amount
