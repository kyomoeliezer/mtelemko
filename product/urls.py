#from django.urls import include,path,re_path
from django.conf.urls import url
from product.views import ProductCreate,ProductList,ProductUpdate

urlpatterns=[
    url(r'^$',ProductList.as_view(),name='productlist'),
    url(r'^new/$',ProductCreate.as_view(),name="newproduct"),
    url(r'^(?P<pk>[0-9]+)/update$',ProductUpdate.as_view(),name="editproduct"),
    #url(r'^(?P<pk>[0-9]+)/delete',MeetingDelete.as_view(),name="deletemeeting"),
]