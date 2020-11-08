numbers=[2,4,6,8]

while True:
    search=int(input("Enter number : "))
    if search==-1:
        break
    for number in numbers:
        if number==search:
            print("Exists")
            break
    else:
        print("Not exists !")