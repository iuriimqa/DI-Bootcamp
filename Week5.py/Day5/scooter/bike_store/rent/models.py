from django.db import models
from datetime import datetime
from faker import Faker

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} | {self.email} | {self.phone_number} | {self.country}"

    # def __str__(self):
    # return f"{self.first_name}"

class Vehicle(models.Model):
    vehicle_type = models.ForeignKey('Vehicle_type', on_delete=models.CASCADE)
    date_created = models.DateTimeField
    real_cost = models.IntegerField()
    size = models.ForeignKey('Vehicle_size', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.vehicle_type} | {self.real_cost} | {self.size}"

class Vehicle_type(models.Model):
    name = models.CharField(50)

    def __str__(self):
        return f"{self.name}"

class Vehicle_size(models.Model):
    name = models.CharField(50)

    def __str__(self):
        return f"{self.name}"

class Rental(models.Model):
    rental_date = models.DateTimeField(null=True)
    return_date = models.DateTimeField(null=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.customer}|{self.vehicle}"

class Rental_rate(models.Model):
    daily_rate = models.FloatField()
    vehicle_type = models.ForeignKey(Vehicle_type, on_delete=models.CASCADE)
    vehicle_size = models.ForeignKey(Vehicle_size,on_delete=models.CASCADE)







