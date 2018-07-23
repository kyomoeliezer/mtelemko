from django.shortcuts import render,redirect,resolve_url,reverse
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from meeting.models import Meeting
from meeting.forms import MeetingForm

# Create your views here.

class MeetingCreate(CreateView):
    form_class = MeetingForm
    template_name = 'meeting/meeting_form.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'form':self.form_class})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Success! scheduled the meeting')
            return  redirect('newmeeting')
        else:
            return render(request,self.template_name,{'form':form})

class MeetingUpdate(UpdateView):
    model = Meeting
    template_name = 'meeting/meeting_update.html'
    fields=['agenda','desc','lead','meeting_status','meeting_time','date']
    def get_success_url(self):
        return reverse('meetinglist')

class MeetingList(ListView):
    model=Meeting
    context_object_name = 'meeting'
    template_name = 'meeting/meeting_list.html'

class MeetingDelete(DeleteView):
    model = Meeting
    success_message = "Success!  deleted successfully."


    def get(self, request, *args, **kwargs):
            messages.success(self.request, self.success_message)
            return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('meetinglist')

