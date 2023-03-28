# # # Exercise1
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
#
# my_fav_numbers = {1,2,3,4,6,7,7,7,7,7}
# my_fav_numbers.add(8)
# my_fav_numbers.add(9)
# my_fav_numbers.remove(9)
# print(my_fav_numbers)
#
# friend_fav_numbers = {3,3,3,5,5,5,10,11,13}
# print(friend_fav_numbers)
#
# our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
# print(our_fav_numbers)

# Exercise2
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

# No, tuple is unchangenable.You can add only another tuple

# # Exercise3
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];
#
# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)


# basket = ["Banana","Apples","Oranges","Blueberries"]
# basket.pop(0)
# basket.pop(-1)
# basket.append("Kiwi")
# basket.insert(0,"Apples")
# print(basket.count("Apples"))
# basket.clear()
# print(basket)
#
# # Exercise4
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

# Integer is "2","3","4". Float is "2.0","3.5","4.5".
# Yes
# [print(x /2, end=" ") for x in range(3, 11, 1)]

# Exercise5
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

# for i in range(1,21,1):
#   if i%2 == 0:
#       print(i)


# Exercise6

# while True:
#     response = input("What's your name? ")
#     if (response == "Yuri"):
#         print("Welcome")
#         break

# Exercise7
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.

# fruits = input("What your favorite fruits, separeted with space? ")
# store = fruits.split()
# # print(store)
# # store = list(fruits)
# inp = input("Please input one fruit ?")
# found = ''
# for fruit in store:
#     if fruit == inp:
#         found = "Wow it's your favorite fruit!"
# if found == "":
#     found = "You chose a new fruit. I hope you enjoy"
# print(found)


    # print("You chose a new fruit. I hope you enjoy")


# Exercise8
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

#
#
# toppings = []
#
# topping = input("Topping or Quit: ")
#
# while topping != "quit":
#
#     toppings.append(topping)
#     print(f"Adding {topping} to pizza")
#     topping = input("Topping or Quit: ")
#
# base_price = 10
# toppings_price = 2.5 * len(toppings)
#
# total_price = base_price + toppings_price
#
# print("TOPPINGS:", toppings, "Total price:", total_price)

# Exercise9
#
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
#
# Ask a family the age of each person who wants a ticket.
#
# Store the total cost of all the family’s tickets and print it out.
#
# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.
#
# total_price = 0
#
# family_info = [('Brad', 14), ('David', 44), ('Monica', 6)]
#
# for name, age in family_info:
#
#     if age < 3:
#         continue
#     elif 3 <= age <= 12:
#         total_price += 10
#     else:
#         total_price += 15
#
# print("Total price:", total_price)
#
#
# teenagers = ['Adam', 'Roy', 'Billy']
# teenagers_info = []
#
# for teenager in teenagers:
#
#     age = input(f"Hi {teenager}, What's your age? ")
#     age_int = int(age)
#     info = (teenager, age_int)
#     teenagers_info.append(info)
#
# eligible = []
# for name, age in teenagers_info:
#
#     if 16 < age < 21:
#         continue
#     eligible.append(name)
#
# print("Eligible:", eligible)

# Exercise10
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
#
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.

# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# finished_sandwiches = []
# for i in sandwich_orders:
#     finished_sandwiches.append(i)
# print("All sandwiches: ", finished_sandwiches, "done. ")

# Exercise11
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.

print("The deli has run out of pastrami..")
finished_sandwiches = []
sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich", "Pastrami sandwich", "Pastrami sandwich"]
del_sandwiches = "Pastrami sandwich"
while del_sandwiches in sandwich_orders:
        sandwich_orders.remove(del_sandwiches)
finished_sandwiches.extend(sandwich_orders)
print(finished_sandwiches)
