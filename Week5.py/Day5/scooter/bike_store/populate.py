import os
import django
from faker import Faker
import random
from datetime import timedelta
from zoneinfo import ZoneInfo

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')
django.setup()

from rent.models import *

fake = Faker()

# if __name__ == '__main__':
#     print("Populating database")
#
#     for i in range(1, 20):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         email = fake.email()
#         phone_number = fake.phone_number()
#         address = fake.address()
#         city = fake.city()
#         country = fake.country()
#         new_customer = Customer(first_name=first_name,last_name=last_name,email=email, phone_number=phone_number,address=address,city=city,country=country)
#         new_customer.save()

if __name__ == '__main__':
    print("Populating database")

    # for i in range(1, 100):
    #     rental_date = fake.first_name()
    #     last_name = fake.last_name()
    #     email = fake.email()
    #     phone_number = fake.phone_number()
    #     address = fake.address()
    #     city = fake.city()
    #     country = fake.country()
    #     new_customer = Customer(first_name=first_name,last_name=last_name,email=email, phone_number=phone_number,address=address,city=city,country=country)
    #     new_customer.save()

    # for i in range(300):
    #     real_cost = random.randint(200,2000)
    #     size_id= random.randint(1,4)
    #     vehicle_type_id= random.randint(1,4)
    #     new_vehicle = Vehicle(id,'real_cost','size_id','vehicle_type_id')
    #     new_vehicle.save()

# for i in range(300):
#     size = random.choice(Vehicle_size.objects.all())
#     type = random.choice(Vehicle_type.objects.all())
#     cost = random.randint(800,2400)
#
#     new_vehicle = Vehicle(vehicle_type = type, real_cost = cost, size = size)
#     new_vehicle.save()

    local_tz = ZoneInfo('Israel')
    for i in range(5):

        r_date = fake.date_time()
        while True:
            ret_date = fake.date_time()
            if ret_date > r_date:
                break

        r_date = r_date.replace(tzinfo=local_tz)
        ret_date = ret_date.replace(tzinfo=local_tz)

        cust = random.choice(Customer.objects.all())
        ve = random.choice(Vehicle.objects.all())

        new_rental = Rental(rental_date=r_date, return_date=ret_date, customer=cust, vehicle=ve)
        new_rental.save()
