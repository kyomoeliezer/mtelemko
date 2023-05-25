from django.conf.urls import url,re_path
from django.urls import path
from lead.views import * # CreateLead,CreateStatus,LeadList,StatusList,LeadUpdate,LeadstatusUpdate,LeadDetail,Dashboard,ContactTargetUpdateVisit

urlpatterns= [
    url(r'^newlead/$',CreateLead.as_view(),name="newlead"),
    
    url(r'^leads-list$',LeadList.as_view(),name="leadlist"),
    url(r'^status/$',StatusList.as_view(),name="statuslist"),
    url(r'^newstatus/$',CreateStatus.as_view(),name="newstatus"),
    url(r'^(?P<pk>[0-9]+)/update/$',LeadUpdate.as_view(),name="updatelead"),
    url(r'^status/(?P<pk>[0-9]+)/update/$',LeadstatusUpdate.as_view(),name="updatestatus"),
    url(r'^lead/(?P<pk>[0-9]+)/delete/$',LEADDelete.as_view(),name="delete_lead"),
    #####LEAD FOLLWUP
    url(r'^followup/(?P<pk>[0-9]+)/now/$',LeadActivityOnFly.as_view(),name="lead_followup"),
    url(r'^(?P<pk>[0-9]+)/followup/edit/$',LeadActivityEditOnFly.as_view(),name="lead_followup_edit"),
    url(r'^(?P<pk>[0-9]+)/followup/delete$',LeadActivityDelete.as_view(),name="lead_followup_delete"),


    ###CAMPAIGN
    url(r'^new-target-contact/$',CreateContactTarget.as_view(),name="newtargetcontact"),
    url(r'^target-contact/(?P<pk>[0-9]+)/update/$',ContactTargetUpdate.as_view(),name="updatetargetcontact"),
    url(r'^target-contact/(?P<pk>[0-9]+)/delete/$',ContactTargetDelete.as_view(),name="delete_targetcontact"),
    url(r'^target-contact-worked-on/(?P<pk>[0-9]+)/update/$',WorkedOnContactAlread.as_view(),name="worked_on"),
    url(r'^target-contact-worked-status/(?P<pk>[0-9]+)/update/$',ContactTargetUpdateVisit.as_view(),name="worked_update"),
    
    
    url(r'^target-contact-worked-on-lists$',ContactTargetList_done.as_view(),name="targetcontacts_done"),
    url(r'^target-qualified-contact-lists$',ContactTargetList_contacts.as_view(),name="targetcontacts_contacts"),
    url(r'^target-qualified-finding-lists$',ContactTargetList_Finding.as_view(),name="targetcontacts_finding"),
    url(r'^target-dropped-lists$',ContactTargetList_Dropped.as_view(),name="targetcontacts_dropped"),
    
    
    
    url(r'^targetanalysis/$',ContactTargetAnalysis.as_view(),name="targetcontact_analysis"),
     url(r'^target-contact/$',ContactTargetList.as_view(),name="targetcontacts"),
    #####
    #####TARGET CONTACT
    url(r'^new-campaign/$',CreateCampaign.as_view(),name="newcampaign"),
    url(r'^campaign/(?P<pk>[0-9]+)/update/$',CampaignUpdate.as_view(),name="updatecampaign"),
    url(r'^campaign/(?P<pk>[0-9]+)/delete/$',CampaignDelete.as_view(),name="delete_campaign"),
    url(r'^campaign/(?P<pk>[0-9]+)/detail/$',CompaignDetail.as_view(),name="campaigndetail"),
    url(r'^campaigns/$',CampaignList.as_view(),name="campaigns"),
    
    url("^(?P<pk>[0-9]+)/detail/$", LeadDetail.as_view(),name="leaddetail"),
    url("^your-lead-dashboard$", DashboardINDIV.as_view(),name="yourleaddashboard"),

   
    #path('<slug:slug>/', LeadDetail.as_view(), name='leaddetail'),
]
