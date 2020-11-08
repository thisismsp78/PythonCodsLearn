min=int(input("Min : "))
max=int(input("Max : "))
#result=[x*y for x in range(min,max) for y in range(min,max)]
result=[f"{x} * {y} = {x*y}" for x in range(min,max) for y in range(min,max)]
#print(result)
for data in result:
    print(data)
