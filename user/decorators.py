from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import REDIRECT_FIELD_NAME
default_message = 'You dont have permission.'
unauthenticated_message = 'User already logged in.'
perm_url=reverse_lazy('no_permission')
def admin_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=perm_url, message=default_message):
    """
    Decorator for views that checks that the user is logged in and is
    staff, displaying message if provided.
    """
    actual_decorator = user_passes_test(
        lambda u: u.role.perm.filter(perm_name='admin').exists(),
        login_url=login_url,
        redirect_field_name=redirect_field_name,

    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

def reg_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=perm_url, message=default_message):
    """
    Decorator for views that checks that the user is logged in and is
    staff, displaying message if provided.
    """
    actual_decorator = user_passes_test(
        lambda u: u.role.perm.filter(perm_name__in=['reg_view','reg_create','reg_delete']).exists(),
        login_url=login_url,
        redirect_field_name=redirect_field_name,

    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator
    
    
###CHET Certificate Permission
def cert_permission(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=perm_url, message=default_message):
    """
    Decorator for views that checks that the user is permitted to created the certificate.
    """
    actual_decorator = user_passes_test(
        lambda u: u.role.perm.filter(perm_name__in=['cert_permission',]).exists(),
        login_url=login_url,
        redirect_field_name=redirect_field_name,

    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

###CHET Account Permission
def all_account_permission(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=perm_url, message=default_message):
    """
    Decorator for views that checks that the user is permitted to created the certificate.
    """
    actual_decorator = user_passes_test(
        lambda u: u.role.perm.filter(perm_name__in=['all_account_operations',]).exists(),
        login_url=login_url,
        redirect_field_name=redirect_field_name,

    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

###CHET Account Permission
def sales_permission(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=perm_url, message=default_message):
    """
    Decorator for views that checks that the user is permitted to created the certificate.
    """
    actual_decorator = user_passes_test(
        lambda u: u.role.perm.filter(perm_name__in=['all_sales',]).exists(),
        login_url=login_url,
        redirect_field_name=redirect_field_name,

    )
    if view_func:
        return actual_decorator(view_func)
    return actual_decorator

