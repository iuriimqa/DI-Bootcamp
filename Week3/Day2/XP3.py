# # Exercise3
# # Create a new python file and import your Dog class from the previous exercise.
# # In the new python file, create a class named PetDog that inherits from Dog.
# # Add an attribute called trained to the __init__ method, this attribute is a boolean and the value should be False by default.
# # Add the following methods:
# # train: prints the output of bark and switches the trained boolean to True
# #
# # play: takes a parameter which value is a few names of other Dog instances (use *args). The method should print the following string: “dog_names all play together”.
# #
# # do_a_trick: If the dog is trained the method should print one of the following sentences at random:
# # “dog_name does a barrel roll”.
# # “dog_name stands on his back legs”.
# # “dog_name shakes your hand”.
# # “dog_name plays dead”.
# import random
# from XP import Dog
#
# class PetDog(Dog):
#     def __init__(self,name,age,weight,trained=False):
#      super().__init__(name, age, weight)
#      self.trained = trained
#
#     def train(self):
#          self.bark()
#          self.trained = True
#
#     def play(self,*args):
#              dog_list = [n.name for n in args]
#              dog_list.append(self.name)
#              dog_list = ", ".join(dog_list)
#              print(f"{dog_list} all play together!")
#
#     def do_a_trick(self):
#          if self.trained:
#              trick_list = ['does a barrel roll', 'stands on his back legs', 'shakes your hand', 'plays dead']
#              trick = random.choice(trick_list)
#              print(f"{self.name} {trick}")
#
# dog1 = PetDog('Pup',5,10)
# dog2 = PetDog('Bobs',7,15)
# dog3 = PetDog('Nan',5,25)
# dog4 = PetDog('Mom',10,30)
#
# dog2.do_a_trick()
# dog2.train()
# dog2.play(dog3,dog4,dog1)
# dog2.do_a_trick()





