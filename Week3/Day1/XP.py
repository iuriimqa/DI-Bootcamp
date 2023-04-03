# Exercise1
# Using this class
#
# class Cat:
#     def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
# Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.
# class Cat:
#   cat_list=[]
#   def __init__(self, cat_name, cat_age):
#         self.name = cat_name
#         self.age = cat_age
#         Cat.cat_list.append(self)
#
# c1 = Cat('Felix', 5)
# c2 = Cat('Smell', 15)
# c3 = Cat('Sebastiyan', 20)
# c4 = Cat('Mel', 13)
# def oldest_cat(cat_list:list) -> Cat:
#     oldest = cat_list[0]
#     for cat in cat_list:
#         if cat.age>oldest.age:
#             oldest = cat
#     return oldest
# result = oldest_cat(cat_list=Cat.cat_list)
# print(result.name)

# # Exercise2
# # Create a class called Dog.
# # In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
# # Create a method called bark that prints the following string “<dog_name> goes woof!”.
# # Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.
# # Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.
# # Print the details of his dog (ie. name and height) and call the methods bark and jump.
# # Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# # Print the details of her dog (ie. name and height) and call the methods bark and jump.
# # Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.
# class Dog:
#     dog_list=[]
#     def __init__(self, dog_name, dog_height):
#         self.name = dog_name
#         self.height = dog_height
#         Dog.dog_list.append(self)
#     def bark(self):
#         print(self.name+" goes woof! ")
#
#     def jump(self):
#         x = self.height * 2
#         print(f'{self.name} jumps {x} cm height!')
#
#
# davids_dog = Dog('Rex', 50)
# sarahs_dog = Dog('Teacup', 20)
# third_dog = Dog('Pluto', 10)
# My_dog = Dog('Bob', 70)
#
# def heighest_dog(dog_list:list) -> Dog:
#     heighest = dog_list[0]
#     for dog in dog_list:
#         if dog.height > heighest.height:
#             heighest = dog
#     return heighest
# result = heighest_dog(dog_list=Dog.dog_list)
#
# davids_dog.bark()
# davids_dog.jump()
#
# sarahs_dog.bark()
# sarahs_dog.jump()
#
# print(result.name)

# # Exercise3
# # Define a class called Song, it will show the lyrics of a song.
# # Its __init__() method should have two arguments: self and lyrics (a list).
# # Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.
# # Create an object, for example:
# #
# # stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# # Then, call the sing_me_a_song method. The output should be:
#
# class Song:
#     def __init__(self, song, lyrics):
#         self.song = song
#         self.lyrics = lyrics
#     def sing_me_a_song(self):
#         print(self.lyrics)
#
# S1 = Song("Song1", "There’s a lady who's sure all that glitters is gold and she’s buying a stairway to heaven")
# Timati =Song('Timati',"Some rap dirty talks about moms and sons")
#
# S1.sing_me_a_song()

# # Exercise4
# # Create a class called Zoo.
# # In this class create a method __init__ that takes one parameter: zoo_name.
# # It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# # Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# # Create a method called get_animals that prints all the animals of the zoo.
# # Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.
# # Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# # Example
# #
# # {
# #     1: "Ape",
# #     2: ["Baboon", "Bear"],
# #     3: ['Cat', 'Cougar'],
# #     4: ['Eel', 'Emu']
# # }
# #
# #
# # Create a method called get_groups that prints the animal/animals inside each group.
# #
# # Create an object called ramat_gan_safari and call all the methods.
# # Tip: The zookeeper is the one who will use this class.
class Zoo:

    # In this class create a method __init__ that takes one parameter: zoo_name.It instantiates two attributes: animals(an empty list) and name(name of the zoo).
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def add_animal(self):
         new_animal = input('Type animal to add ')
         self.animals.append(new_animal)

    def get_animals(self):
          print(self.animals)

    def sell_animal(self):
         animal_sold = input('What animal you want to remove? ')
         self.animals.remove(animal_sold)
         print(self.animals)

    def sort_animals(self):
        animals = sorted(self.animals)
        zoo_list = []
        zoo_list.append([animals[0]])
        for i in range(1,len(animals)):
            if animals[i][0] != animals[i-1][0]:
                zoo_list.append([])
            zoo_list[-1].append(animals[i])
        zoo_list = enumerate(zoo_list)
        for i in zoo_list:
            print((f'{i[0]+1}:{i[1]}'))


        print(list(zoo_list))

    def ramatgan_safari(self):
        zoo.add_animal()
        zoo.add_animal()
        zoo.add_animal()
        zoo.add_animal()
        zoo.sell_animal()
        zoo.sort_animals()


zoo = Zoo('Ramat-gan')

# zoo.add_animal()
# zoo.add_animal()
# zoo.add_animal()
#
#
# zoo.sort_animals()

zoo.ramatgan_safari()



