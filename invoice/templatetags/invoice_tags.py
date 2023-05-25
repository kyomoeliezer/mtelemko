from django import template
from django.db.models import Max,Min,Sum,F,FloatField
from invoice.models import *
from django.db.models import * #Q,Count,F,Max,ProtectedError,IntegerField
import datetime
register = template.Library()

@register.simple_tag
def invoice_amount(id):
    inv=InvoiceLine.objects.filter(invoice_id=id)
    if inv:
        return inv.aggregate(total_group=Sum(F('qty')*F('price'), output_field=FloatField()))['total_group']


    return inv.count();

@register.simple_tag
def invoice_vat(id):
    inv=InvoiceLine.objects.filter(invoice_id=id)
    if inv:
        return  inv.aggregate(total_group=Sum(F('qty')*F('price')*Value('0.18'), output_field=FloatField()))['total_group']
        


    return inv.count();
@register.simple_tag
def invoice_amount_total(id):
    inv=InvoiceLine.objects.filter(invoice_id=id)
    if inv:
        return  inv.aggregate(total_group=Sum(F('qty')*F('price')*Value('1.18'), output_field=FloatField()))['total_group']
        


    return inv.count();

@register.simple_tag
def int_add(a,b):
    if a and b:
        return int(a)+int(b)
    else:
        return 0
@register.simple_tag
def product(a,b):
    if a and b:
        return a*b
    else:
        return '-'

@register.simple_tag
def toa(a,A):
    if A and a:
        return float(A) - float(a)
    elif A and not a:
        return A
    
    elif a and not A:
        return a
        
    else:
        return '-'

@register.simple_tag
def date_deff(a):
    date_format = "%Y-%m-%d"

    b = (datetime.datetime.today().date())
    delta = b - a
    return  delta.days # that's it
