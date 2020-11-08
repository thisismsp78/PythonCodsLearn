
def maxmin(numbers):
    min=numbers[0]
    max=numbers[0]
    for number in numbers:
        if number<min:
            min=number
        elif number>max:
            max=number
    return (min,max)


#print(maxmin([9,0,5,7,4,8]))
minValue,maxValue=maxmin([9,0,5,7,4,8])
print("Min : ",minValue)
print("Max : ",maxValue)