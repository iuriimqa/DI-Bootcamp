"""
URL configuration for bike_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rent.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rentals/',Rentals.as_view(),name = 'rentals'),
    path('vehicles/',Vehicles.as_view(),name = 'vehicles'),
    path('vehicles/<int:pk>',Vehicle_id.as_view()),
    path('rentals/<int:pk>',Rental_id.as_view()),
    path('rentals/add',RentalAdd.as_view()),
    path('vehicles/add',VehicleAdd.as_view()),
    path('customers/',Customers.as_view(), name = 'customers'),
    path('customers/<int:pk>',Customer_id.as_view()),
    path('customers/add',CustomerAdd.as_view())
]
