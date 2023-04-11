def full_info(*info) -> str:
    out = ""
    for data in info:
        out += data + '\n'
    return out 

print(full_info('Lea', '30'))