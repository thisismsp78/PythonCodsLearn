import sqlite3
import hashlib

connection=sqlite3.connect("database.db")
"""
connection.execute("CREATE TABLE IF NOT EXISTS User(UserId INTEGER PRIMARY KEY AUTOINCREMENT,Username TEXT UNIQUE,Password BLOB)")
username="admin"
password=b"0000"
hash=hashlib.md5(password).digest()
connection.execute("INSERT INTO User(Username,Password) VALUES(?,?)",[username,hash])
connection.commit()
"""

username=input("Enter username : ")
password=input("Enter password : ").encode()
hash=hashlib.md5(password).digest()

cursor=connection.cursor()
cursor.execute("SELECT * FROM User WHERE Username=? AND Password=?",[username,hash])
if len(cursor.fetchall())>0:
    print("Ok")
else:
    print("Invalid usernaem or password !")

cursor.close()
connection.close()
