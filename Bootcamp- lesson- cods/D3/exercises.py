# 1
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






# 2
sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"

}

keys_to_remove = ["name", "salary"]
deleted = {}
for key in keys_to_remove:
    # del sample_dict[key]
    removed = sample_dict.pop(key)
    deleted[key] = removed

print(sample_dict)

print("Removed:", deleted)



