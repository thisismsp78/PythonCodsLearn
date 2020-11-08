from random import randint

numbers=[]
length=int(input("Enter length : "))
min=int(input("Enter min : "))
max=int(input("Enter max : "))
for i in range(0,length):
    numbers.append(randint(min,max))
    print(numbers[i])
