from django.conf.urls import url,re_path
from django.urls import path
from project.views import * #CreateLead,CreateStatus,LeadList,StatusList,LeadUpdate,LeadstatusUpdate,LeadDetail

urlpatterns= [
    url(r'^new-project/$',CreateProject.as_view(),name="newproject"),
    url(r'^completed',ProjectListCompleted.as_view(),name="completedlist"),
    url(r'^$',ProjectList.as_view(),name="projectlist"),
    url(r'^tasks',TasksList.as_view(),name="tasks"),
    url(r'^reminder',TaskRemainder.as_view(),name="reminder"),
    
    url(r'^(?P<pk>[0-9]+)/update/$',ProjectUpdate.as_view(),name="updateproject"),
    url(r'^(?P<pk>[0-9]+)/delete/$',ProjectDelete.as_view(),name="deleteproject"),
    url(r'^(?P<pk>[0-9]+)/project-detail/$',ProjectDetail.as_view(),name="projectdetail"),
    url(r'^(?P<pk>[0-9]+)/project-add-cost/$',AddProjectCost.as_view(),name="addcost"),
    url(r'^(?P<pk>[0-9]+)/project-add-task/$',TaskAdd.as_view(),name="addtask"),
    url(r'^(?P<pk>[0-9]+)/project-edit-task/$',EditProjectTask.as_view(),name="edittask"),
    url(r'^(?P<pk>[0-9]+)/project-workon-task/$',TaskWorkon.as_view(),name="workontask"),
    url(r'^(?P<pk>[0-9]+)/project-delete-task/$',TaskDelete.as_view(),name="deletetask"),
    url(r'^(?P<pk>[0-9]+)/edit-cost/$',EditProjectCost.as_view(),name="editcost"),
    url(r'^(?P<pk>[0-9]+)/del-cost/$',CostDelete.as_view(),name="deletecost"),
    
   


]
