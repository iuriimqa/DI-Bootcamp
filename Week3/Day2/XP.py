# # Exercise1
# # Using this code:
# #
# # class Pets():
# #     def __init__(self, animals):
# #         self.animals = animals
# #
# #     def walk(self):
# #         for animal in self.animals:
# #             print(animal.walk())
# #
# # class Cat():
# #     is_lazy = True
# #
# #     def __init__(self, name, age):
# #         self.name = name
# #         self.age = age
# #
# #     def walk(self):
# #         return f'{self.name} is just walking around'
# #
# # class Bengal(Cat):
# #     def sing(self, sounds):
# #         return f'{sounds}'
# #
# # class Chartreux(Cat):
# #     def sing(self, sounds):
# #         return f'{sounds}'
# #
# #
# # Create another cat breed named Siamese which inherits from the Cat class.
# # Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# # Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# # Take all the cats for a walk, use the walk method.
#
# class Pets():
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Siamise(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# bengal = Bengal('Vasya',5)
# chartreux =Chartreux('Petya',7)
# siamis = Siamise('Shura',3)
# allcats =[bengal, chartreux, siamis]
#
# sara_pets = Pets(allcats)
# sara_pets.walk()

# # Exercise2
# # Create a class called Dog with the following attributes name, age, weight.
# # Implement the following methods in the Dog class:
# # bark: returns a string which states: “<dog_name> is barking”.
# # run_speed: returns the dogs running speed (weight/age*10).
# # fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.
# #
# # Create 3 dogs and run them through your class.
#
# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#
#     def bark(self):
#         barking = print(f'{self.name,"is barking"}')
#         return barking
#
#     def run_speed(self):
#         speed = (self.weight/self.age*10)
#         return speed
#     def fight(self, other_dog):
#         if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
#             winner = print(f'{"The winner is ",self.name}')
#         else:
#             winner = print(f'{"The winner is ",other_dog.name}')
#         return winner
#
# dog1 = Dog('Puppy',5,20)
# dog2 = Dog('Max',7,30)
# dog3 = Dog('Bob', 8,50)
#
# dog1.bark()
# dog2.bark()
# dog3.bark()
#
# dog1.run_speed()
# dog2.run_speed()
# dog3.run_speed()
#
# dog2.fight(dog3)
#
