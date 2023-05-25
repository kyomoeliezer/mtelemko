from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from .models import User,Role

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=('username','email')

class CustomUserUpdateForm(UserChangeForm):
    class Meta:
        model=User
        fields=('username','password','last_name','last_name','first_name')

class CustomAuthenticationForm(forms.Form):
    username=forms.CharField(label='Email/Mobile',required=True)
    password=forms.CharField(widget=forms.PasswordInput(),label='Password')

class UserForm(forms.ModelForm):
    email=forms.EmailField(required=True)
    mobile=forms.CharField(required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    role=forms.ModelChoiceField(queryset=None,label='Role kwenye system')
    password=forms.CharField(widget=forms.PasswordInput())
    cpassword=forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')
    class Meta:
        model=User
        fields=['first_name','last_name','role','email']

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['role'].queryset = Role.objects.all()
        self.fields['role'].widget.attrs['class'] = 'select2'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'

    def clean_email(self):
        email=self.cleaned_data.get("email")
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError(
                "Email already exists"
            )
        else:
            return email

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("cpassword")
        if password != confirm_password:
            raise forms.ValidationError(
                "The password and confirm password does not match"
            )

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField(required=True)
    mobile=forms.CharField(required=True)
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    role=forms.ModelChoiceField(queryset=None,label='Role kwenye system')
    #password=forms.CharField(widget=forms.PasswordInput())
    #cpassword=forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')
    class Meta:
        model=User
        fields=['first_name','last_name','email','role','mobile']

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['role'].queryset = Role.objects.all()
        self.fields['role'].widget.attrs['class'] = 'select2'
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-title'





