
while True:
    file=open("YourProducts.txt","r")
    print("1-Equals")
    print("2-Contains")
    print("3-Starts with")
    print("4-Ends with")
    select=int(input("Select : "))
    name=input("Enter name to search : ")
    for row in file:
        if select==1 and row.strip()==name:
            print(row.strip())
        elif select==2 and name in row:
            print(row.strip())
        elif select==3 and row.startswith(name):
            print(row.strip())
        elif select==4 and row.strip().endswith(name):
            print(row.strip())
    file.close()
