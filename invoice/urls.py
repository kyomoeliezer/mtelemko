from django.conf.urls import url,re_path
from django.urls import path
from invoice.views import *

urlpatterns= [
    url(r'^services', ServicesList.as_view(), name='services'),
    url(r'^new-services$', CreateService.as_view(), name='new_services'),
    url(r'^uservices/(?P<pk>[0-9]+)/update$', UpdateService.as_view(), name='update_services'),
    url(r'^uservice/(?P<pk>[0-9]+)/delete$', ServiceDelete.as_view(), name='delete_services'),

    url(r'^invoice-pdf/$',PrintInvoice.as_view(),name="invoice"),
    url(r'^(?P<pk>[0-9]+)/invoice-pdf$',PrintInvoicePDF.as_view(),name="invoicepdf"),
    url(r'^(?P<pk>[0-9]+)/delivery-pdf$',PrintDeliveryPDF.as_view(),name="deliverypdf"),
    ###JOB CARD PDF  """PDF USING THE JOBCARD"""
    url(r'^(?P<pk>[0-9]+)/jobcard-pdf$',PrintJobcardPdf.as_view(),name="jobcard_pdf"),
    url(r'^(?P<pk>[0-9]+)/jobcard-update$',UpdateJobcard.as_view(),name="jobcard_update"),

    url(r'^(?P<pk>[0-9]+)/jobcard-new$',NewJobcard.as_view(),name="jobcard_new"),
    url(r'^(?P<pk>[0-9]+)/(?P<job>[0-9]+)/jobcard-detail$',JobcardDetail.as_view(),name="jobcard_detail"),


    url(r'^invoice-new/$',NewQoutation.as_view(),name="newinvoice"),
    url(r'^print-jobcard$',PrintANY.as_view(),name="demojobcard"),
    url(r'^invoice-new-import/$',ImportQoutation.as_view(),name="newinvoice_import"),

    url(r'^invoices-list/$',Invoices.as_view(),name="invoices"),
    url(r'^paid-invoices-list/$',PaidInvoices.as_view(),name="paid_invoices"),
    url(r'^all-for-year/$',YearInvoices.as_view(),name="all_for_year"),
    
    
    url(r'^qoutes-list/$',Qoutes.as_view(),name="qoutes"),
    url(r'^cancelled-list/$',Cancelled.as_view(),name="cancelled"),
    url(r'^(?P<pk>[0-9]+)/invoice$',InvoiceDetail.as_view(),name="invoice_detail"),
    url(r'^duplicate/(?P<pk>[0-9]+)/invoice$',DuplicateIvoince.as_view(),name="invoice_duplicate"),
    
    url(r'^(?P<pk>[0-9]+)/update-invoice-import$',INvoiceImportUpdate.as_view(),name="invoice_update_import"),
    url(r'^(?P<pk>[0-9]+)/update-invoice$',INvoiceUpdate.as_view(),name="invoice_update"),


    url(r'^(?P<pk>[0-9]+)/qoute2invoice$',Move2Invoice.as_view(),name="qoute2invoice"),
    url(r'^(?P<pk>[0-9]+)/delete-trash-it$',Move2DELETE.as_view(),name="qoute2delete"),
    url(r'^(?P<pk>[0-9]+)/invoice2cancelled$',Move2Cancel.as_view(),name="inv2cancel"),
    url(r'^(?P<pk>[0-9]+)/invoice2paid$',Move2Paid.as_view(),name="inv2paid"),
    url(r'^(?P<pk>[0-9]+)/invoice2unpaid$',Move2Unpaid.as_view(),name="inv2unpaid"),
    url(r'^(?P<pk>[0-9]+)/invoice2qoute$',Move2Qoute.as_view(),name="move2qoute"),

    #####InvoiceDistributionAdd
    url(r'^(?P<pk>[0-9]+)/distribute$',InvoiceDistributionAdd.as_view(),name="exp_distribute_add"),
    url(r'^(?P<pk>[0-9]+)/distribute/delete$',InvoiceDistributionDelete.as_view(),name="exp_distribute_delete"),



    
    



]
