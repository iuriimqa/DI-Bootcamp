from django.shortcuts import render
from django.db import models
from phonenumber_field import modelfields
# Create your views here.

class Person(models.Model):

    def search(model, value):

        result = None
        try:
            model_instance = model.objects.get(name = value)
            result = model_instance
        except model.DoesNotExist:
            pass
        try:
            model_instance = model.objects.get(phone_number = value)
            result = model_instance
        except model.DoesNotExist:
            pass

        return result


    def search_person(request, search_value: str):

        context = {}

        person_info = search(Person, search_value)

        if person_info is not None:
            context = {'person': person_info}

        return render(request, 'person_info.html', context)


class Profile(models.Model):
    country_origin = models.CharField(max_length=50)
    languages = models.ManyToManyField('Language')

class Language(models.Model):
    name = models.CharField(max_length=50)





