def add_two(num1, num2) -> int:
    return num1 + num2

print(add_two(1,2))

def concat_str(str1, str2) -> str:
    concatenated = str1 + ' ' + str2
    return concatenated

res = concat_str('Hello', 'There')

def separate_str(text) -> tuple[str, str]:
    str1, str2 = text.split(' ')
    return str1, str2 

str1, str2 = separate_str(res)
print(str1)
print(str2)