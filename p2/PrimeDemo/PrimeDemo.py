number=int(input("Enter number : "))
half=number//2
while half>1:
    if number%half==0:
        print("Complex")
        break
    half-=1
else:
    print("Prime")