numbers=[2,7,8,3,9,4,15,6]
min=0
max=numbers[0]
for number in numbers:
    if number<min:
        min=number
    if number>max:
        max=number
print("Min : ",min)
print("Max : ",max)