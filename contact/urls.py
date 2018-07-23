from django.conf.urls import url,re_path
from contact.views import CreateContact,CreateCompany,ContactList,ContactUpdate

urlpatterns= [
    url(r'^newcontact/$',CreateContact.as_view(),name="newcontact"),
     url(r'^newcompany/$',CreateCompany.as_view(),name="newcompany"),
    url(r'^(?P<pk>\d+)/update/$',ContactUpdate.as_view(),name="updatecontact"),
    url(r'^$',ContactList.as_view(),name="contactlist"),
]