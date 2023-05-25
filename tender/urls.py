from django.conf.urls import url,re_path
from django.urls import path
from tender.views import * #CreateLead,CreateStatus,LeadList,StatusList,LeadUpdate,LeadstatusUpdate,LeadDetail

urlpatterns= [
    url(r'^new-tender/$',CreateTender.as_view(),name="newtender"),
    url(r'^evaluation$',TenderListEvaluation.as_view(),name="evaluationlist"),
    url(r'^worn$',TenderListWorn.as_view(),name="wornlist"),
    url(r'^failed$',TenderListFailed.as_view(),name="failedlist"),
    url(r'^$',TenderList.as_view(),name="tenderlist"),
    url(r'^(?P<pk>[0-9]+)/update/$',TenderUpdate.as_view(),name="updatetender"),
    url(r'^(?P<pk>[0-9]+)/delete/$',TenderDelete.as_view(),name="deletetender"),
]
