# # Exercise1
# # Random Sentence Generator
# import urllib.request
# import urllib
# import random

#
# def get_words_from_file():
#     files = []
#     with open('namelist1.txt', 'r') as f:
#         for line in f:
#             files.append(line[0:-1].lower())
#     return files
#
#
# def get_random_sentence(lenth: int, files: list):
#     res_string = files[random.randint(0, len(files) - 1)].capitalize()
#     for _ in range(lenth - 1):
#         res_string += (" " + files[random.randint(0, len(files) - 1)])
#     return (res_string + '.')
#
#
# def main():
#     phrase_len = input(
#         "This program creates a phrase from random words. \nWhat is the length of the phrase you want to make? ")
#     try:
#         phrase_len = int(phrase_len)
#         if not 2 < phrase_len <= 20:
#             raise ValueError
#     except (TypeError, ValueError):
#         print('Phrase length must be an integer between 2 and 20')
#         exit()
#     files = get_words_from_file()
#     print("\nYour phrase is: ")
#     print(get_random_sentence(phrase_len, files))
#
#
# main()

# # Exercise2
# # JSON
# import json
# sampleJson = """{
#    "company":{
#       "employee":{
#          "name":"emma",
#          "payable":{
#             "salary":7000,
#             "bonus":800
#          }
#       }
#    }
# }"""
# # Access the nested “salary” key from the JSON-string above.
# data = json.loads(sampleJson)
# salary = data["company"]["employee"]["payable"]["salary"]
# # Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# data["company"]["employee"]["birth_date"] = '12/05/1991'
# print(salary)
# print(data)
# # Save the dictionary as JSON to a file.
# with open('newfile.json','w') as f:
#     json.dump(data, f)


