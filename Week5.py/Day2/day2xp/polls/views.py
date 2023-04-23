from django.shortcuts import render


from info.models import Family, Animal
import os
import json

# Create your views here.

def families(request, id):
    family = 4
    #Change the animal family to print its information to html file
    f = open('animals.json')
    data = json.load(f)
    data_animals = Animal.objects.all()
    data_families = Family.objects.all()
    list_temp = []
    for i in range(len(data['animals'])):
        if data['animals'][i]['family'] == id:
            list_temp.append(data['animals'][i]['name'])
    for i in range(len(data['families'])):
        if data['families'][i]['id'] == id:
            family_temp = data['families'][i]['name']
    for i in range(len(data_animals)):
        if data_animals[i].family_id == id:
            list_temp.append(data_animals[i].name)
    for i in range(len(data_families)):
        if data_families[i].id == id:
            family_temp = data_families[i].name

    context = {
        'animal_list': list_temp,
        'family_name': family_temp
    }
    f.close()
    return render(request, 'families.html/', context)

def animals(request, id):
    f = open('animals.json')
    data = json.load(f)
    for animal in data['animals']:
        if animal['id'] == id:
    data = Animal.objects.all()
    for animal in data:
        if animal.id == id:
            result = animal
    family_id = result['family']
    images = os.listdir('info/static/images/')
    context = {
        'image': images[id - 1],
        'animal_name': result['name'],
        'animal_legs': result['legs'],
        'animal_weight': result['weight'],
        'animal_height': result['height'],
        'animal_speed': result['speed'],
        'animal_family': data['families'][family_id - 1]['name'],
        'animal_name': result.name,
        'animal_legs': result.legs,
        'animal_weight': result.weight,
        'animal_height': result.height,
        'animal_speed': result.speed,
        'animal_family': Family.objects.all()[result.family_id - 1],
        # data['families'][family_id - 1]['name'],
    }
    f.close()
    return render(request, 'animals.html/', context)

def animallist(request):
    data = Animal.objects.all()
    images = os.listdir('info/static/images/')
    context = {
        'images': images,
        'animals': data
    }
    return render(request, 'animallist.html/', context)


# id = 1
# images = os.listdir('static/images/')
# print(images[id])
