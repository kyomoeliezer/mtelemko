from django import template
from django.db.models import Max,Min
from user.models import *
#from sales.models import * #Batch,Ticket,Box,HouseGrade,PCNTicket
from django.db.models import * #Q,Count,F,Max,ProtectedError,IntegerField
register = template.Library()



@register.simple_tag
def is_admin(user):
    if user:
        if 'ADMIN' in (user.role.code).upper():
            return True

    return False


@register.simple_tag
def is_supervisor(user):
    if user:
        if 'SU' in (user.role.code).upper():
            return True

    return False


@register.simple_tag
def is_operator(user):
    if user:
        if 'OM' in (user.role.code).upper():
            return True

    return False

