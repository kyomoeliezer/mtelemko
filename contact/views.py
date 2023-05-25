
from django.views.generic import CreateView,ListView,UpdateView
from django.shortcuts import redirect,reverse,resolve_url,render,HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from contact.forms import ContactForm,CompanyForm
from django.contrib import  messages
from contact.models import Contact,Company

class CreateContact(CreateView):
    template_name='contact/contact_form.html'
    form_class = ContactForm
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'forms':self.form_class})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user_id=self.request.user.id
            form.save()

            messages.success(request, 'Success! created contact')
            return redirect('newcontact')
        else:
            return render(request,self.template_name,{'forms':form})

@method_decorator(csrf_exempt,name='dispatch')
class CreateContactOnFly(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name='contact/modal/contact_form_onfly.html'
    form_class = ContactForm
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'forms':self.form_class})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user_id=self.request.user.id
            n=form.save()
            cont=Contact.objects.filter(id=form.id).first()
            htm='<option value="'+str(form.id)+'" selected>'+cont.first_name+' '+cont.last_name+' : '+cont.company+'</option>'
            return HttpResponse(htm)
        else:
            return HttpResponse('0')

class ContactUpdate(UpdateView):
    model = Contact
    template_name = 'contact/contact_update.html'
    form_class = ContactForm
    context_object_name = 'forms'

    def get_success_url(self):
        return reverse('contactlist')


class CreateCompany(CreateView):
    template_name='contact/company_form.html'
    form_class = CompanyForm
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'forms':self.form_class})

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.user_id=self.request.user.id
            form.save()
            messages.success(request, 'Success! created company')
            return redirect('newcompany')
        else:
            return render(request,self.template_name,{'forms':form})

class ContactList(ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
    context_object_name='contacts'
