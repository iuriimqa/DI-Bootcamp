filename = 'nameslist.txt'

with open(filename, 'r') as file:
    text = file.read()
print(text)

with open(filename, 'r') as file:
    text_line = list(file.readline(5))
print(text_line)




