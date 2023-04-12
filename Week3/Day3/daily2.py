# Daily1
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.
#
# Other abilities of a Circle instance:
#
# Compute the circle’s area
# Print the circle and get something nice
# Be able to add two circles together
# Be able to compare two circles to see which is bigger
# Be able to compare two circles and see if there are equal
# Be able to put them in a list and sort them

# from math import pi
#
#
# class Circle:
# 	name = 'Circle'
#
# 	def __init__(self, radius):
# 		self.radius = radius
#
# 	def get_area(self):
# 		return pi * (self.radius ** 2)  # f = p*R^2
#
#
# circle1 = Circle(1)
# circle2 = Circle(2)
# circle3 = Circle(3)
#
# circle_sum_r = circle1.radius + circle2.radius
# circle_dif_r = circle1.radius > circle2.radius
# circle_eq_r = circle1.radius == circle2.radius
# circle_list = [circle3, circle1, circle2]
# circle_list = sorted(circle_list, key=lambda x: x.radius)  # sort list
# # sorted(circle_list, key=lambda x: x.radius)
# for x in circle_list:  # sort list and take only radius
# 	print(x.radius)
#
# print(circle1.name)
# print(circle1.radius)
# print(circle2.radius)
# print(circle3.radius)
# print(circle1.get_area())
# print(circle2.get_area())
# print(circle3.get_area())
# print(circle_sum_r)
# print(circle_dif_r)
# print(circle_eq_r)
# # print(circle_list.sort)


# import translate
# # Daily2
# # Consider this list
# #
# # french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
# # Look at this result :
# # {"Bonjour": "Hello", "Au revoir": "Goodbye", "Bienvenue": "Welcome", "A bientôt": "See you soon"}
# # You have to recreate the result using a translator module.
#
# from deep_translator import GoogleTranslator
# french_words= ["Bonjour", "Au revoir", "Bienvenue", "A bientôt"]
# trans_dict={}
# for p in french_words:
# 	translated = GoogleTranslator(source='french', target='en').translate(p)
# 	print(translated)
# 	trans_dict[p]=translated
# print (trans_dict)


