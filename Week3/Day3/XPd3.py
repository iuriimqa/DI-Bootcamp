# # # Exercise1
# # # Write a program which prints the results of the following python built-in functions: abs(), int(), input().
# # # Using the __doc__ dunder method create your own documentation which explains the execution of your code. Take a look at the doc method on google for help.
# #
# def abs1(a=-7.5):
#     """The abs() function returns the absolute value of the specified number."""
#     abs1 = abs(a)
#     return abs1
#
# def int1(a="-20"):
#     """The int() function converts the specified value into an integer number"""
#     int1 = int(a)
#     return int1
#
# def input1():
#     """The input() function allows user input."""
#     input1 = input("Print something here ")
#     return input1
#
# print(abs1())
# print(int1())
# print(input1())
#
# print(abs1.__doc__)
# print(int1.__doc__)
# print(input1.__doc__)
#
# # Exercise2
# # class Currency:
# #     def __init__(self, currency, amount):
# #         self.currency = currency
# #         self.amount = amount
# #
# #     #Your code starts HERE
# #
# #
# # Using the code above, implement the relevant methods and dunder methods which will output the results below.
# # Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# # >>> c1 = Currency('dollar', 5)
# # >>> c2 = Currency('dollar', 10)
# # >>> c3 = Currency('shekel', 1)
# # >>> c4 = Currency('shekel', 10)
# #
# # >>> str(c1)
# # '5 dollars'
# #
# # >>> int(c1)
# # 5
# #
# # >>> repr(c1)
# # '5 dollars'
# #
# # >>> c1 + 5
# # 10
# #
# # >>> c1 + c2
# # 15
# #
# # >>> c1
# # 5 dollars
# #
# # >>> c1 += 5
# # >>> c1
# # 10 dollars
# #
# # >>> c1 += c2
# # >>> c1
# # 20 dollars
# #
# # >>> c1 + c3
# # TypeError: Cannot add between Currency type <dollar> and <shekel>
# class Currency:
#     def __init__(self, currency, amount):
#         self.amount = amount
#         self.currency = currency
#
#
#     def __str__(self):
#         return str(self.amount)+str(self.currency)
#
#
#     def __int__(self):
#         return int(self.amount)
#
#     def __add__(self, other):
#         if type(other) == int:
#             self.amount + other
#             return self
#         elif type(other) == type(self):
#             if self.currency == other.currency:
#                 self.amount + other.amount
#                 return self
#             else:
#                 raise TypeError("Cannot add between different Currency type")
#
#     def __iadd__(self, other):
#         if type(other) == int:
#             self.amount += other
#             return self
#         elif type(other) == type(self):
#             if self.currency == other.currency:
#                self.amount += other.amount
#                return self
#
#             else:
#                 raise TypeError("Cannot add between different Currency type")
#
#
#         return isum
#
#     def __repr__(self):
#         return str(self.amount)+str(self.currency)
#
#
#
# c1 = Currency('dollar', 5)
# c2 = Currency('dollar', 10)
# c3 = Currency('shekel', 1)
# c4 = Currency('shekel', 10)
#
# print(str(c1))
# print(int(c1))
# print(repr(c1))
# c1+5
# c1+c1
# print(c1)
# c1+=5
# print(c1)
# print(type(c1), type(c2))
# c1 += c2
# print(c1)
# c1 += c3
# print(c1)
