total_price = 0

family_info = [('Brad', 14), ('David', 44), ('Monica', 6)]

for name, age in family_info:

    if age < 3:
        continue
    elif 3 <= age <= 12:
        total_price += 10
    else: 
        total_price += 15

print("Total price:", total_price)





teenagers = ['Adam', 'Roy', 'Billy']
teenagers_info = []

for teenager in teenagers: 

    age = input(f"Hi {teenager}, What's your age? ")
    age_int = int(age)
    info = (teenager, age_int)
    teenagers_info.append(info)

eligible = []
for name, age in teenagers_info:

    if 16 < age < 21:
        continue
    eligible.append(name)

print("Eligible:", eligible)