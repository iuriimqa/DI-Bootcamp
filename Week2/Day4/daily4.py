# # Matrix
# # To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, selecting only the alpha characters and connecting them. Then he replaces every group of symbols between two alpha characters by a space.
# #
# # Using his technique, try to decode this matrix.
# #
# # Hints:
# # Use
# # ● lists for storing data
# # ● Loops for going through the data
# # ● if/else statements to check the data
# # ● String for the output of the secret message
#
# # matrix = [[7, 'i', 3],
# #           ['T', 's', 'i'],
# #           ['h', '%', 'x']
# #           ['i', ' ', '#']
# #           ['s', 'M', ' ']
# #           ['$', 'a', ' ']
# #           ['#', 't', '%']
# #           ['^', 'r', '!']
# #           ]
#
# matrix_str = '''7i3
# Tsi
# h%x
# i #
# sM
# $a
# #t%
# ^r!'''
#
# matrix_list = list(matrix_str)
# print(matrix_list)
#
# column1 = matrix_list[0::4]
# column2 = matrix_list[1::4]
# column3 = matrix_list[2::4]
# print(column1)
# print(column2)
# print(column3)
#
# def proc_column(column: list[str]) -> str:
#     message = ''
#     non_aplpha = 0
#     for char in column:
#         if char.isalpha():
#             message += char
#             non_aplpha = 0
#         else:
#             non_aplpha += 1
#             if non_aplpha >= 2 and message[-1] != ' ':
#                 message += ' '
#     return message
#
# message1 = proc_column(column1)
# message2 = proc_column(column2)
# message3 = proc_column(column3)
#
# print(message1+message2+message3)
