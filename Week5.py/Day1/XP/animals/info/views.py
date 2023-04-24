from django.shortcuts import render
from django.http import HttpResponse
import json


def familyid(request, id):
        with open('info/animals.json', 'r') as f:
                data = json.load(f)

        data_dic = {'data': data}
        context = {}
        context['animals_name'] = [f['name'] for f in data_dic['data']['animals'] if int(f['family']) == int(id)]
        context['family_id'] = id
        print(context, type(id))

        return render(request, 'family.html', context)


def animalid(request, id):
        with open('info/animals.json', 'r') as f:
                data = json.load(f)

        data_dic = {'data': data}
        context = {}
        context['animals'] = data_dic['data']['animals'][id - 1]
        context['animal_id'] = int(id)

        return render(request, 'animal.html', context)
