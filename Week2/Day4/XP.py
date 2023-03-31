# # Exercise1
# # Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# # Call the function, and make sure the message displays correctly.
#
# def display_message(a:str) -> str:
#     sent = print("I am learning" + a + "today")
#     return sent
# display_message(" Science ")

# # Exercise2
# # Write a function called favorite_book() that accepts one parameter called title.
# # The function should print a message, such as "One of my favorite books is <title>".
# # For example: “One of my favorite books is Alice in Wonderland”
# # Call the function, make sure to include a book title as an argument when calling the function.
#
# def favorite_book(title:str) ->str:
#     sent = print("One of my favorite books is  "+title+"! ")
#     return sent
# favorite_book("Harry Potter")

# # Exercise3
# # Write a function called describe_city() that accepts the name of a city and its country as parameters.
# # The function should print a simple sentence, such as "<city> is in <country>".
# # For example “Reykjavik is in Iceland”
# # Give the country parameter a default value.
# # Call your function.
#
# def describe_city(city:str,country:str) ->str:
#     sent = print("The "+city+" is the capital of "+country+". ")
#     return sent
# describe_city("Tel-aviv","Russia")

# # Exercise4
# # Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
# # Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.
#
# from random import randint
# def numberical(a:int) -> str | int:
#     b = randint(1,100)
#     if a == b:
#         print("Success")
#     else:
#         print("Fail", a, b)
# numberical(5)

# # Exercise5
# # Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# # The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# # Call the function make_shirt().
# #
# # Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# # Make a large shirt with the default message
# # Make medium shirt with the default message
# # Make a shirt of any size with a different message.
# #
# # Bonus: Call the function make_shirt() using keyword arguments.
#
# def make_shirt(size="large", text="I love Python") -> str:
#     shirt = print("The size of the shirt is: "+size+" and the text is: "+text)
#     return shirt
# make_shirt()

# # Exercise6
# # Using this list of magician’s names. magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# # Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
# # Write a function called make_great() that modifies the list of magicians by adding the phrase "the Great" to each magician’s name.
# # Call the function make_great().
# # Call the function show_magicians() to see that the list has actually been modified.
#
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# def show_magicians(a = magician_names) -> list:
#     for magician in magician_names:
#         magician_list = print(list(magician))
#     return magician_list
# show_magicians()
#
# def make_great(a = magician_names) -> list:
#     great_list = print(list(map(lambda a:" The Great "+ a, magician_names)))
#     return great_list
# make_great()
# show_magicians()

# Exercise7
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
#
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
#
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
#
# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().
#
# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

# from random import randint
# def get_random_temp() -> int:
#     a = randint(-10,40)
#     print(a)
#     return a
# get_random_temp()
# def main() -> str:
#     b = get_random_temp()
#     if b<0:
#       print("The temperature right now is:", b,"Celsium. ","Brrr, that’s freezing! Wear some extra layers today")
#     if 0<b<16:
#       print("The temperature right now is:", b, "Celsium. ","Quite chilly! Don’t forget your coat")
#     if 16<b<23:
#       print("The temperature right now is:", b, "Celsium. ", "Nice, Spring's weather")
#     if 24<b<32:
#       print("The temperature right now is:", b, "Celsium. ", "Wow!It's hot, be careful")
#     if 32<b<40:
#       print("The temperature right now is:", b, "Celsium. ", "Extremely hot, I think better to stay home today")
#
#     return b
# main()


#2
# from random import randint
# def get_random_temp() -> int:
#     season =input("Input season ?")
#     if season == 'spring':
#         top = 15
#         down = 5
#     if season == 'summer':
#         top = 35
#         down = 16
#     if season == 'autumn':
#         top = 4
#         down = -5
#     if season == 'winter':
#         top = -5
#         down = -20
#     a = randint(down,top)
#     print(a)
#     return a
# get_random_temp()

