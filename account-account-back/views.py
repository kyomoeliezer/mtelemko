from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,View,FormView,DeleteView,DetailView
from django.shortcuts import redirect,reverse,resolve_url,render,HttpResponse
from django.db.models import FloatField, F,Sum,Case,When,IntegerField,Value,Min,Q,Count,Max

from django.utils.decorators import method_decorator
from user.decorators import *

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import  messages
import datetime
from payment.views import create_payment
from account.common import *


from account.models import *
from account.forms import *

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class RegisterExpense(LoginRequiredMixin,CreateView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'expenses/new.html'
    form_class = ExpenseForm
    context_object_name = 'forms'
    header='Record Expense'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        context['forms'] = self.form_class
        return context

    def post(self,request, *args,**kwargs ):
        form = self.form_class(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            ###Create payment
            amount=request.POST.get('amount')
            payment=create_payment(amount,form.desc,form.date,request.user,1,request.POST.get('account'),request.POST.get('trans_account'))
            ####JOURNALIZE
            insert_on_journal(payment.id,form.date,form.desc,amount,amount,form.invoice,form.champion,request.POST.get('account'),request.POST.get('trans_account'))
            insert_on_bankjournal(payment.id, form.date, form.desc, 0,amount, form.invoice, form.champion, request.POST.get('account'))
            form.dr=request.POST.get('amount')
            form.payment_id=payment.id
            form.save()
            messages.success(request, 'Success! created company')
            return redirect('expenses')
        else:
            return render(request,self.template_name,{'forms':form})

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class ExpenseList(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'expenses/expenses.html'
    context_object_name = 'lists'
    header = ' Expense Lists'
    model=Expensejournal
    order=['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['header'] = self.header
        context['lists']=Expensejournal.objects.all().order_by('-id')
        context['exsum'] = Expensejournal.objects.filter(date__year=datetime.datetime.today().year).aggregate(sum2=Sum('dr'))['sum2']
        return context

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class ExpenseInGroups(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    template_name = 'expenses/expenses_by_account.html'
    context_object_name = 'lists'
    header = ' Expense Lists'
    model=Expensejournal
    order=['-id']

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data()
        year=self.request.GET.get('year')
        if not year:
            year=datetime.datetime.today().year
        context['header'] = self.header+' ['+str(year)+']'
        context['lists']=Expensejournal.objects.filter(date__year=year).values(accountname=F('account__name')).annotate(
          AccSum=Sum('dr'),no=Count('id')
        )
        context['exsum'] = Expensejournal.objects.filter(date__year=year).aggregate(sum2=Sum('dr'))['sum2']
        return context
################################################
###########DELETE DELETE#############################
deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class DeleteTransaction(LoginRequiredMixin,View):
    login_url = reverse_lazy('login-user')
    redirect_field_name = 'next'
    def get(self,request,*args,**kwargs):
        delete_transaction(self.kwargs['pk'])
        messages.success(request,'Deleted transaction ')
        return redirect(reverse('expenses'))

################################
###########CREATE CHART#############
####CHARTS
deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class CreateChart(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Chartofaccount
    fields = ['name','accountno']
    template_name = 'chart/new.html'
    context_object_name = 'form'
    header='New Chart of Account'
    success_url = reverse_lazy('charts')

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class UpdateChartofAccount(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Chartofaccount
    fields = ['name','accountno']
    template_name ='chart/new.html'
    context_object_name = 'form'
    header='Update Chart'
    success_url = reverse_lazy('charts')
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class ChartofaccountDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Chartofaccount
    success_message = "Success!  deleted charts."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request,'Huwezi kufuta chart hii, kuna data zinategemea data  hii')
            return redirect('charts')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('charts')

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class ChartsList(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Chartofaccount
    context_object_name = 'lists'
    template_name = 'chart/lists.html'
    header='Charts of accounts'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

###END CHART###########################
################################
###########CREATE ACCOUNTCATEGORY#############
####CACCOUNT CATEGORY
deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class CreateAccountcategory(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Accountcategory
    fields = ['name','accountno','chart']
    template_name = 'categoryaccount/new.html'
    context_object_name = 'form'
    header='New Account Category'
    success_url = reverse_lazy('accountcategories')

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class UpdateAccountcategory(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Accountcategory
    fields = ['name','accountno','chart']
    template_name ='categoryaccount/new.html'
    context_object_name = 'form'
    header='Update Category'
    success_url = reverse_lazy('accountcategories')
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class CategoryaccountDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Accountcategory
    success_message = "Success!  deleted charts."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request,'Huwezi kufuta Account category hii, kuna data zinategemea data  hii')
            return redirect('accountcategories')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('accountcategories')

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class AccountcategoryList(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Accountcategory
    context_object_name = 'lists'
    template_name = 'categoryaccount/lists.html'
    header='Category accounts'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

###END ACCOUNT CATEGORY###########################

################################
###########CREATE ACCOUNT#############
####CACCOUNT ACCOUNT
deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class CreateAccount(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Account
    fields = ['name','accountno','chart','accountcategory','is_cashaccount','is_bankaccount']
    template_name = 'account/new.html'
    context_object_name = 'form'
    header='New Account '
    success_url = reverse_lazy('accounts')

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class UpdateAccount(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Account
    fields =  ['name','accountno','chart','accountcategory','is_cashaccount','is_bankaccount']
    template_name ='account/new.html'
    context_object_name = 'form'
    header='Update Account'
    success_url = reverse_lazy('accounts')
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class AccountDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Account
    success_message = "Success!  deleted charts."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request,'Huwezi kufuta Account  hii, kuna data zinategemea data  hii')
            return redirect('accounts')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('accounts')

deco_user=[all_account_permission]
@method_decorator(deco_user,name='dispatch')
class AccountList(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Account
    context_object_name = 'lists'
    template_name = 'account/lists.html'
    header=' Accounts'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

###END ACCOUNT ###########################


