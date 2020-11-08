from random import randint
first=[randint(0,100) for i in range(randint(1,10))]
first.sort()
print(first)
second=[randint(0,100) for i in range(randint(1,10))]
second.sort()
print(second)
result=[]
firstIndex=0
secondIndex=0
for time in range(len(first)+len(second)):
    if firstIndex==len(first) or (secondIndex<len(second) and first[firstIndex]>second[secondIndex]):
        result.append(second[secondIndex])
        secondIndex+=1
    else:
        result.append(first[firstIndex])
        firstIndex+=1
print(result)
