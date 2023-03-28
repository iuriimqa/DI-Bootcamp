list1 = [5,10,15,20,25,50,20]
idx = list1.index(20)
list1[idx] = 200
print(list1)


number = input("Input your number? ")
for i in range(1,11):
    print(number,'x',i,'=',number*i)

while i != 10:
    print(i+1)