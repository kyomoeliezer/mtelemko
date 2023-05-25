"""mtelemko URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.views.generic import TemplateView
from lead.views import AppsView #DashboardINDIV


urlpatterns = [
    path('account/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('user/',include('user.urls')),
    path('mproduct/',include('product.urls')),
    path('lead-m/',include('lead.urls')),
    path('tender-m/',include('tender.urls')),
    path('project-m/',include('project.urls')),
    path('mm-invoice/',include('invoice.urls')),
    path('contact/lead-m/', include('contact.urls')),
    path('maccounting/exp-m/', include('account.urls')),

    path('meeting/lead-m/', include('meeting.urls')),
    path('',AppsView.as_view(),name="apps"),
    #path('',LeadList.as_view(),name="leadlist"),
    #path('lead-list',LeadList.as_view(),name="leadlist"),
    path('', TemplateView.as_view(template_name="master_app.html")),


]
#urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
