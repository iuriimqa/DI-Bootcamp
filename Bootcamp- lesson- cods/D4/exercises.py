def calculation(a: int, b: int) -> tuple[int, int]:
    add = a + b
    sub = a - b
    return add, sub

res = calculation(5, 10)
# print(res)



def multiply_add(num: int, limit: int) -> int:
    base = '1'
    res = 0

    for i in range(1, limit + 1):
        multiplicator = base * i # '11'
        multiplicator = int(multiplicator) # 11
        res += num * multiplicator

    return res

print(multiply_add(3, 4))
