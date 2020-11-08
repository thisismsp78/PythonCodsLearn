name=input("Enter name : ")
result=""
for index in range(1,len(name)+1):
    #print(index*-1)
    #print(name[index*-1])
    result+=name[index*-1]
print(result)