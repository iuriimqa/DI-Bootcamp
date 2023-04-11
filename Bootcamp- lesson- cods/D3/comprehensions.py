numbers = []

for num in range(100):
    if num % 2 == 0:
        numbers.append(num)

# print(numbers)
        # what_to_add(2,4,6..) for number in range(100)
numbers = [num for num in range(100) if num % 2 == 0]

print(numbers)

# 
alpha = 'אבגדה'
heb_dict = dict(enumerate(alpha)) 
# {0: 'א', 1: 'ב', 2: 'ג', 3: 'ד', 4: 'ה'}

even_letters = [value for key, value in heb_dict.items() if key % 2 == 1]

print(even_letters)

even_letters = {key: value for key, value in heb_dict.items() if key % 2 == 1}

print(even_letters)




word = "HEllo"

word_list = [char for char in word if char != 'l']

print(word_list)

word = "HEllO"

word_dict = {index: char for index, char in enumerate(word)}

print(word_dict)