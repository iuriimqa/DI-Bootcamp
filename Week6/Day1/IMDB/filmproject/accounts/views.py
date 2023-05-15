from django.shortcuts import render
from .models import *
from django.views import generic
from .forms import SignUpForm,LoginForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.base import TemplateView



class SignUp(generic.CreateView):
    form_class = SignUpForm
    model = User
    success_url = reverse_lazy('login')
    template_name = "signup.html"
    context_object_name = 'signup'

class Login(generic.FormView):
    form_class = LoginForm
    success_url = reverse_lazy('homepage')
    template_name = "login.html"
    context_object_name = 'login'

class Profile(generic.DetailView):
    template_name = 'profile.html'
    context_object_name = 'profile'
    model = User

class LogoutView(TemplateView):
    template_name = 'logout.html'

