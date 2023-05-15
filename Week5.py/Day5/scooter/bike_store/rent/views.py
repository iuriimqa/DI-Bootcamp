from django.shortcuts import render
from .models import *
from .forms import *
from datetime import date
from django.db.models import F
from faker import Faker
from django.views import generic
from django.urls import reverse_lazy


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

class VehicleAdd(generic.CreateView):
    template_name = 'vehicle_add.html'
    context_object_name = 'addvehicle'
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('vehicles')


class Rentals(generic.ListView):
    template_name = 'rental.html'
    context_object_name = 'rentals'
    model = Rental

class Rental_id(generic.DetailView):
    template_name = 'rental_id.html'
    context_object_name = 'rental_id'
    model = Rental

class RentalAdd(generic.CreateView):
    template_name = 'rental_add.html'
    context_object_name = 'addrental'
    model = Rental
    fields = '__all__'
    success_url = reverse_lazy('rentals')

class Customers(generic.ListView):
    template_name = 'customers.html'
    context_object_name = 'customers'
    model = Customer


class Customer_id(generic.DetailView):
    template_name = 'customer_id.html'
    context_object_name = 'customer_id'
    model = Customer

class CustomerAdd(generic.CreateView):
    template_name = 'customer_add.html'
    context_object_name = 'addcustomer'
    model = Customer
    fields = '__all__'
    success_url = reverse_lazy('rentals')



