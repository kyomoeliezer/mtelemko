import os
import csv
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,UpdateView,View,FormView,DeleteView,DetailView
from django.shortcuts import redirect,reverse,resolve_url,render,HttpResponse
from django.db.models import FloatField, F,Sum,Case,When,IntegerField,Value,Min,Q,Count,Max
from lead.utility import *
from invoice.models import *
from invoice.forms import *
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import  messages
import datetime
from account.models import Expensejournal
# Create your views here.

###
################################
###########CREATE SERVICE#############
####ROLES
class CreateService(LoginRequiredMixin,CreateView):
	redirect_field_name = 'next'
	login_url = reverse_lazy('login_user')
	model = ServiceCategory
	fields = ['name','desc']
	template_name = 'invoice/services/new.html'
	context_object_name = 'form'
	header='New Service'
	success_url = reverse_lazy('services')

	def get_context_data(self, **kwargs):
		context=super().get_context_data()
		context['header']=self.header
		return context

class UpdateService(LoginRequiredMixin,UpdateView):
	redirect_field_name = 'next'
	login_url = reverse_lazy('login_user')

	model = ServiceCategory
	fields = ['name','desc']
	template_name = 'invoice/services/new.html'
	context_object_name = 'form'
	header='Update Service'
	success_url = reverse_lazy('services')
	def get_context_data(self, **kwargs):
		context=super().get_context_data()
		context['header']=self.header
		return context

class ServiceDelete(LoginRequiredMixin,DeleteView):
	redirect_field_name = 'next'
	login_url = reverse_lazy('login_user')
	model = ServiceCategory
	success_message = "Success!  deleted service."
	def post(self, request, *args, **kwargs):
		try:
			return self.delete(request, *args, **kwargs)
		except ProtectedError:
			messages.warning(request,'Huwezi kufuta permission hii, kuna data zinategemea data  hii')
			return redirect('services')

	def get(self, request, *args, **kwargs):
			return self.post(request, *args, **kwargs)
	def get_success_url(self):
		return reverse('services')

class ServicesList(LoginRequiredMixin,ListView):
	redirect_field_name = 'next'
	login_url = reverse_lazy('login_user')
	model = ServiceCategory
	context_object_name = 'lists'
	template_name = 'invoice/services/lists.html'
	header='Service'
	def get_context_data(self, **kwargs):
		context=super().get_context_data()
		context['header']=self.header
		return context


###END Service###########################


##@

def invoice_no(no):
	date=datetime.datetime.today().year
	#date=str(date.strftime('%Y'))
	if int(no) <10:
		return 'MIF'+str(date)+'-'+'00'+str(no)

	elif int(no) <100:
		return 'MIF'+str(date)+'-'+'0'+str(no)
	else:
		return  'MIF'+str(date)+'-'+str(no)


class PrintANY(View):
	def get(self,request):
		content={}
		pdf = render_to_pdf('invoice/pdf/jobcard.html', content,'file')
		if pdf:
			response = HttpResponse(pdf, content_type='application/force-download')
			content = "attachment; filename=JOBCARD.pdf  "
			response['Content-Disposition'] = content
			return response
		else:
			return HttpResponse("Not found")


class PrintInvoice(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	template_name = 'invoice/pdf/invoice_pdf.html'
	context_object_name = 'lists'
	def get(self,request, *args, **kwargs):
		pdf = render_to_pdf(self.template_name, {},'file')
		if pdf:
			response = HttpResponse(pdf, content_type='application/force-download')
			content = "attachment; filename=INVOICE001.pdf  "
			response['Content-Disposition'] = content
			return response
		else:
			return HttpResponse("Not found")
			
class PrintDeliveryPDF(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	template_name = 'invoice/pdf/delivery_note_pdf.html'
	context_object_name = 'lists'
	def get(self,request, *args, **kwargs):
		content={}
		content['invoice']=invoice=Invoice.objects.get(id=self.kwargs['pk'])
		content['invoicelines']=invln=InvoiceLine.objects.filter(invoice_id=self.kwargs['pk']).order_by('order')
		content['total']=invln.aggregate(total_group=Sum(F('qty')*F('price'), output_field=FloatField()))['total_group']

		pdf = render_to_pdf(self.template_name, content,'file')
		if pdf:
			response = HttpResponse(pdf, content_type='application/force-download')
			content = "attachment; filename=%s.pdf  " %invoice.invoice_no
			response['Content-Disposition'] = content
			return response
		else:
			return HttpResponse("Not found")

class PrintInvoicePDF(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	template_name = 'invoice/pdf/invoice_pdf.html'
	context_object_name = 'lists'
	def get(self,request, *args, **kwargs):
		content={}
		content['invoice']=invoice=Invoice.objects.get(id=self.kwargs['pk'])
		content['invoicelines']=invln=InvoiceLine.objects.filter(invoice_id=self.kwargs['pk']).order_by('order')
		content['total']=invln.aggregate(total_group=Sum(F('qty')*F('price'), output_field=FloatField()))['total_group']
			
		pdf = render_to_pdf(self.template_name, content,'file')
		if pdf:
			response = HttpResponse(pdf, content_type='application/force-download')
			content = "attachment; filename=%s.pdf  " %invoice.invoice_no
			response['Content-Disposition'] = content
			return response
		else:
			return HttpResponse("Not found")


class NewQoutation(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	template_name = 'invoice/new_invoice.html'
	form_class = QouteForm
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{'forms':self.form_class})

	def post(self,request, *args,**kwargs ):
		form = self.form_class(request.POST)
		if form.is_valid():
			intno=31
			maxdata=Invoice.objects.aggregate(mano=Max('no'))
			if maxdata['mano']:
				intno=maxdata['mano']
			qty=request.POST.getlist('qty')
			price=request.POST.getlist('price')
			desc=request.POST.getlist('desc')
			ismain=request.POST.getlist('ismain')
			order=request.POST.getlist('order')
			#return HttpResponse(ismain)
			
			invoice=Invoice.objects.create(champion=request.POST.get('champion'),
																		category=request.POST.get('category'),invoice_status='QOUTE',start_date=request.POST.get('start_date'),end_date=request.POST.get('end_date'),deposittype=request.POST.get('deposittype'),stock_info=request.POST.get('stock_info'),tag=request.POST.get('tag'),comment=request.POST.get('comment'),
			currency=request.POST.get('currency'),antetion_person=request.POST.get('antetion_person'),
					   city=request.POST.get('city'),pobox=request.POST.get('pobox'),company=request.POST.get('company'),user_id=self.request.user.id,campaign_id=request.POST.get('campaign'))
			now = datetime.datetime.now()
			invoice.invoice_no=invoice_no(intno+1);
			invoice.no=(intno+1)
			invoice.save()
			list=[]
			for i in range(len(desc)):
				if float(qty[i]) ==0 and float(price[i]) == 0:
					list.append(InvoiceLine(invoice_id=invoice.id,desc=desc[i],qty=0,price=0,order=order[i]))
					
				else:
					list.append(InvoiceLine(invoice_id=invoice.id,desc=desc[i],qty=qty[i],price=price[i],order=order[i]))
					


			if len(list) > 0:
				InvoiceLine.objects.bulk_create(list)

			messages.success(request, 'Success! created qoutation')
			return redirect(reverse('invoice_detail',kwargs={'pk':invoice.id}))
		else:
			return render(request,self.template_name,{'forms':form})


class DuplicateIvoince(LoginRequiredMixin,View):
	login_url = reverse_lazy('login_user')
	redirect_field_name = 'next'
	def get(self, request, *args, **kwargs):
		maxdata=Invoice.objects.aggregate(mano=Max('no'))
		intno=31
		if maxdata['mano']:
			intno=maxdata['mano']
		obj=Invoice.objects.get(id=self.kwargs['pk'])


		obj.pk = None
		obj.invoice_no=invoice_no(intno+1);
		obj.no=(intno+1)
		obj.is_invoice=False
		obj.is_cancelled=False
		obj.is_aninvoice=False
		obj.invoice_status='QOUTE'
		obj.save()
		invoice_id=obj.id

		alllines=InvoiceLine.objects.filter(invoice_id=self.kwargs['pk'])
		list=[]
		for lin in alllines:
			list.append(InvoiceLine(invoice_id=invoice_id,desc=lin.desc,qty=lin.qty,price=lin.price,order=lin.order))
		InvoiceLine.objects.bulk_create(list)
		messages.success(request, 'Success! duplicated the invoice')
		return redirect(reverse('invoice_update',kwargs={'pk':obj.id}))

		 



class ImportQoutation(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login_user')
	redirect_field_name = 'next'
	template_name = 'invoice/new_invoice_import.html'
	model = Invoice
	header='Import Invoice'
	form_class=QouteUploadForm
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{'form':self.form_class,'header':'NEW QOUTE'})

	def post(self,request, *args,**kwargs ):
		form = self.form_class(request.POST,request.FILES)
		if form.is_valid():
			intno=31
			maxdata=Invoice.objects.aggregate(mano=Max('no'))
			if maxdata['mano']:
				intno=maxdata['mano']
			qty=request.POST.getlist('qty')
			price=request.POST.getlist('price')
			desc=request.POST.getlist('desc')
			ismain=request.POST.getlist('ismain')
			order=request.POST.getlist('order')
			file = request.FILES['file']
			fs = FileSystemStorage()
			name=str(datetime.date.today())+'.csv'
			file_name = fs.save(name,file)
			file_path= fs.path(file_name)
			invoice=Invoice.objects.create(champion=request.POST.get('champion'),
																		category=request.POST.get('category'),invoice_status='QOUTE',start_date=request.POST.get('start_date'),end_date=request.POST.get('end_date'),deposittype=request.POST.get('deposittype'),stock_info=request.POST.get('stock_info'),tag=request.POST.get('tag'),
			currency=request.POST.get('currency'),antetion_person=request.POST.get('antetion_person'),
			   city=request.POST.get('city'),pobox=request.POST.get('pobox'),company=request.POST.get('company'),user_id=self.request.user.id,campaign_id=request.POST.get('campaign'))
			invoice.invoice_no=invoice_no(intno+1);
			invoice.no=(intno+1)
			invoice.save()
			list=[]
			#return HttpResponse(request.FILES['file'].read())
			with open(file_path, 'r') as csvfile:
				reader=csv.DictReader(csvfile)
				for row in  reader:
					if float(row['PRICE'].replace(",", "")) ==0 and float(row['QTY']) == 0:
						list.append(InvoiceLine(invoice_id=invoice.id,desc=row['ITEM'],qty=0,price=0,order=row['SN']))

					else:
						list.append(InvoiceLine(invoice_id=invoice.id,desc=row['ITEM'],qty=row['QTY'],price=float(row['PRICE'].replace(",", "")),order=row['SN']))
			if len(list) > 0:
				InvoiceLine.objects.bulk_create(list)

			messages.success(request,'Success created invoice')
			return redirect(reverse('invoice_detail',kwargs={'pk':invoice.id}))
		return render(request,self.template_name,{'form':form})

			#return HttpResponse(ismain)

class INvoiceImportUpdate(LoginRequiredMixin,UpdateView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Invoice
	template_name = 'invoice/new_invoice_import.html'
	form_class = QouteUploadForm
	context_object_name = 'forms'

	def get_success_url(self):
		return reverse('invoices')

	def get_context_data(self, **kwargs):
		context=super().get_context_data()
		#context['invoicelines']= InvoiceLine.objects.filter(invoice_id=self.kwargs['pk']).order_by('order')
		context['invoice']= invo=Invoice.objects.get(id=self.kwargs['pk'])
		context['header']=invo.invoice_no+'/UPDATE'
		return context

	def post(self, request, *args, **kwargs):
		form=self.form_class(request.POST,request.FILES)
		if form.is_valid():
			invoiceno=Invoice.objects.filter(id=self.kwargs['pk']).first()
			invoice=Invoice.objects.filter(id=self.kwargs['pk']).update(champion=request.POST.get('champion'),
																		category=request.POST.get('category'),start_date=request.POST.get('start_date'),end_date=request.POST.get('end_date'),tag=request.POST.get('tag'),currency=request.POST.get('currency'),comment=request.POST.get('comment'),antetion_person=request.POST.get('antetion_person'),deposittype=request.POST.get('deposittype'),stock_info=request.POST.get('stock_info'),	city=request.POST.get('city'),pobox=request.POST.get('pobox'),campaign_id=request.POST.get('campaign'),company=request.POST.get('company'))
			if len(request.FILES) != 0:
				file = request.FILES['file']
				fs = FileSystemStorage()
				name=invoiceno.invoice_no+'-'+str(datetime.date.today())+'.csv'
				file_name = fs.save(name, file)
				file_path=fs.path(file_name)

				InvoiceLine.objects.filter(invoice_id=self.kwargs['pk']).delete()
				list=[]
				data=''
				with open(file_path, 'r') as csvfile:
					reader=csv.DictReader(csvfile)
					for row in  reader:
						data=data+row['ITEM']
						if row['ITEM'] is not None and (float(row['PRICE'].replace(",", "")) ==0 or row['PRICE'] is None)  and (float(row['QTY']) == 0 or row['QTY'] is None):
							list.append(InvoiceLine(invoice_id=self.kwargs['pk'],desc=row['ITEM'],qty=0,price=0,order=row['SN']))

						else:
							list.append(InvoiceLine(invoice_id=self.kwargs['pk'],desc=row['ITEM'],qty=row['QTY'],price=float(row['PRICE'].replace(",", "")),order=row['SN']))

				if len(list) > 0:
					InvoiceLine.objects.bulk_create(list)

				messages.success(request,'Success! updated')
				return redirect(reverse('invoice_detail',kwargs={'pk':self.kwargs['pk']}))
		else:
			return render(request,self.template_name,{'form':form})


class Invoices(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Invoice
	template_name = 'invoice/invoice_list.html'
	context_object_name='invoices'
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data()
		context['invoices']=Invoice.objects.filter(Q(is_aninvoice=True)&Q(is_cancelled=False)&~Q(invoice_status='PAID')).order_by('-id')
		context['header']='INVOICES'
		return context

class Qoutes(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Invoice
	template_name = 'invoice/qoutes.html'
	context_object_name='invoices'
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data()
		context['invoices']=Invoice.objects.filter(is_aninvoice=False,is_cancelled=False).order_by('-id')
		context['header']='QOUTATIONS'
		return context

class Cancelled(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Invoice
	template_name = 'invoice/invoice_list.html'
	context_object_name='invoices'
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data()
		context['header']='CANCELLED'
		context['invoices']=Invoice.objects.filter(is_cancelled=True).order_by('-id')
		return context

class PaidInvoices(LoginRequiredMixin,ListView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Invoice
	template_name = 'invoice/invoice_list.html'
	context_object_name='invoices'
	def get_context_data(self, *, object_list=None, **kwargs):
		context=super().get_context_data()
		context['header']='PAID INVOICES'
		context['invoices']=Invoice.objects.filter(invoice_status='PAID').order_by('-id')
		return context

class YearInvoices(LoginRequiredMixin, ListView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Invoice
	template_name = 'invoice/invoice_list.html'
	context_object_name = 'invoices'
	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data()
		year = self.request.GET.get('year')
		#status = self.request.GET.get('status')
		if not year:
			# if datetime.datetime.strftime(datetime.datetime.now(), '%m') =='01':
			year = datetime.datetime.now().year - 1
			context['invoices'] = Invoice.objects.filter(invoice_status__in=['PAID', 'INVOICE'], invoice_date__year=year).order_by(
			'-id')

		else:
			context['invoices'] = Invoice.objects.filter(invoice_status__in=['PAID', 'INVOICE'], invoice_date__year=year).order_by(
				'-id')

		context['header'] = 'ALL INVOICES  FOR A YEAR '+str(year)
		return context

##INVOICE DISTRIBUTION
@method_decorator(csrf_exempt,name='dispatch')
class InvoiceDistributionAdd(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	template_name='invoice/modal/add_distribution.html'
	form_class = InvoiceDistributionForm
	def get(self, request, *args, **kwargs):
		return render(request,self.template_name,{'form':self.form_class,'invoice_id':self.kwargs['pk']})

	def post(self,request, *args,**kwargs ):
		form = self.form_class(request.POST)
		if form.is_valid():
			form=form.save(commit=False)
			form.created_by_id=self.request.user.id
			form.invoice_id=self.kwargs['pk']
			form.save()
			messages.success(request,'Added the distribution')
			return redirect(reverse('invoice_detail',kwargs={'pk':self.kwargs['pk']}))
		else:
			messages.warning(request, 'Failed to add the distribution')
			return  redirect(reverse('invoice_detail',kwargs={'pk':self.kwargs['pk']}))

class InvoiceDistributionDelete(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	def get(self, request, *args, **kwargs):
		invoice_id=InvoiceDistribution.objects.filter(id=self.kwargs['pk']).first().invoice_id
		InvoiceDistribution.objects.filter(id=self.kwargs['pk']).delete()
		messages.success(request, 'Deleted the distribution')
		return redirect(reverse('invoice_detail', kwargs={'pk': invoice_id}))



class InvoiceDetail(LoginRequiredMixin,DetailView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	template_name = "invoice/invoice_detail.html"
	model = Invoice
	context_object_name = 'invoice'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['expense']=Expensejournal.objects.filter(invoice_id=self.kwargs['pk'])
		context['expected'] = InvoiceDistribution.objects.filter(invoice_id=self.kwargs['pk'])
		context['exsum']=sdat=Expensejournal.objects.filter(invoice_id=self.kwargs['pk']).aggregate(sdat=Sum('dr'))['sdat']
		context['expectedsum'] =InvoiceDistribution.objects.filter(invoice_id=self.kwargs['pk']).aggregate(scr=Sum('expected_amount'))['scr']
		context['jobcard']=Jobcard.objects.filter(invoice_id=self.kwargs['pk']).first()
		context['invoicelines'] = InvoiceLine.objects.filter(invoice_id=self.kwargs['pk']).order_by('order')
		context['invsum'] = InvoiceLine.objects.filter(invoice_id=self.kwargs['pk']).aggregate(dt=Sum(F('price') * F('qty')))['dt'] - sdat
		return context

class INvoiceUpdate(LoginRequiredMixin,UpdateView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Invoice
	template_name = 'invoice/update.html'
	form_class = QouteForm
	context_object_name = 'forms'

	def get_success_url(self):
		return reverse('invoices')
	def get_context_data(self, **kwargs):
		context=super().get_context_data()
		context['invoicelines']= InvoiceLine.objects.filter(invoice_id=self.kwargs['pk']).order_by('order')
		context['invoice']= Invoice.objects.get(id=self.kwargs['pk'])
		return context

	def post(self, request, *args, **kwargs):
		form=self.form_class(request.POST)
		if form.is_valid():
			if request.POST.get('show_tax'):
				show_tax=True
			else:
				show_tax=False

			invoice=Invoice.objects.filter(id=self.kwargs['pk']).update(start_date=request.POST.get('start_date'),deposittype=request.POST.get('deposittype'),end_date=request.POST.get('end_date'),
			stock_info=request.POST.get('stock_info'),tag=request.POST.get('tag'),show_tax=show_tax,comment=request.POST.get('comment'),	currency=request.POST.get('currency'),antetion_person=request.POST.get('antetion_person'),
																		city=request.POST.get('city'),
																		pobox=request.POST.get('pobox'),
																		champion=request.POST.get('champion'),
																		category=request.POST.get('category'),
																		campaign_id=request.POST.get('campaign'),
																		company=request.POST.get('company'),user_id=self.request.user.id)
			InvoiceLine.objects.filter(invoice_id=self.kwargs['pk']).delete()

			qty=request.POST.getlist('qty')
			price=request.POST.getlist('price')
			desc=request.POST.getlist('desc')
			order=request.POST.getlist('order')
			list=[]
			for i in range(len(desc)):
				list.append(InvoiceLine(invoice_id=self.kwargs['pk'],desc=desc[i],qty=qty[i],price=price[i],order=order[i]))

			if len(list) > 0:
				InvoiceLine.objects.bulk_create(list)
			messages.success(request,'Success! updated')
			return redirect(reverse('invoice_detail',kwargs={'pk':self.kwargs['pk']}))
		else:
			return render(request,self.template_name,{'form':form})
			
class Move2DELETE(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model=Invoice
	context_object_name = 'invoice'

	def get(self,*kwargs,**args):
		InvoiceLine.objects.filter(invoice_id=self.kwargs['pk']).delete()
		invo=Invoice.objects.filter(id=self.kwargs['pk']).delete()
		messages.success(self.request,'Qoute removed')
		return redirect(reverse('qoutes'))


class Move2Invoice(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model=Invoice
	context_object_name = 'invoice'

	def get(self,*kwargs,**args):
		invo=Invoice.objects.filter(id=self.kwargs['pk']).first()
		Invoice.objects.filter(id=self.kwargs['pk']).update(invoice_status='INVOICE',invoice_start_date=datetime.datetime.today().date(),is_aninvoice=True)
		messages.success(self.request,'Invoice created')
		return redirect(reverse('invoice_detail',kwargs={'pk':self.kwargs['pk']}))

class Move2Cancel(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model=Invoice
	context_object_name = 'invoice'

	def get(self,*kwargs,**args):
		invo=Invoice.objects.filter(id=self.kwargs['pk']).first()
		Invoice.objects.filter(id=self.kwargs['pk']).update(invoice_status='CANCELLED',invoice_start_date=datetime.datetime.today().date(),is_cancelled=True)
		messages.success(self.request,str(invo.invoice_no)+' Cancelled ')
		return redirect(reverse('invoice_detail',kwargs={'pk':self.kwargs['pk']}))


class Move2Paid(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model=Invoice
	context_object_name = 'invoice'

	def get(self,*kwargs,**args):
		invo=Invoice.objects.filter(id=self.kwargs['pk']).first()
		Invoice.objects.filter(id=self.kwargs['pk']).update(invoice_status='PAID')
		messages.success(self.request,str(invo.invoice_no)+' Marked Paid ')
		return redirect(reverse('invoice_detail',kwargs={'pk':self.kwargs['pk']}))

class Move2Unpaid(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model=Invoice
	context_object_name = 'invoice'

	def get(self,*kwargs,**args):
		invo=Invoice.objects.filter(id=self.kwargs['pk']).first()
		Invoice.objects.filter(id=self.kwargs['pk']).update(invoice_status='UNPAID')
		messages.success(self.request,str(invo.invoice_no)+' Marked Unpaid ')
		return redirect(reverse('invoice_detail',kwargs={'pk':self.kwargs['pk']}))

class Move2Qoute(LoginRequiredMixin,View):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model=Invoice
	context_object_name = 'invoice'

	def get(self,*kwargs,**args):
		invo=Invoice.objects.filter(id=self.kwargs['pk']).first()
		Invoice.objects.filter(id=self.kwargs['pk']).update(invoice_status='QOUTE',is_aninvoice=False)
		messages.success(self.request,str(invo.invoice_no)+' Marked QOUTE ')
		return redirect(reverse('invoice_detail',kwargs={'pk':self.kwargs['pk']}))


####################################################
####  JOBCARD ######################################
###################################################

class UpdateJobcard(LoginRequiredMixin,UpdateView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Jobcard
	form_class = JobcardUpdateForm
	context_object_name = 'form'
	template_name = 'invoice/jobcard/update.html'


	def get_context_data(self, **kwargs):
		context=super().get_context_data()
		context['header']='UPDATE JOBCARD'
		context['jobcardline']=JobcardLine.objects.filter(jobcard_id=self.kwargs['pk'])
		return context

	def post(self,request, *args,**kwargs ):
		form = self.form_class(request.POST)
		if form.is_valid():
			jobcard=Jobcard.objects.filter(id=self.kwargs['pk'])
			#return HttpResponse(jobcard.first().invoice_id)
			job_id=jobcard.first().id
			invoob=Invoice.objects.get(id=jobcard.first().invoice_id)

			#device=request.POST.getlist('device')
			desc=request.POST.getlist('desc')
			order=request.POST.getlist('order')
			status=request.POST.getlist('status1')

			jobcard.update(job_date=request.POST.get('job_date'),project=request.POST.get('project'),device=request.POST.get('device'),client=request.POST.get('client'),
			address=request.POST.get('address'),city=request.POST.get('city'),
					   technician=request.POST.get('technician'),user_id=self.request.user.id)
			JobcardLine.objects.filter(jobcard_id=job_id).delete()


			list=[]
			for i in range(len(desc)):
				if len(desc) > 0:
					list.append(JobcardLine(jobcard_id=job_id,desc=desc[i],order=order[i],status=status[i]))
			if len(list) > 0:
				JobcardLine.objects.bulk_create(list)

			messages.success(request, 'Success! created jobcard')
			return redirect(reverse('jobcard_detail',kwargs={'job':job_id,'pk':invoob.id}))


		else:
			jobcardline=JobcardLine.objects.filter(jobcard_id=self.kwargs['pk'])
			return render(request,self.template_name,{'form':form,'jobcardline':jobcardline})


#############################UPDATE JOBCARD
class NewJobcard(LoginRequiredMixin,CreateView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Invoice
	template_name = 'invoice/jobcard/new.html'
	form_class = JobcardForm
	context_object_name = 'forms'

	def get_form_kwargs(self,**kwargs):
		invoice=Invoice.objects.get(id=self.kwargs['pk'])
		kwargs=super(NewJobcard,self).get_form_kwargs()
		kwargs.update({'invoice':invoice})
		return kwargs
	def get_context_data(self, **kwargs):
		context=super().get_context_data()
		invoice=Invoice.objects.get(id=self.kwargs['pk'])
		context['header']='JOBCARD FOR INVOICE NO. '+invoice.invoice_no
		return context

	def post(self,request, *args,**kwargs ):
		invoice=Invoice.objects.get(id=self.kwargs['pk'])
		form = self.form_class(request.POST,invoice=invoice)
		if form.is_valid():
			invoob=Invoice.objects.get(id=self.kwargs['pk'])
			if not Jobcard.objects.filter(invoice_id=self.kwargs['pk']).exists():

				intno=31
				maxdata=Jobcard.objects.aggregate(mano=Max('jobno'))
				if maxdata['mano']:
					intno=maxdata['mano']

				#device=request.POST.getlist('device')
				desc=request.POST.getlist('desc')
				order=request.POST.getlist('order')
				status=request.POST.getlist('status1')

				#return HttpResponse(ismain)
				invoob=Invoice.objects.get(id=self.kwargs['pk'])
				jobcard=Jobcard.objects.create(status='done',job_date=request.POST.get('job_date'),project=request.POST.get('project'),device=request.POST.get('device'),client=request.POST.get('client'),
				address=request.POST.get('address'),city=request.POST.get('city'),
						   technician=request.POST.get('technician'),user_id=self.request.user.id,invoice_id=self.kwargs['pk'])
				now = datetime.datetime.now()
				jobcard.jobcard_no=invoice_no(invoob.no);
				jobcard.jobno=(invoob.no)

				jobcard.save()
				job_id=jobcard.id
				list=[]
				for i in range(len(desc)):
					if len(desc) > 0:
						list.append(JobcardLine(jobcard_id=job_id,desc=desc[i],order=order[i],status=status[i]))
				if len(list) > 0:
					JobcardLine.objects.bulk_create(list)

				messages.success(request, 'Success! created jobcard')
				return redirect(reverse('jobcard_detail',kwargs={'job':job_id,'pk':invoob.id}))
			else:
				job_id=Jobcard.objects.filter(invoice_id=self.kwargs['pk']).first().id
				return redirect(reverse('jobcard_detail',kwargs={'job':job_id,'pk':invoob.id}))

		else:
			invoice=Invoice.objects.get(id=self.kwargs['pk'])
			header='JOBCARD FOR INVOICE NO. '+invoice.invoice_no
			return render(request,self.template_name,{'form':form,'header':header})


class JobcardDetail(LoginRequiredMixin,DetailView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	template_name = "invoice/jobcard/jobcard_detail.html"
	model = Invoice
	context_object_name = 'invoice'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['jobcard']=jobcard=Jobcard.objects.get(id=self.kwargs['job'])
		context['invoicelines'] = JobcardLine.objects.filter(jobcard_id=jobcard.id).order_by('order')
		return context

class PrintJobcardPdf(LoginRequiredMixin,DetailView):
	login_url = reverse_lazy('login-user')
	redirect_field_name = 'next'
	model = Jobcard
	def get(self,*args, **kwargs):
		content={}
		content['jobcard']=jobcard=Jobcard.objects.get(id=self.kwargs['pk'])
		content['jobcardline']=JobcardLine.objects.filter(jobcard_id=self.kwargs['pk'])


		pdf = render_to_pdf('invoice/jobcard/jobcard_pdf.html', content,'file')
		if pdf:
			response = HttpResponse(pdf, content_type='application/force-download')
			content = "attachment; filename=JOBCARD.pdf  "
			response['Content-Disposition'] = content
			return response
		else:
			return HttpResponse("Not found")
