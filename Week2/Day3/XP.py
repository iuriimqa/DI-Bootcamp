# Exercise1
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# keys = ['Ten','Twenty','Thirty']
# values = [10, 20, 30]
# sample_dict = dict(zip(keys, values))
# print(sample_dict)

# Exercise2
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Given the following object:
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
#
# How much does each family member have to pay ?
#
# Print out the family’s total cost for the movies.



# family = {"rick": 3, 'beth': 13, 'morty': 13, 'summer': 8}
# totalprice = 0
# newlist = list(family.values())
# for i in newlist:
#     if 3< i <12:
#         totalprice = totalprice + 10
#     if i>12:
#         totalprice = totalprice + 15
# print(totalprice)
#
# Exercise3
# Here is some information about a brand.
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
#
#
# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
# 3.
# 4. Print a sentence that explains who Zaras clients are.
# 5. Add a key called country_creation with a value of Spain.
# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# 7. Delete the information about the date of creation.
# 8. Print the last international competitor.
# 9. Print the major clothes colors in the US.
# 10. Print the amount of key value pairs (ie. length of the dictionary).
# 11. Print the keys of the dictionary.
# 12. Create another dictionary called more_on_zara with the following details:
#
# creation_date: 1975
# number_stores: 10 000
#
#
# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# 14. Print the value of the key number_stores. What just happened ?

# brand = {
#     "name":"Zara",
#     "creation_date":1975,
#     "creator_name": "Amancio Ortega Gaona",
#     "type_of_clothes": ["men", "women", "children", "home"],
#     "international_competitors": ["Gap", "H&M", "Benetton"],
#     "number_stores": 7000,
#     "major_color": {
#         "France": "blue",
#         "Spain": "red",
#         "US": ["pink", "green"]
#     },
# }
# # Change the number of stores to 2.
# brand["number_stores"] = 2
# # Print a sentence that explains who Zaras clients are.
# print("Zara's clients are: ",brand["type_of_clothes"])
# # Add a key called country_creation with a value of Spain.
#
# brand["country_creation"] = "Spain"
#
# # Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
# if "international_competitors" in brand:
#     print("Yes")
# else:
#     print("No")
#
# brand["name"] = "Desigual","Zara"
# # Delete the information about the date of creation.
# brand.pop("creation_date")
# # Print the last international competitor.
# print(brand["international_competitors"][-1])
# # Print the major clothes colors in the US.
# print(brand["major_color"]['US'])
# # Print the amount of key value pairs (ie. length of the dictionary).
# print(len/(brand))
# # Print the keys of the dictionary.
# print(brand.keys())
#
# # Create another dictionary called more_on_zara with the following details:
# #
# # creation_date: 1975
# # number_stores: 10 000
#
# more_on_zara = {'creation_date':1975, 'number_stores':10000}
#
# # Use a method to add the information from the dictionary more_on_zara to the dictionary brand
#
# brand.update(more_on_zara)
# # Print the value of the key number_stores. What just happened
# print(brand["number_stores"])
# #
# Exercise4
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
numbers = [0, 1, 2, 3, 4]
users_dict = dict(zip(users, numbers))
print(users_dict)
print(users_dict)

users_dict2 = dict(zip(numbers, users))
print(users_dict2)
users.sort()
users_dict3 = dict(zip(users, numbers))
print(users_dict3)


user_dictc = {key: value for (key, value) in users_dict.items() if key.startswith('M') or key.startswith('P')}
print(user_dictc)

user_dict5 = {key: value for (key, value) in users_dict.items() if key.startswith('i')}
print(user_dict5)



