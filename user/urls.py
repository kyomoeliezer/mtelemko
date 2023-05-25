from django.conf.urls import re_path,include,url
from user.views import *

from user.roles import YouDontHavePermission

urlpatterns=[
    url(r'^login-user$', LoginView1.as_view(),name='login_user'),
    url(r'^login-user$', LoginView1.as_view(),name='login-user'),
    url(r'^logout-user$', LogoutView.as_view(),name='logout_user'),
    url(r'^(?P<pk>[0-9]+)/as-user$', LoginViewasSomeUser.as_view(),name='as_user'),
    
    url(r'^userroles$', Roles.as_view(),name='roles'),
    #url(r'^users$', Users.as_view(),name='users'),
    url(r'^new-user', NewUser.as_view(),name='new_user'),

    url(r'^new-role$', CreateRole.as_view(),name='new_role'),
    url(r'^you-dont-have-permission$', YouDontHavePermission.as_view(),name='no_permission'),
    url(r'^(?P<pk>[0-9]+)/delete$', UserDelete.as_view(),name='delete_user'),
    url(r'^(?P<pk>[0-9]+)/update$', UpdateRole.as_view(),name='update_role'),
    url(r'^(?P<pk>[0-9]+)/user-update$', UpdateUser.as_view(),name='update_user'),

    #####
###PERMIS
    url(r'^perm-required$', PermissionRequired.as_view(),name='permission_required'),
    url(r'^permissions$', PermissionsList.as_view(),name='permissions'),
    url(r'^new-permission$', CreatePermission.as_view(),name='new_permission'),
    url(r'^permission/(?P<pk>[0-9]+)/update$', UpdatePermission.as_view(),name='update_permission'),
    url(r'^permission/(?P<pk>[0-9]+)/delete$', PermissionDelete.as_view(),name='delete_permission'),
    url(r'^', Users.as_view(),name='users'),


]
