from django.shortcuts import render,redirect,resolve_url,reverse
from django.contrib import messages
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from product.models import Product
from product.forms import ProductForm

# Create your views here.

class ProductCreate(CreateView):
    form_class = ProductForm
    template_name = 'product/product_form.html'
    def get(self, request, *args, **kwargs):
        return render(request,self.template_name,{'form':self.form_class})
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'Success! added new product')
            return  redirect('newproduct')
        else:
            return render(request,self.template_name,{'form':form})

class ProductList(ListView):
    model=Product
    context_object_name = 'product'
    template_name = 'product/product_list.html'

class ProductUpdate(UpdateView):
    model = Product
    template_name = 'product/product_update.html'
    fields=['name','description','type','tag']
    def get_success_url(self):
        return reverse('productlist')
