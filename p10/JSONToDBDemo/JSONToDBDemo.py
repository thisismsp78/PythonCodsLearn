import sqlite3
import json

connection=sqlite3.connect("database.db")
connection.execute("CREATE TABLE IF NOT EXISTS Product(ProductId INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Color TEXT)")
file=open("Products.json","r")
products=json.load(file)
for product in products:
    connection.execute("INSERT INTO Product(ProductId,Name,Color) VALUES(?,?,?)",[product["productId"],product["name"],product["color"]])
    connection.commit()
file.close()
connection.close()

