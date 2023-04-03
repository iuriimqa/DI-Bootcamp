# class Animal:
#
#     def __init__(self, name:str):
#         self.name = name
#
#     def breathing(self):
#         out = f'{self.name} breaths'
#         print(out)
#
# class Mammal(Animal):#child
#     def __init__(self,name:str,lungs:int):
#         super().__init__(name)
#         self.lungs = 2
#
#     def produce_milk(self):
#         out =f'{self.name} produces milk'
#         print(out)
#
#
# class SeaMammal(Mammal):
#     def hold_breath(self):
#         super().__init__(name,lungs)
#         out = f'{self.name} holds breath'
#         print(out)
#
#
#
# dolphin = SeaMammal('dolphin')
# dolphin.hold_breath()
#
#
# class Door:
#     def __init__(self, is_opened:str) -> str:
#         self.is_opened = is_opened
#
#     def open_door(self):
#         self.is_opened = True
#
#     def close_door(self):
#         self.is_opened = False
#
# class BlockedDoor(Door):
#
#     def open_door(self):
#         raise TypeError('Blocked Door cannot be opened! ')
#
#     def close_door(self):
#         raise TypeError('Blocked Door cannot be closed! ')
#
# blocked = BlockedDoor
# d = {}
#
# try:
#         # blocked.open()
#      if d['Hello'] == 1:
#          pass
#
# except(TypeError):
#         print('Someone trying to open a Blocked door!')
# except KeyError:
#         print('Invalid Key')
# except ValueError:
#         print('Invalid Value')
#
# finally:
#     print('But finally is always work')




   # print("SOMETHING")

password = 1234

while True:
  try:
    user_pass = int(input(" Please type a password "))
    if user_pass == password:
        print("Welcome")
        break
  except (ValueError):
    print('Please input numbers')
