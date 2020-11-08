rows=[]
family=""
name=""
phone=""
while True:
    print("1-New")
    print("2-Search")
    print("3-Print")
    print("4-Filter")
    print("5-Exit")
    select=int(input("Select : "))
    if select==1:
        family=input("Enter family : ")
        name=input("Enter name : ")
        phone=input("Enter phone : ")
        rows.append(",".join([family,name,phone]))
    elif select==2:
        family=input("Enter family : ")
        name=input("Enter name : ")
        phone="Not exists !"
        for row in rows:
            fields=row.split(",")
            if fields[0]==family and fields[1]==name:
                phone=fields[2]
                break
        print(phone)
    elif select==3:
        for row in rows:
            fields=row.split(",")
            print(f"{fields[0]}{''.join([' ' for x in range(25-len(fields[0]))])} | {fields[1]}{''.join(' ' for x in range(25-len(fields[1])))} | {fields[2]}")
    elif select==4:
        family=input("Enter family : ")
        name=input("Enter name : ")
        for row in rows:
            fields=row.split(",")
            if family in fields[0] and name in fields[1]:
                print(f"{fields[0]}{''.join([' ' for x in range(25-len(fields[0]))])} | {fields[1]}{''.join(' ' for x in range(25-len(fields[1])))} | {fields[2]}")
    elif select==5:
        break
