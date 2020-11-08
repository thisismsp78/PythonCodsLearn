import hashlib
import sqlite3

connection=sqlite3.connect("database.db")
connection.execute("CREATE TABLE IF NOT EXISTS User(UserId INTEGER PRIMARY KEY AUTOINCREMENT,Username TEXT,Password BLOB)")
username=input("Enter username : ")
password=input("Enter password : ").encode()
connection.execute("INSERT INTO User(Username,Password) VALUES(?,?)",[username,hashlib.md5(password).digest()])
connection.commit()
connection.close()

