from django.shortcuts import render,redirect,reverse
from django.views import View
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from tender.models import *
from tender.forms import * # Lead_statusForm,LeadForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

class CreateTender(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='tender/tender_form.html'
    form_class = TenderForm
    context_object_name = 'form'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'form':self.form_class})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user = self.request.user
            data.save()
            messages.success(request, 'Success! recorded the tender')
            return redirect('newtender')
        else:
            return render(request,self.template_name,{'forms':form})

class TenderUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = Tender
    form_class = TenderForm
    template_name = 'tender/tender_form.html'
    context_object_name = 'forms'
    #success_url = reverse('index')
    def get_success_url(self):
        return reverse('tenderlist')

class TenderList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'tender/tender_list.html'
    model = Tender
    context_object_name = 'tenders'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['header']='ALL TENDERS'
        return context

class TenderListEvaluation(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'tender/tender_list.html'
    model = Tender
    context_object_name = 'tenders'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['header']='EVALUATIONS'
        context['tenders']=Tender.objects.filter(status='Evaluation').order_by('-id')
        return context

class TenderListWorn(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'tender/tender_list.html'
    model = Tender
    context_object_name = 'tenders'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['header']='WORN TENDERS'
        context['tenders']=Tender.objects.filter(status='Worn').order_by('-id')
        return context

class TenderListFailed(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'tender/tender_list.html'
    model = Tender
    context_object_name = 'tenders'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['header']='FAILED TENDERS'
        context['tenders']=Tender.objects.filter(status='Failed').order_by('-id')
        return context

class TenderDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    """MARKET CENNTER DELETE"""
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Tender
    success_message = "Success!  deleted successfully."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
            messages.success(request,'Success!,Deleted')
        except ProtectedError:
            messages.warning(request,'Faile!,You cannot delete this it is related to others')
            return redirect('tenderlist')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('tenderlist')
