from random import randint

numbers=[]
length=int(input("Enter length : "))
min=int(input("Enter min : "))
max=int(input("Enter max : "))
count=0
while(len(numbers)<length):
    count+=1
    randomNumber=randint(min,max)
    if (randomNumber in numbers)==False:
        numbers.append(randomNumber)

for number in numbers:
    print(number)

print("Count : ",count)