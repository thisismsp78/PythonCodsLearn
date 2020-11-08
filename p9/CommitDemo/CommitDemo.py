import sqlite3

connection=sqlite3.connect("database.db")
connection.execute("CREATE TABLE IF NOT EXISTS Category(CategoryId INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT)")
name=input("Enter name : ")
connection.execute(f"INSERT INTO Category(Name) VALUES('{name}')")
connection.commit()
connection.close()

