sample_dict = {
   "class":{
      "student":{
         "name":"Mike",
         "marks":{
            "physics":70,
            "history":80
         }
      }
   }
}

x = sample_dict["class"]["student"]["marks"]["history"]
print(x)
history_mark = None
current_dict = sample_dict

while True:
   if "history" in current_dict:
       history_mark = current_dict["history"]
       break
   else:
       for key in current_dict:
           if isinstance(current_dict[key], dict):
               current_dict = current_dict[key]

print(history_mark)

sample_dict = {
   "name":"Kelly",
   "age":25,
   "salary":8000,
   "city":"New York"
}

keys_to_remove = ["name","salary"]
deleted = {}
for key in keys_to_remove:
   removed =sample_dict.pop(key)
   deleted[key] = removed
print(sample_dict)
print(removed)

word = "HELLO"
word_list = {index:char for index, char in enumerate(word)}
print(word_list)

numbers_1 = [num for num in range(11)]
numbers_2 = [num for num in range(11,22)]

print(numbers_1)
print(numbers_2)

connected = list(zip(numbers_1, numbers_2))
print(connected)

