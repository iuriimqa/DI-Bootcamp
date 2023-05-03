from django.shortcuts import render
from .models import *
from .forms import *
from datetime import date
from django.db.models import F
from faker import Faker
from django.views import generic


class Rentals(generic.ListView):
    template_name = 'rental.html'
    context_object_name = 'rentals'
    model = Rental

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['page_title'] = "Rentals"
    #     context['rental']


# def rental(request):
#     rentals = Rental.objects.all().order_by(
#         F('return_date').asc(nulls_first=True))
#     context = {'rentals': rentals}
#     return render(request,'rental.html',context)

class Vehicles(generic.ListView):
    template_name = 'vehicle.html'
    context_object_name = 'vehicles'
    model = Vehicle

class Vehicle_id(generic.DetailView):
    template_name = 'vehicle_id.html'
    context_object_name = 'vehicle_id'
    model = Vehicle

class Rentals(generic.ListView):
    template_name = 'rental.html'
    context_object_name = 'rentals'
    model = Rental

class Rental_id(generic.DetailView):
    template_name = 'rental_id.html'
    context_object_name = 'rental_id'
    model = Rental