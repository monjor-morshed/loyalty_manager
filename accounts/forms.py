from django import forms
from .models import Customer

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomerForm(UserCreationForm):
    username = forms.CharField(max_length=50, widget=forms.TextInput, required=True, help_text='Required.')
    email = forms.EmailField(label='Email' ,max_length=254, widget=forms.EmailInput, help_text='Required')
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, help_text='Required')
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput, help_text='Required')
    class Meta:
        model = Customer
        fields = ('username', 'email', 'password1', 'password2')

class CustomerAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', max_length=50, widget=forms.TextInput, help_text='Required')
    password = forms.CharField(label='Password', widget=forms.PasswordInput, help_text='Required')


