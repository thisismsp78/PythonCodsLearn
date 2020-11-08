number=int(input("Enter number : "))
half=number//2
result="Prime"
while half>1:
    if number%half==0:
        result="Complex"
        break
    half-=1
print(result)