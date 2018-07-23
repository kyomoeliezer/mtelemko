from django.conf.urls import url,re_path
from django.urls import path
from lead.views import CreateLead,CreateStatus,LeadList,StatusList,LeadUpdate,LeadstatusUpdate,LeadDetail

urlpatterns= [
    url(r'^newlead/$',CreateLead.as_view(),name="newlead"),
    url(r'^$',LeadList.as_view(),name="leadlist"),
    url(r'^status/$',StatusList.as_view(),name="statuslist"),
    url(r'^newstatus/$',CreateStatus.as_view(),name="newstatus"),
    url(r'^(?P<pk>[0-9]+)/update/$',LeadUpdate.as_view(),name="updatelead"),
    url(r'^status/(?P<pk>[0-9]+)/update/$',LeadstatusUpdate.as_view(),name="updatestatus"),
    url("^(?P<pk>[0-9]+)/detail/$", LeadDetail.as_view(),name="leaddetail"),
    #path('<slug:slug>/', LeadDetail.as_view(), name='leaddetail'),
]