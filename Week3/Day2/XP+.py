# # # Daily1
# # Create a class called Family and implement the following attributes:
# #
# # members: list of dictionaries with the following keys : name, age, gender and is_child (boolean).
# # last_name : (string)
# # Initial members data:
# class Family:
#
#     def __init__(self,last_name, members):
#         self.last_name = last_name
#         self.members = members
#
#     def born(self,**kwargs):
#             self.members.append(kwargs)
#             print("Congratulations on the birth of a new family member: ",
#               kwargs['name'])
#
#     def is_18(self, name):
#             return ([n['age'] for n in members if n['name'] == name][0] > 18)
#
#     def family_presentation(self):
#      print(f"Member's of Family: ")
#
#      for p in members:
#             print(p['name'])
#
#
# members = [
#     {'name':'Michael','age':35,'gender':'Male','is_child':False},
#     {'name':'Sarah','age':32,'gender':'Female','is_child':False}
# ]
#
# family2 = Family('Stivenson',members)
# boy = {'name':'Max','age':10,'gender':'Male','is_child':True}
# family2.born(**boy)
#
# print(members)
# print(Family.is_18('Stivenson','Michael'))
# print(Family.family_presentation('Stivenson'))

Daily2
