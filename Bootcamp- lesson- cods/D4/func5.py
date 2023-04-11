def generate_info() -> tuple[int, str]:
    return 'Yossi', 'A'

def concat_str(str1, str2) -> str:
    concatenated = str1 + ' ' + str2
    return concatenated

def summarize_info() -> str:
    str1, str2 = generate_info()
    concatenated = concat_str(str1, str2)
    return concatenated

print(summarize_info())
