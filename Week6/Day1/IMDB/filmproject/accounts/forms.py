from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import views
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='First_name',min_length=5, max_length=150)
    last_name = forms.CharField(label='Last_name',min_length=5, max_length=150)

    class Meta:
        model = User
        fields = ['username','first_name','last_name']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))