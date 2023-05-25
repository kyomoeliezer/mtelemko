from django import template
from django.contrib.auth.models import Group
register = template.Library()

@register.simple_tag
def is_manager(request):
     return request.user.groups.filter(name='manager').exists()

@register.simple_tag
def role_name(user):
      if  not  user.groups.filter(name='admin').exists():
           return 'Admin'
      elif  not  user.groups.filter(name='manager').exists():
           return 'Manager'
      elif  not  user.groups.filter(name='teacher').exists():
           return 'Teacher'
      elif  not  user.groups.filter(name='parent').exists():
           return 'Parent'
      elif  not  user.groups.filter(name='academic').exists():
           return 'Academic'
      else:
           return ''

