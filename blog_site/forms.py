from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django import forms

class CustomUserForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your FirstName'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your LastName'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Username'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email ID'}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Mobile number'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter you Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter you Password again'}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','id':'photo'}),required=False)

    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','contact','password1','password2','profile_pic']

class CustomUserChangeForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your FirstName'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your LastName'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Username'}),required=False,disabled=True)
    email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email ID'}))
    contact = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Enter your Mobile number'}),max_length=10)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter you Password'}),required=False)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter you Password again'}),required=False)
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class':'form-control','id':'photo'}),required=False)
    class Meta:
        model = CustomUser
        fields = ['first_name','last_name','username','email','contact','password1','password2','profile_pic']