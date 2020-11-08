phonebook=[]
while True:
    print("1-New")
    print("2-Search")
    print("3-Print")
    print("4-Exit")
    select=int(input("Select : "))
    if select==1:
        family=input("Enter family : ")
        name=input("Enter name : ")
        phone=input("Enter phone : ")
        phonebook.append({'family':family,'name':name,'phone':phone})
        print("Saved")
    elif select==2:
        family=input("Enter family : ")
        name=input("Enter name : ")
        print("1-Equals")
        print("2-Contains")
        print("3-Starts with")
        print("4-Ends with")
        select=int(input("Select : "))
        for row in phonebook:
            if (select==1 and (row['family']==family and row['name']==name)) or (select==2 and (family in row['family'] and name in row['name'])) or (select==3 and (row['family'].startswith(family) and row['name'].startswith(name))) or (select==4 and (row['family'].endswith(family) and row['name'].endswith(name))):
                print(f"{row['family']}{''.join(' ' for i in range(25-len(row['family'])))}{row['name']}{''.join(' ' for i in range(25-len(row['name'])))}{row['phone']}")
    elif select==3:
        for row in phonebook:
            print(f"{row['family']}{''.join(' ' for i in range(25-len(row['family'])))}{row['name']}{''.join(' ' for i in range(25-len(row['name'])))}{row['phone']}")
    elif select==4:
        break