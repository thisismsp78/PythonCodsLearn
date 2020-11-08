number=int(input("Enter number : "))
if number>100 or number<0:
    print("Invalid !")
elif number>75:
    print("A")
elif number>50:
    print("B")
elif number>25:
    print("C")
else:
    print("D")