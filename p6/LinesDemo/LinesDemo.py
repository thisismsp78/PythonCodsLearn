file=open("Names.txt","a")
while True:
    name=input("Enter name : ")
    if name=="exit":
        file.close()
        break
    file.write(f"{name}\n")
    file.flush()
