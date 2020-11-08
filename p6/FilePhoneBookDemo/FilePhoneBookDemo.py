import subprocess

while True:
    subprocess.call("cls",shell=True)
    print("1-New")
    print("2-Search")
    print("3-Print")
    print("4-Exit")
    select=int(input("Select : "))
    if select==1:
        subprocess.call("cls",shell=True)
        family=input("Enter family : ")
        name=input("Enter name : ")
        phone=input("Enter phone : ")
        file=open("PhoneBook.txt","a")
        file.write(f"{family},{name},{phone}\n")
        file.close()
        print("Saved")
    elif select==2:
        subprocess.call("cls",shell=True)
        print("1-Equals")
        print("2-Contains")
        print("3-Starts with")
        print("4-Ends with")
        select=int(input("Select : "))
        family=input("Enter family : ")
        name=input("Enter name : ")        
        file=open("PhoneBook.txt","r")
        for row in file:
            fields=row.strip().split(",")
            view=False
            if select==1 and fields[0]==family and fields[1]==name:
                view=True
            elif select==2 and family in fields[0] and name in fields[1]:
                view=True
            elif select==3 and fields[0].startswith(family) and fields[1].startswith(name):
                view=True
            elif select==4 and fields[0].endswith(family) and fields[1].endswith(name):
                view=True
            if view:
                print(f"{fields[0]}{''.join(' ' for i in range(25-len(fields[0])))} | {fields[1]}{''.join(' ' for i in range(25-len(fields[1])))} | {fields[2]}")
        file.close()
        print("Press enter to continue...")
        input()
    elif select==3:
        subprocess.call("cls",shell=True)
        file=open("PhoneBook.txt","r")
        for row in file:
            fields=row.strip().split(",")
            print(f"{fields[0]}{''.join(' ' for i in range(25-len(fields[0])))} | {fields[1]}{''.join(' ' for i in range(25-len(fields[1])))} | {fields[2]}")
        file.close()
        print("Press enter to continue...")
        input()

    elif select==4:
        break