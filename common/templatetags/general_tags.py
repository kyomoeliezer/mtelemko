from django import template
from django.db.models import Max,Min,Sum,F,FloatField
#from invoice.models import *
from lead.models import Lead
from django.db.models import * #Q,Count,F,Max,ProtectedError,IntegerField
import datetime
register = template.Library()

@register.simple_tag
def product(a,b):
    if a and b:
        return a*b
    else:
        return 0

@register.simple_tag
def date_deff_with_today(a):
    date_format = "%Y-%m-%d"

    b = (datetime.datetime.today().date())
    delta = b - a
    return  delta.days # that's it

@register.simple_tag
def add(a,b):
    if a and b:
        return a+b
    if a and not b:
        return a
    if b and not a:
        return b
    else:
        return 0


@register.simple_tag
def int_add(a,b):
    if a and b:
        return int(a)+int(b)
    elif a and not b:
        return a
    elif b and not a:
        return b

@register.simple_tag
def minus(a,b):
    if a and b:
        return a-b
    else:
        return 0
@register.simple_tag
def no_leads(id):
    lead=Lead.objects.filter(campaign_id=id)
    if lead:
        return lead.aggregate(sum=Sum('expected_sale_amount'))['sum']
    else:
        return 0

@register.simple_tag
def set(a):
    return a