number=int(input("Enter number : "))
half=number//2
while half>1:
    if number%half==0:
        print("Complex")
    half-=1
print("Prime")
    #else:
    #    print("Prime")