# CREATE

a_set = {1,2,3}

a_dict = {100: "And then something happend"}

b_dict = {'first_name': 'Yossi',
          'last_name': 'Eik',
          'age': 31, 
          'residence': 'Tel Aviv',
          'languages': ['python', 'js', 'html']}

# Get data

# print(b_dict['first_name'])
# print(b_dict['languages'][0])

b_dict.get('planet', 'earth') # return 'earth' if 'planet' key not found
 
# get the keys
b_dict.keys()
# get the values 
b_dict.values()

# Update 

b_dict['country'] = 'Israel' # adds new key and value
b_dict.update({'residence': 'Tel Aviv',
               'languages': ['python', 'js', 'html']})

a_dict[100] = 'something' # overwriting

# Delete

removed = b_dict.pop('country') 
# del b_dict['country']

b_dict.clear() # remove all keys and values


# Loops


b_dict = {'first_name': 'Yossi',
          'last_name': 'Eik',
          'age': 31, 
          'residence': 'Tel Aviv',
          'languages': ['python', 'js', 'html']}

full_name = ""
for key in b_dict:
    print(key)
    if key == 'first_name' or key == 'last_name':
        full_name += f'{b_dict[key]} '

print(full_name)

for value in b_dict.values():
    print(value)

for key, value in b_dict.items():
    print(f"Key: {key}, Value: {value}")

