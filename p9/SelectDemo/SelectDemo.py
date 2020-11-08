import sqlite3

connection=sqlite3.connect("database.db")
connection.execute("CREATE TABLE IF NOT EXISTS Category(CategoryId INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT)")
connection.close()
while True:
    print("1-New")
    print("2-Print")
    print("3-Delete")
    print("4-Update")
    print("5-Search")
    print("6-Exit")
    select=int(input("Select : "))
    if select==1:  
        name=input("Enter name : ")
        connection=sqlite3.connect("database.db")                
        connection.execute(f"INSERT INTO Category(Name) VALUES(?)",(name,))
        connection.commit()
        connection.close()
    elif select==2:
        connection=sqlite3.connect("database.db") 
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM Category")
        for category in cursor:
            print(category[0],category[1])
        cursor.close()
        connection.close()
    elif select==3:
        connection=sqlite3.connect("database.db") 
        categoryId=int(input("Enter categoryId : "))
        connection.execute("DELETE FROM Category WHERE CategoryId=?",(categoryId,))
        connection.commit()
        connection.close()
    elif select==4:
        connection=sqlite3.connect("database.db") 
        categoryId=int(input("Enter categoryId : "))
        name=input("Enter name : ")
        connection.execute("UPDATE Category SET Name=? WHERE CategoryId=?",(name,categoryId))
        connection.commit()
        connection.close()
    elif select==5:
        name=input("Enter name : ")
        name=f"%{name}%";
        connection=sqlite3.connect("database.db") 
        cursor=connection.cursor()
        cursor.execute("SELECT * FROM Category WHERE Name LIKE ?",(name,))
        for category in cursor:
            print(category[0],category[1])
        cursor.close()
        connection.close()
    else:
        break
