from random import randint

numbers=[]
for i in range(0,10):
    numbers.append(randint(0,100))
    print(numbers[i])
min=numbers[0]
max=numbers[0]
for number in numbers:
    if number<min:
        min=number
    if number>max:
        max=number
print("Min : ",min)
print("Max : ",max)
