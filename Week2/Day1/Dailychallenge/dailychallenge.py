st = input('Please input letters ')
if len(st)<10:
    print("string not long enough")
elif len(st)>10:
    print("string too long")
    print(st[0])
    print(st[-1])

letter = ""
for x in st:
    letter += x
    print(letter)


