from random import randint
numbers=[randint(0,100) for i in range(10)]
print(numbers)
time=0
#be tedade aza
while time<len(numbers):
    index=0
    switched=False
    while index<len(numbers)-1-time:
        if numbers[index]>numbers[index+1]:
            temp=numbers[index]
            numbers[index]=numbers[index+1]
            numbers[index+1]=temp
            switched=True
        index+=1    
    if switched==False:
        print(time)
        break
    time+=1
print(numbers)
