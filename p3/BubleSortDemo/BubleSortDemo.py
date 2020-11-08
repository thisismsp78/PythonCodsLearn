from random import randint
#numbers=[9,0,8,2,7,3,6,4,5]
numbers=[randint(0,100) for i in range(10)]
print(numbers)
#daghighan be tedade aza
for time in range(len(numbers)):
    #aza ra 2 be 2 moghayese va dar soorate lozoom jabeja kon
    switched=False
    for index in range(len(numbers)-1-time):
        if(numbers[index]>numbers[index+1]):
            #in ozv zakhire dar temp
            temp=numbers[index]
            #badi jaye ghabli
            numbers[index]=numbers[index+1]
            #temp be jaye baadi
            numbers[index+1]=temp
            switched=True
    if switched==False:
        print("Time : ",time)
        break        

print(numbers)