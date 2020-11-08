
import sqlite3
import json

connection=sqlite3.connect("database2.db")
connection.execute("CREATE TABLE IF NOT EXISTS Product(ProductId INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Color TEXT)")

class Product:
    productId=0
    name=""
    color=""
    def save(self):
        connection=sqlite3.connect("database2.db")
        #connection.execute("CREATE TABLE IF NOT EXISTS Product(ProductId INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Color TEXT)")
        connection.execute("INSERT INTO Product(ProductId,Name,Color) VALUES(?,?,?)",[self.productId,self.name,self.color])
        connection.commit()
        connection.close()

"""
file=open("product.json","r")
productJSON=json.load(file)
product=Product()
product.__dict__.update(productJSON)
product.save()
"""

file=open("products.json","r")
productsJSON=json.load(file)
for productJSON in productsJSON:
    product=Product()
    product.__dict__.update(productJSON)
    product.save()    