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
        rows.append({'family':family,'name':name,'phone':phone})
    elif select==2:
        family=input("Enter family : ")
        name=input("Enter name : ")
        phone="Not exists !"
        for row in rows:
            if row['family']==family and row['name']==name:
                phone=row['phone']
                break
        print(phone)
    elif select==3:
        for row in rows:
            print(f"{row['family']}{''.join([' ' for x in range(25-len(row['family']))])} | {row['name']}{''.join(' ' for x in range(25-len(row['name'])))} | {row['phone']}")
    elif select==4:
        family=input("Enter family : ")
        name=input("Enter name : ")
        for row in rows:
            if family in row['family'] and name in row['name']:
                print(f"{row['family']}{''.join([' ' for x in range(25-len(row['family']))])} | {row['name']}{''.join(' ' for x in range(25-len(row['name'])))} | {row['phone']}")
    elif select==5:
        break

