from random import randint

numbers=[]
index=0
while index<10:
    numbers.append(randint(0,100))
    index+=1
#print(numbers)
for number in numbers:
    print(number)

