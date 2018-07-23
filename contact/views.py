
from django.views.generic import CreateView,ListView,UpdateView
from django.shortcuts import redirect,reverse,resolve_url,render
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
            form.save(commit=True)

            messages.success(request, 'Success! created contact')
            return redirect('newcontact')
        else:
            return render(request,self.template_name,{'forms':form})

class ContactUpdate(UpdateView):
    model = Contact
    template_name = 'contact/contact_update.html'
    fields=['first_name','middle_name','last_name','has_a_company','mobile','email','company']

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
            form.save(commit=True)

            messages.success(request, 'Success! created company')
            return redirect('newcompany')
        else:
            return render(request,self.template_name,{'forms':form})

class ContactList(ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
    context_object_name='contacts'