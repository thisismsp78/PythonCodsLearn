courses={}
while True:
    print("1-New")
    print("2-Delete")
    print("3-Exit")
    select=int(input("Select : "))
    if select==1:
        newName=input("Enter new name : ")
        newTime=int(input("Enter new time : "))
        courses.update([(newName,newTime)])
        print(courses)
    elif select==2:
        deleteName=input("Enter new name : ")
        del courses[deleteName]
        print(courses)
    else:
        break
