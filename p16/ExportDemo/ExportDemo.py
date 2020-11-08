
import sqlite3
import json

class Product:
    productId=0
    name=""
    color=""

connection=sqlite3.connect("database.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM Product")
products=[]
for row in cursor:
    product=Product()
    product.productId=row[0]
    product.name=row[1]
    product.color=row[2]
    products.append(product.__dict__)
cursor.close()
connection.close()
file=open("products.json","w")
json.dump(products,file)
file.close()
