# # Exercise2
# # Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
# # if it’s the same number, display a success message to the user, else don’t.
# import random
# from random import randint
  # def combinated():
  #       a = input("Please input numbers from 1 to 100?")
  #       b = random.randint(1,100)
  #       if a == b:
  #       res = print("Success!You winner!")
  #       else:
  #       res = print("Sorry")
  #       return res
# combinated()
import datetime
# # Exercise3
# # Generate random String of length 5
# # Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# # Hint: use the string module
# from random import randint
# import string
# my_abc = string.ascii_letters
# my_string = ''
# for i in range(5):
#     my_string += my_abc[random.randint(1, len(my_abc))]
# print(my_string)

# # Exercise4
# # Create a function that displays the current date.
# # Hint : Use the datetime module.
#
# import datetime
# def dt():
#     d = print(datetime.datetime.now())
#     return d
# dt()

# # Exercise5
# # Create a function that displays the amount of time left from now until January 1st.
# # (Example: the 1st of January is in 10 days and 10:34:01hours).

# ny='2024-01-01'
# ny=ny.split("-")
# date1=datetime.date(int(ny[0]),int(ny[1]),int(ny[2]))
# days=datetime.date.today()-date1
# print(days)

# Exercise6

# bt_date='1991-05-13'
# bt_date=bt_date.split("-")
# date1=datetime.date(int(bt_date[0]),int(bt_date[1]),int(bt_date[2]))
# days=datetime.date.today()-date1
# print("Minutes lived: ", int(days.total_seconds()/60))

# # Exercise7
# to_date=datetime.date.today()
# print(f"To date: {to_date}")
# ny_date='2023-04-06'
# ny_date=ny_date.split("-")
# h_date=datetime.date(int(ny_date[0]),int(ny_date[1]),int(ny_date[2]))
# days=h_date-to_date
# print(days)
#
# Exercise9

# from faker import Faker
# fake = Faker()
# user_list=[]
# for i in range(5):
#     name=fake.name()
#     addres=fake.address()
#     language=fake.language_code()
#     user_list.append({'name':name, 'addres':addres, 'language':language})
# print (user_list)