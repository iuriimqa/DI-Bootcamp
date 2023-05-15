from django.shortcuts import render
from .models import *
from django.views import generic
from .forms import AddFilmForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

class AddFilm(generic.CreateView):
    template_name = 'film/addfilm.html'
    model = Film
    fields = '__all__'
    context_object_name = 'addfilm'
    success_url = reverse_lazy("homepage")



class Films(generic.ListView):
    template_name = 'homepage.html'
    model = Film
    context_object_name = 'films'

class AddDirector(generic.CreateView):
    template_name = 'director/adddirector.html'
    model = Director
    context_object_name = 'adddirector'
    fields = '__all__'
    success_url = reverse_lazy("adddirector")









# Create your views here.
