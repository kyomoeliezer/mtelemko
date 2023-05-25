
from django.views.generic import CreateView,ListView,UpdateView,View,FormView,DeleteView
from django.shortcuts import redirect,reverse,resolve_url,render,HttpResponse
from django.contrib.auth.models import Group
from django.db.models import Q,Count,F,Max,ProtectedError
#from django.db.models import ProtectedError,Count,F,Q,Case,When,Value,FloatField,Sum
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import login,logout # ,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from user.custombackend import authenticate
from user.form import CustomAuthenticationForm
from user.form import *
from user.models import *
from django.contrib.auth.hashers import make_password
#from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from user.decorators import *


from user.models import Role,User

################################
###########CREATE PERMISSION#############
####ROLES
class CreatePermission(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = CustPermission
    fields = ['perm_name','perm_desc']
    template_name = 'perm/create.html'
    context_object_name = 'form'
    header='New Permission'
    success_url = reverse_lazy('permissions')

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

class UpdatePermission(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')

    model = CustPermission
    fields = ['perm_name','perm_desc']
    template_name ='perm/create.html'
    context_object_name = 'form'
    header='Update Permission'
    success_url = reverse_lazy('permissions')
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

class PermissionDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = CustPermission
    success_message = "Success!  deleted permissions."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request,'Huwezi kufuta permission hii, kuna data zinategemea data  hii')
            return redirect('permissions')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('permissions')

class PermissionsList(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = CustPermission
    context_object_name = 'lists'
    template_name = 'perm/perm_list.html'
    header='Permissions'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

class PermissionRequired(LoginRequiredMixin,View):
    def get(self,request):
        return render(request,'perm/permission_required.html')
###END PERMISSION###########################


####ROLES
class CreateRole(LoginRequiredMixin,CreateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')

    model = Role
    fields = ['name','code','perm']
    template_name = 'user/new_role.html'
    context_object_name = 'form'
    header='New Role'
    success_url = reverse_lazy('roles')

    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

class UpdateRole(LoginRequiredMixin,UpdateView,SuccessMessageMixin):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')

    model = Role
    fields = ['name','perm']
    template_name = 'user/update_role.html'
    context_object_name = 'form'
    header='Update Role'
    success_message = 'Succesfully Updated'
    success_url = reverse_lazy('roles')
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

class RoleDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Role
    success_message = "Success!  umefuta."
    def post(self, request, *args, **kwargs):
        try:
            return self.delete(request, *args, **kwargs)
        except ProtectedError:
            messages.warning(request,'Huwezi kufuta aina user huyu, kuna data zinategemea data za user hii')
            return redirect('roles')

    def get(self, request, *args, **kwargs):
            return self.post(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('roles')

class Roles(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')

    model = Role
    context_object_name = 'lists'
    template_name = 'user/role_role.html'
    header='Roles'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context

class RoleList(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = Group
    context_object_name = 'lists'
    template_name = 'user/role_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context=super(RoleList,self).get_context_data()
        context['Title']='Roles'

        return context

class UserDelete(LoginRequiredMixin,DeleteView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = User
    success_url = reverse_lazy('users')
    success_message = "Success! deleted"
    def get(self, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return self.post(*args, **kwargs)

###LOGIN NOW
class LoginView1(View):
    form_class = CustomAuthenticationForm
    template_name = 'user/login.html'
    # display blank form
    def get(self, request):
        logout(request)
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process form data
    def post(self, request):
        form = self.form_class(data=request.POST)
        username=request.POST.get('username')
        password=request.POST.get('password')

        if form.is_valid():
            #if credentials are correct, this returns a user object
            user = authenticate(self,username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    """
                    if   user.role is not None:
                        if 'SALE' in user.role.code:
                            return redirect('leadlist')

                        else:
                            return redirect('leadlist')
                    """
                    return redirect('apps')

            else:
                return render(request, self.template_name, {'form': form,'error':'Your email and password are incorect'})

        return render(request, self.template_name, {'form': form})

class LoginViewasSomeUser(View):

    def get(self, request, *args, **kwargs):
        user=User.objects.get(id=self.kwargs['pk'])
        

        if user:
            #if credentials are correct, this returns a user object
            #user = authenticate(self,username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(self.request, user)
                    """
                    if   user.role is not None:
                        if 'SALE' in user.role.code:
                            return redirect('leadlist')

                        else:
                            return redirect('leadlist')
                    """
                    return redirect('apps')

            else:
                return render(request, self.template_name, {'form': form,'error':'Your email and password are incorect'})

        return redirect(reverse_leazy('users'))




class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login_user')



class Users(LoginRequiredMixin,ListView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model = User
    context_object_name = 'lists'
    template_name = 'user/user_list.html'
    header='Users'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        return context



###ROLES END

class NewUser(CreateView):

    model =User
    form_class = UserForm
    template_name = 'user/new_user.html'
    context_object_name = 'form'
    header='New User'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header
        context['roles']=Role.objects.all()
        return context
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():
            if request.POST.get('cpassword') in request.POST.get('password'):
                user=User.objects.create_user(username=request.POST.get('email'),email=request.POST.get('email'),mobile=request.POST.get('mobile'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),role_id=request.POST.get('role'),password=make_password(request.POST.get('password')),is_staff=True,is_active=True)
                #user=User.objects.create_user(username=request.POST.get('email'),email=request.POST.get('email'),mobile=request.POST.get('mobile'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),password=make_password(request.POST.get('password')),is_staff=True,is_active=True)
                messages.success(request,'Success! created '+request.POST.get('email'))
                return redirect('users')
            else:
                return render(request,self.template_name,{'form':form,'header':self.header,'error':'Password Do not Match'})

        else:
            return render(request,self.template_name,{'form':form,'header':self.header})


class UpdateUser(LoginRequiredMixin,UpdateView):
    redirect_field_name = 'next'
    login_url = reverse_lazy('login_user')
    model =User
    form_class = UserUpdateForm
    template_name = 'user/update_user.html'
    context_object_name = 'form'
    header='Update User'
    def get_context_data(self, **kwargs):
        context=super().get_context_data()
        context['header']=self.header

        return context
    def post(self, request, *args, **kwargs):
        form=self.form_class(request.POST)
        if form.is_valid():


            user=User.objects.filter(id= self.kwargs['pk']).update(username=request.POST.get('email'),email=request.POST.get('email'),mobile=request.POST.get('mobile'),first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),role_id=request.POST.get('role'))
            messages.success(request,'Success! update '+request.POST.get('email'))
            return redirect('users')

                #return render(request,self.template_name,{'form':form,'header':self.header,'error':'Password Do not Match'})

        else:
            return render(request,self.template_name,{'form':form,'header':self.header})

##########################################################################################################
####################MWAKA WA FEDHA##############################




