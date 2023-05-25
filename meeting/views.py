from django.shortcuts import render,redirect,resolve_url,reverse
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from meeting.models import Meeting
from meeting.forms import MeetingForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.

class MeetingCreate(CreateView):
    form_class = MeetingForm
    template_name = 'meeting/meeting_form.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'forms':self.form_class})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user = self.request.user
            data.save()
            messages.success(request, 'Success! scheduled the meeting')
            return  redirect('newmeeting')
        else:
            return render(request,self.template_name,{'forms':form})

class MeetingUpdate(UpdateView):
    model = Meeting
    template_name = 'meeting/meeting_update.html'
    form_class = MeetingForm
    context_object_name = 'forms'
    def get_success_url(self):
        return reverse('meetinglist')

class MeetingUpdate(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    context_object_name = 'forms'
    model = Meeting
    template_name = 'meeting/meeting_update.html'
    form_class = MeetingForm
    #fields=['date','meeting_time','agenda','desc','meeting_status','lead']

    #success_url = reverse('index')
    def get_success_url(self):
        return reverse('meetinglist')

class MeetingList(ListView):
    model=Meeting
    context_object_name = 'meeting'
    template_name = 'meeting/meeting_list.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['meeting']=Meeting.objects.filter(user=self.request.user).order_by('-id')
        return context

class MeetingDelete(DeleteView):
    model = Meeting
    success_message = "Success!  deleted successfully."


    def get(self, request, *args, **kwargs):
            messages.success(self.request, self.success_message)
            return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('meetinglist')

