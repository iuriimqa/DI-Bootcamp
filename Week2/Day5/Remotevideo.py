# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
# res = []
# for value in some_list:
#     if some_list.count(value)>1:
#         if value not in res:
#             res.append(value)
#
#
# print(res)

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for pixel in row:
        if (pixel == 1):
            print('*', '')
        else:
            print('', '')
        print(' ')

