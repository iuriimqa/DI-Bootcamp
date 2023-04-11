# class Object:
#     numbers_object_created = 0
#     objects = {}
#
#     def __init__(self):
#         Object.objects[Object.numbers_object_created] = self
#         Object.numbers_object_created += 1
#
#
# Object()
# Object()
# Object()
# Object()
# Object()
#
# print(Object.numbers_object_created)
# print(Object.objects)

import requests
import time
import json

database = []

while len(database) < 5:
    response = requests.get("https://api.chucknorris.io/jokes/random?category=money")
    data = response.json()
    database.append(data)
    print(data)
