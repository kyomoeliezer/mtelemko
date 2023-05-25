from django.shortcuts import redirect,reverse,resolve_url,render,HttpResponse
from django.views import View
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from lead.models import * # Lead_status,Lead
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from meeting.models import Meeting
from invoice.models import Invoice
from lead.forms import * # Lead_statusForm,LeadForm,CampaignForm,TargetForm,TargetFormVisitStatus
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q,Sum,F,Min,Max,IntegerField,FloatField,Count,Case,When,Value,ProtectedError
from django.db.models.functions import ExtractWeek, ExtractYear, ExtractMonth
from django.db.models.functions import TruncMonth
from invoice.models import InvoiceLine
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse_lazy
import datetime


class AppsView(LoginRequiredMixin,View):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = "apps/index.html"
    model = Lead
    def get(self,request):
        return render(request,self.template_name)

class CreateLead(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/lead_form.html'
    form_class = LeadForm
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'forms':self.form_class})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user = self.request.user
            data.save()
            Meeting.objects.create(lead_id=data.pk,date=datetime.datetime.today(),agenda=self.request.POST.get('title'),user=self.request.user)
            messages.success(request, 'Success! created contact')
            return redirect('newlead')
        else:
            return render(request,self.template_name,{'forms':form})


class CreateStatus(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/status_form.html'
    form_class = Lead_statusForm
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'forms':self.form_class})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)

            messages.success(request, 'Success! created status')
            return redirect('newstatus')
        else:
            return render(request,self.template_name,{'forms':form})

class LeadUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = Lead
    template_name = 'lead/lead_edit_form.html'
    fields=['leadmanager','title','desc','expected_sale_amount','expected_closing_date','contact','status','status_info','score','campaign']
    #success_url = reverse('index')

    def get_success_url(self):
        return reverse('leadlist')
class LeadstatusUpdate(UpdateView):
    model = Lead_status
    template_name = 'lead/status_update.html'
    fields=['name','order']

    def get_success_url(self):
        return reverse('statuslist')

class LeadList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'lead/lead_list.html'
    model = Lead
    context_object_name = 'leads'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['leads']=Lead.objects.filter(user=self.request.user).order_by('-created_at')
        return context


class StatusList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'lead/status_list.html'
    model = Lead_status
    context_object_name = 'status'

class LeadDetail(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = "lead/lead_profile.html"
    model = Lead

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meetings'] = Meeting.objects.filter(lead_id=self.kwargs['pk'])
        context['maxact']=LeadActivity.objects.filter(lead_id=self.kwargs['pk']).aggregate(mx=Max('id'))
        context['activities']=LeadActivity.objects.filter(lead_id=self.kwargs['pk']).order_by('-id')
        return context
        
class LEADDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    """LEAD DELE"""
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Lead
    success_message = "Success!  deleted successfully."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
            messages.success(request,'Success!,Deleted')
        except ProtectedError:
            messages.warning(request,'Faile!,You cannot delete this it is related to others')
            return redirect('leadlist')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('leadlist')


########################################################################
#####COMPAIGN                                                 ##########
########################################################################
class CreateCampaign(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = Campaign
    template_name='campaign/campaign_form.html'
    form_class = CampaignForm
    context_object_name = 'forms'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'forms':self.form_class})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user = self.request.user
            data.save()
            messages.success(request, 'Success! created compaign')
            return redirect('campaigns')
        else:
            return render(request,self.template_name,{'forms':form})

class CampaignList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='campaign/campaigns.html'
    model = Campaign
    context_object_name = 'campaigns'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header']='COMPAIGNS'
        context['campaigns']=Campaign.objects.order_by('-id')

        return context

class CampaignDelete(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    """CAMPAIGN DELETE"""
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Campaign
    success_message = "Success!  deleted successfully."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
            messages.success(request,'Success!,Deleted')
        except ProtectedError:
            messages.warning(request,'Faile!,You cannot delete this it is related to others')
            return redirect('campaigns')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('campaigns')



class CampaignUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = Campaign
    context_object_name = 'form'
    template_name='campaign/campain_update.html'
    fields=['name','desc','script','target_lead_no','campaign_start','campaign_end']
    success_message = "Success!  updated successfully."
    #success_url = reverse('index')
    
    def get_success_url(self):
        return reverse('campaigns')

class CompaignDetail(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = "campaign/campaign_detail.html"
    model = Campaign
    context_object_name = 'camp'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leads'] = Lead.objects.filter(campaign_id=self.kwargs['pk']).values(stat=F('status__name')).annotate(
                total=Count('id'),
                opp=Count('id'),
            opp_val=Sum('expected_sale_amount'))
        context['invoices'] = InvoiceLine.objects.filter(invoice__campaign_id=self.kwargs['pk']).values(stat=F('invoice__invoice_status')).annotate(
                total=Count('invoice_id',distinct=True),
                val=Sum(F('qty')*F('price'),output_field=FloatField()))
        context['contact_total']=TargetContact.objects.filter(campaign_id=self.kwargs['pk']).count()
        context['visted']=TargetContact.objects.filter(Q(campaign_id=self.kwargs['pk'])&~Q(visit_desc__isnull=True)).count()
        context['contacts'] = TargetContact.objects.filter(Q(campaign_id=self.kwargs['pk'])&~Q(status='finding')).values('status').annotate(
                total=Count('id'))
        return context


###############################LEAD
##LEAD ACTIVITIES
@method_decorator(csrf_exempt,name='dispatch')
class LeadActivityOnFly(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/modal/activity_modal.html'
    form_class = LeadActivityForm
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'form':self.form_class,'lead_id':self.kwargs['pk']})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.created_by_id=self.request.user.id
            form.lead_id=self.kwargs['pk']
            form.followup_date=datetime.datetime.now()
            form.save()

            return HttpResponse('Added activity')
        else:
            return HttpResponse('0')

@method_decorator(csrf_exempt,name='dispatch')
class LeadActivityEditOnFly(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/modal/activity_modal.html'
    model = LeadActivity
    form_class = LeadActivityForm
    context_object_name = 'forms'
    def get_context_data(self, **kwargs):
        conte=super().get_context_data()
        conte['pk']=self.kwargs['pk']
        return conte

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            LeadActivity.objects.filter(id=self.kwargs['pk']).update(followup=request.POST.get('followup'),followup_by_id=request.POST.get('followup_by'),followup_date=request.POST.get('followup_date'))

            return HttpResponse('Updated activity')
        else:
            return HttpResponse('0')

class LeadActivityDelete(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    """LEADACTIVITY DELETE"""
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = LeadActivity
    success_message = "Success!  deleted successfully."

    def post(self, request, *args, **kwargs):
        lead_id=LeadActivity.objects.get(id=self.kwargs['pk']).lead_id
        try:
            return self.delete(request, *args, **kwargs)
            messages.success(request,'Success!,Deleted')

        except ProtectedError:
            messages.warning(request,'Faile!,You cannot delete this it is related to others')
            return redirect( reverse('leaddetail',kwargs={'pk':lead_id}))

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)

    def get_success_url(self):
        lead_id=LeadActivity.objects.get(id=self.kwargs['pk']).lead_id
        return reverse('leaddetail',kwargs={'pk':lead_id})



####################################
####################################
####TARGET CONTACT################
class CreateContactTarget(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = TargetContact
    template_name='lead/target/target_form.html'
    form_class = TargetForm
    context_object_name = 'forms'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'forms':self.form_class})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user = self.request.user
            data.save()
            messages.success(request, 'Success! created target contact')
            return redirect('targetcontacts')
        else:
            return render(request,self.template_name,{'forms':form})

class ContactTargetList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/target/targets.html'
    model = TargetContact
    context_object_name = 'targets'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header']='CONTACTS TARGETS'
        context['targets']=TargetContact.objects.filter(worked_on=False,user=self.request.user).order_by('-id')
        return context

class ContactTargetAnalysis(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/target/targets.html'
    model = TargetContact
    context_object_name = 'targets'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['analysis']=analysis=TargetContact.objects.filter(user=self.request.user).annotate(month=ExtractMonth('created_at')).values('month').annotate(c=Count('id')).values('month', 'c')#annotate(year=ExtractYear('created_at')).annotate(Madate=Max('created_at')).annotate(Mindate=Min('created_at')).annotate(week=ExtractWeek('created_at')).values('year', 'week','Madate','Mindate').annotate(contacts=Count('id'))
       
        context['header']='CONTACTS TARGETS'
        context['targets']=TargetContact.objects.filter(user=self.request.user).order_by('-created_at')
        return context

class ContactTargetList_done(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/target/target_done.html'
    model = TargetContact
    context_object_name = 'targets'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header']='DONE CONTACTS'
        context['targets']=TargetContact.objects.filter(worked_on=True,user=self.request.user).order_by('-id')
        return context

class ContactTargetList_contacts(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/target/target_done.html'
    model = TargetContact
    context_object_name = 'targets'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header']='QUALIFIED CONTACTS'
        context['targets']=TargetContact.objects.filter(worked_on=True,status='contact',user=self.request.user).order_by('-id')
        return context

class ContactTargetList_Finding(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/target/targets.html'
    model = TargetContact
    context_object_name = 'targets'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header']='FINDING A WAY IN'
        context['targets']=TargetContact.objects.filter(worked_on=True,status='finding',user=self.request.user).order_by('-id')
        return context

class ContactTargetList_Dropped(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='lead/target/target_dropped.html'
    model = TargetContact
    context_object_name = 'targets'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header']='DROPPED TARGETS'
        context['targets']=TargetContact.objects.filter(worked_on=True,status='dropped',user=self.request.user).order_by('-id')
        return context




class ContactTargetDelete(LoginRequiredMixin,SuccessMessageMixin,DeleteView):
    """CONTACT TARGET DELETE"""
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = TargetContact
    success_message = "Success!  deleted successfully."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
            messages.success(request,'Success!,Deleted')
        except ProtectedError:
            messages.warning(request,'Faile!,You cannot delete this it is related to others')
            return redirect('targetcontacts')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('targetcontacts')



class ContactTargetUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = TargetContact
    context_object_name = 'form'
    template_name='lead/target/target_form_update.html'
    fields=['name','location','main_activity','campaign','mobile']
    success_message = "Success!  updated successfully."
    #success_url = reverse('index')
    def get_context_data(self, **kwargs):
        kwargs['header']='UPDATE TARGET CONTACT'
        
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse('targetcontacts')

##############UPDATE STATUS OF OF THE LEAD########
class ContactTargetUpdateVisit(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    form_class=TargetFormVisitStatus
    model = TargetContact
    context_object_name = 'form'
    template_name='lead/target/target_change_status.html'
    #fields=['name','location','main_activity','campaign','mobile']
    success_message = "Success!  updated successfully."
    #success_url = reverse('index')
    def get_context_data(self, **kwargs):
        kwargs['header']='VISIT STATUS'
        return super().get_context_data(**kwargs)
    
    def get_success_url(self):
        return reverse('targetcontacts')
    
    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.worked_on=True
        self.object.save()
        messages.success(self.request,'Succes!, Updated')
        return HttpResponseRedirect(self.get_success_url())

#######


class WorkedOnContactAlread(View):
    def get(self,request,*args,**kwargs):
        TargetContact.objects.filter(id=self.kwargs['pk']).update(worked_on=True)
        messages.success(self.request,'Succes! marked')
        return redirect('targetcontacts')
        
        

######END TARGET CONTACT##############

class DashboardINDIV(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = "dashboard.html"
    model = Lead
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leads']=Lead.objects.filter(~Q(status__name='Lost')&Q(user_id=self.request.user.id)).count()
        context['dis']=Lead.objects.filter(Q(status__name='Lost')&Q(user_id=self.request.user.id)).count()
        context['qoute']=Invoice.objects.filter(Q(user_id=self.request.user.id)).count()
        context['closed']=Lead.objects.filter(Q(status__name='Sale')&Q(user_id=self.request.user.id)).count()
        cl=Lead.objects.filter(Q(status__name='Sale')&Q(user_id=self.request.user.id))
        q=Lead.objects.filter(Q(status__name='Qoute')&Q(user_id=self.request.user.id))
        clamount=qamount=0
        if q:
           qamount=Lead.objects.filter(~Q(status__name='Qoute')&Q(user_id=self.request.user.id)).aggregate(mano=Sum('expected_sale_amount'))['mano'] 
        context['qamount']=qamount  
        if cl:
           clamount=Lead.objects.filter(~Q(status__name='Qoute')&Q(user_id=self.request.user.id)).aggregate(mano=Sum('expected_sale_amount'))['mano'] 
        context['clamount']=clamount  
        
        return context



class Dashboard(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = "dashboard.html"
    model = Lead
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['leads']=Lead.objects.filter(~Q(status__name='Lost')).count()
        context['dis']=Lead.objects.filter(Q(status__name='Lost')).count()
        context['qoute']=Lead.objects.filter(~Q(status__name='Qoute')).count()
        context['closed']=Lead.objects.filter(~Q(status__name='Sale')).count()
        return context
