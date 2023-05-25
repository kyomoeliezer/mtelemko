from django.shortcuts import render,redirect,reverse,HttpResponse
from django.views import View
from django.contrib import messages
from django.views.generic import CreateView,ListView,UpdateView,DetailView,DeleteView
from django.template.loader import render_to_string
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from project.models import *
from common.functions import *
from project.forms import * # Lead_statusForm,LeadForm
from django.db.models import FloatField, F,Sum,Case,When,IntegerField,Value,Min,Q,Count
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import datetime

class CreateProject(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='project/project_form.html'
    form_class = ProjectForm
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'form':self.form_class,'header':'NEW PROJECT'})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user = self.request.user
            data.save()
            messages.success(request, 'Success! recorded the project')
            return redirect('newproject')
        else:
            return render(request,self.template_name,{'form':form,'header':'NEW PROJECT'})

class ProjectUpdate(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = Project
    form_class = ProjectUpdateForm
    template_name = 'project/project_update_form.html'
    context_object_name = 'forms'
    success_message = 'Success! updated'
    #success_url = reverse('index')
    def get_success_url(self):
        return reverse('projectdetail',kwargs={'pk':self.kwargs['pk']})
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']='UPDATE PROJECT'
        return context

class ProjectList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['header']='ALL PROJECTS'
        context['projects']=Project.objects.filter(~Q(status='Completed')).order_by('-id')
        return context

class ProjectListCompleted(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'project/project_list.html'
    model = Project
    context_object_name = 'projects'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['header']='COMPLETED PROJECT'
        context['projects']=Project.objects.filter(status='Completed').order_by('-id')
        return context

class ProjectDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    """MARKET CENNTER DELETE"""
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Project
    success_message = "Success!  deleted successfully."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
            messages.success(request,'Success!,Deleted')
        except ProtectedError:
            messages.warning(request,'Faile!,You cannot delete this it is related to others')
            return redirect('projectlist')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('projectlist')

class ProjectDetail(LoginRequiredMixin,DetailView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = "project/project_profile.html"
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = ProjectTasks.objects.filter(project_id=self.kwargs['pk'])
        context['costs'] = costs=ProjectAmounts.objects.filter(project_id=self.kwargs['pk'])
        context['tasks'] = costs=ProjectTasks.objects.filter(project_id=self.kwargs['pk'])
        context['costs_total']=0
        if costs:
            context['costs_total']=ProjectAmounts.objects.filter(project_id=self.kwargs['pk']).aggregate(su=Sum('amount'))['su']
        
        return context

@method_decorator(csrf_exempt,name='dispatch')
class AddProjectCost(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = ProjectAmounts
    template_name='project/modal/project_cost.html'
    form_class = CostForm
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']='ADD PROJECT COST'
        context['listid']=self.kwargs['pk']
        return context

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.project_id = self.kwargs['pk']
            data.user = self.request.user
            data.save()
            messages.success(request, 'Success! recorded the project cost')
            return redirect(reverse('projectdetail',kwargs={'pk':self.kwargs['pk']}))

@method_decorator(csrf_exempt,name='dispatch')
class EditProjectCost(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = ProjectAmounts
    template_name='project/modal/project_cost_update.html'
    form_class = CostForm
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']='EDIT PROJECT COST'
        context['lists']=ProjectAmounts.objects.filter(id=self.kwargs['pk'])
        context['listid']=self.kwargs['pk']
        return context

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            ProjectAmounts.objects.filter(id=self.kwargs['pk']).update(cost_name=request.POST.get('cost_name'),amount=request.POST.get('amount'))
            
            messages.success(request, 'Success! recorded the project cost')
            return HttpResponse('1')


class CostDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    """COST DELE"""
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = ProjectAmounts
    success_message = "Success!  deleted successfully."
    def post(self, request, *args, **kwargs):
        id=ProjectAmounts.objects.filter(id=self.kwargs['pk']).first().project_id
        try:
            return self.delete(request, *args, **kwargs)
            messages.success(request,'Success!,Deleted')
        except ProtectedError:
            messages.warning(request,'Faile!,You cannot delete this it is related to others')
            return redirect(reverse('projectdetail',kwargs={'pk':id}))

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)

    def get_success_url(self):
        id=ProjectAmounts.objects.filter(id=self.kwargs['pk']).first().project_id
        return reverse('projectdetail',kwargs={'pk':id})
        
############################################################################
############PROJECT TASK####################################################
@method_decorator(csrf_exempt,name='dispatch')
class TaskAdd(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = Project
    template_name='task/modal/task_new.html'
    form_class = TaskForm
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']='New Task'
        context['project']=Project.objects.filter(id=self.kwargs['pk']).first()
        context['listid']=self.kwargs['pk']
        return context

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            ProjectTasks.objects.create(name=request.POST.get('name'),desc=request.POST.get('desc'),end_date=request.POST.get('end_date'),start_date=request.POST.get('start_date'),responsible_id=request.POST.get('responsible'),project_id=self.kwargs['pk'],user_id=request.user.id)
            
            messages.success(request, 'Success! recorded the project task')
            return HttpResponse('1')
####EDIT
@method_decorator(csrf_exempt,name='dispatch')
class EditProjectTask(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = ProjectTasks
    template_name='task/modal/task_update.html'
    form_class = TaskForm
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']='Edit Task'
        context['reslist']=User.objects.all()
        context['lists']=ProjectTasks.objects.filter(id=self.kwargs['pk'])
        context['listid']=self.kwargs['pk']
        return context

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            ProjectTasks.objects.filter(id=self.kwargs['pk']).update(name=request.POST.get('name'),desc=request.POST.get('desc'),end_date=request.POST.get('end_date'),start_date=request.POST.get('start_date'),responsible_id=request.POST.get('responsible'))
            
            messages.success(request, 'Success! updated the project task')
            return HttpResponse('1')

####WORKON TASK
@method_decorator(csrf_exempt,name='dispatch')
class TaskWorkon(LoginRequiredMixin,UpdateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    model = ProjectTasks
    template_name='task/modal/task_info.html'
    form_class = TaskWorkonForm
    context_object_name = 'forms'

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']='Work Task'
        context['lists']=ProjectTasks.objects.filter(id=self.kwargs['pk'])
        context['listid']=self.kwargs['pk']
        return context

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            ProjectTasks.objects.filter(id=self.kwargs['pk']).update(desc=request.POST.get('desc'),end_date=request.POST.get('end_date'),status=request.POST.get('status'))
            
            messages.success(request, 'Success! worked on the project task')
            return HttpResponse('1')


class TaskDelete(LoginRequiredMixin,DeleteView,SuccessMessageMixin):
    """COST DELE"""
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = ProjectTasks
    success_message = "Success!  deleted successfully."
    def post(self, request, *args, **kwargs):
        id=ProjectTasks.objects.filter(id=self.kwargs['pk']).first().project_id
        try:
            return self.delete(request, *args, **kwargs)
            messages.success(request,'Success!,Deleted')
        except ProtectedError:
            messages.warning(request,'Faile!,You cannot delete this it is related to others')
            return redirect(reverse('projectdetail',kwargs={'pk':id}))

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)

    def get_success_url(self):
        id=ProjectTasks.objects.filter(id=self.kwargs['pk']).first().project_id
        return reverse('projectdetail',kwargs={'pk':id})

class TasksList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'task/task_list.html'
    model = ProjectTasks
    context_object_name = 'tasks'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data()
        context['header']='TASK ON PROGRESS'
        context['tasks']=ProjectTasks.objects.filter(~Q(status='completed')&Q(start_date__lte=datetime.today())).order_by('-id')
        context['upcomming']=ProjectTasks.objects.filter(~Q(status='completed')&~Q(start_date__lte=datetime.today())).order_by('start_date')
        return context

class TaskRemainder(View):
    def get(self,request,*args,**kwargs):
        subject='Today Task Reminder ('+datetime.today().strftime("%A %B  %d, %Y")+")"
        message='message'
        message = render_to_string('task/email/remainder_mail.html', {
            'name': 'M-Sales',
            'date':datetime.today(),
            'message':message,
            'tasks':ProjectTasks.objects.filter(~Q(status='completed')&Q(start_date__lte=datetime.today())).order_by('-end_date')
        })
        send_mail('eliezer.kyomo@mifumotz.com',subject,message)
        return HttpResponse(1)
        
