#from django.urls import include,path,re_path
from django.conf.urls import url
from meeting.views import MeetingCreate,MeetingUpdate,MeetingList,MeetingDelete

urlpatterns=[
    url(r'^$',MeetingList.as_view(),name='meetinglist'),
    url(r'^new/$',MeetingCreate.as_view(),name="newmeeting"),
    url(r'^(?P<pk>[0-9]+)/update$',MeetingUpdate.as_view(),name="editmeeting"),
    url(r'^(?P<pk>[0-9]+)/delete',MeetingDelete.as_view(),name="deletemeeting"),
]