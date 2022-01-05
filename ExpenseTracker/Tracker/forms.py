from django import forms
from django.forms import ModelForm, widgets
from django import forms
from django.forms import ModelForm
from .models import * 
from django.contrib.auth.forms import UserCreationForm

class FormProfile(forms.ModelForm):


    class Meta:
        model = Profile 
        fields = "__all__"
        exclude = ['expenses','user','currency_type','curr_value']

        widgets = {
            'income' : forms.NumberInput(attrs = {'class':'form-control'}),
            'income_category' : forms.TextInput(attrs={'class': 'form-control'}),
            'balance': forms.NumberInput(attrs= {'class': 'form-control'}),
            
        }

class MyUserCreationForm(UserCreationForm):
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control required','placeholder':'Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control required','placeholder':'Confirm-Password'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'login-form form-control required','placeholder':'Email'}))
    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].label = ""
        self.fields['username'].label=''
        self.fields['password1'].label=''
        self.fields['password2'].label=''
    class Meta:
        model = User
        fields=['username','email','password1','password2']
    
        widgets = {
            'username' : forms.TextInput(attrs={'class': 'login-form form-control required','placeholder':'username'}),
            'email' : forms.EmailInput(attrs={'class': 'login-form form-control required','placeholder':'Email'}),
            'password1' : forms.PasswordInput(attrs={'class': 'login-form form-control required','placeholder':'Password'}),
            'password2' : forms.PasswordInput(attrs={'class': 'login-form form-control required','placeholder':'Confirm-Password'}),
        }
