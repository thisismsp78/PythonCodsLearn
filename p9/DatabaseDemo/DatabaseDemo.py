import sqlite3

connection=sqlite3.connect("database.db")
connection.execute("CREATE TABLE IF NOT EXISTS Category(CategoryId INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT)")
connection.close()
