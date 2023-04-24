from django.shortcuts import render
from .models import Person


def search(model, field, value):

    result = None
    try:
        models_instance = model.object.get(fieldvalue)
        result = models_instance

    except model.DoesNotExist:
            pass
    return result

def search_person(request, search_value: str):

    context = {}

    person_info = search(Person, search_value)

    if person_info is not None:
        context = {'person':person_info}

    return render(request, 'person_info.html', context)

# def profile_view(request, search_value:str)
