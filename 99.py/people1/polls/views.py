from django.shortcuts import render
from django.http import HttpResponse
import json

json_file = "polls/people.json"
with open(json_file, 'r') as file:
    people = json.load(file)
    people_age = sorted(people['people'], key=lambda i: i['age'])
    people['people'] = people_age


def index(request):
    people_age = [(item["name"], item["age"],item["country"]) for item in people["people"]]
    people_age.sort(key=lambda item: item[1])
    context = {'result': people_age}
    return render(request, 'index.html', context)

def people_Id(request):
    json_file = "polls/people.json"
    with open(json_file, 'r') as file:
        people = json.load(file)
        people_id = people['people']


        context = {
            'id': id,
            'people_id': people_id,
            'people_1':people_id[0]
        }
        return render(request, 'people_id.html', context)