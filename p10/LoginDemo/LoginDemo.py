import sqlite3

#connection=sqlite3.connect("database.db")
#connection.execute("CREATE TABLE IF NOT EXISTS User(UserId INTEGER PRIMARY KEY AUTOINCREMENT,Username TEXT,Password TEXT)")
#connection.execute("INSERT INTO User(Username,Password) VALUES('admin','0000')")
#connection.commit()
#connection.close()

username=input("Enter username : ")
password=input("Enter password : ")
connection=sqlite3.connect("database.db")
cursor=connection.cursor()
#cursor.execute("SELECT * FROM User WHERE Username=? AND Password=?",[username,password])
cursor.execute("SELECT COUNT(*) FROM User WHERE Username=? AND Password=?",[username,password])
rows=cursor.fetchall()
#print(rows[0][0])
#print(len(rows))
#if len(rows)==1:
#    print("Ok")
#else:
#    print("Invalid !")
if rows[0][0]==1:
    print("Ok")
else:
    print("Invalid !")
cursor.close()
connection.close()