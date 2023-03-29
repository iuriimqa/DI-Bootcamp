# def print_something() -> None:
#     print("SOMETHING")
#
# for i in range(20):
#     print_something()
#
# def add_two(num1,num2) -> int:
#     return num1+num2
#
#     print(add_two(1,2))

# def concrat_str(str1,str2) ->str:
#         concatenated = str1 + '' + str2
#
#         print(concrat_str('Hello', 'There'))
# def separate_str(text) -> tuple[str,str]:
#     str1, str2 = text.split(' ')
#     return str1, str2

# str1,str2 = separate_str(res)

# def calculation(a: int, b: int) ->tuple[int, int]:
#      add = a+b
#      sub = a-b
#      mod = a*b
#      return add,sub,mod
#
# res= calculation(5,20)
# print(res)

# def sunny_dark(hour: int) -> str | None:
#     if 10 < hour <18:
#         return "sunny"
#     elif 24> hour > 10 or 0 < hour <10:
#         return "dark"
#     else:
#         return None
#
# print(sunny_dark(10))

# def full_info(**kwargs):
#     print(kwargs)
#
# print(full_info(first_name ='Lea', country = 'IL'))
#
#
# def calcuation(a:int, limit:int) -> int:
#     base ='1'
#     res = 0
#     for i in range(1,limit+1):
#         multiplicator = base * i
#         multiplicator = int(multiplicator)
#         res += a * multiplicator
#
#     return res
# print(calcuation(3,8))

# lambda function


# add_two =

words = ['dog','cat','ball']
result_list = list(map(lambda s:s.capitalize(), words))
print(result_list)