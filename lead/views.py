from django.shortcuts import render,redirect,reverse
from django.views import View
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView,DetailView
from lead.models import Lead_status,Lead
from meeting.models import Meeting
from lead.forms import Lead_statusForm,LeadForm

class CreateLead(CreateView):
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
            messages.success(request, 'Success! created contact')
            return redirect('newlead')
        else:
            return render(request,self.template_name,{'forms':form})


class CreateStatus(CreateView):
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

class LeadUpdate(UpdateView):
    model = Lead
    template_name = 'lead/lead_edit_form.html'
    fields=['title','desc','expected_sale_amount','expected_closing_date','contact','status','score']
    #success_url = reverse('index')
    def get_success_url(self):
        return reverse('leadlist')
class LeadstatusUpdate(UpdateView):
    model = Lead_status
    template_name = 'lead/status_update.html'
    fields=['name','order']

    def get_success_url(self):
        return reverse('statuslist')

class LeadList(ListView):
    template_name = 'lead/lead_list.html'
    model = Lead
    context_object_name = 'leads'

class StatusList(ListView):
    template_name = 'lead/status_list.html'
    model = Lead_status
    context_object_name = 'status'

class LeadDetail(DetailView):
    template_name = "lead/lead_profile.html"
    model = Lead

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['meetings'] = Meeting.objects.filter(lead_id=self.kwargs['pk'])
        return context


