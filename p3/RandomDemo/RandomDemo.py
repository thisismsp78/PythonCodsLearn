from random import randint
length=int(input("Enter length : "))
min=int(input("Enter min : "))
max=int(input("Enter max : "))
if length>max-min+1:
    print("Invalid input !")
else:
    domain=[]
    while min<=max:
        domain.append(min)
        min+=1
    result=[]
    for item in range(length):
        index=randint(0,length-item)
        result.append(domain[index])
        domain[index]=domain[length-item-1]
    for number in result:
        print(number)
