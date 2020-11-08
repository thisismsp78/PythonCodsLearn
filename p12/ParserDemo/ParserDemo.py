import json
import sqlite3
import xml.etree.ElementTree as ET
import requests

class Product:
    productId=0
    name=""
    color=""



content=requests.get("http://ramezani.info/products.xml").text
products=[]
productElements=ET.fromstring(content)
#print(productElements)
for i in range(0,len(productElements)):
    product=Product()
    product.productId=int(productElements[i][0].text)
    product.name=productElements[i][1].text
    product.color=productElements[i][2].text
    products.append(product)

file=open("products.csv","w")
for product in products:
    file.write(f"{product.productId},{product.name},{product.color}\n")

file.close()

connection=sqlite3.connect("database.db")
connection.execute("CREATE TABLE IF NOT EXISTS Product(ProductId INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Color TEXT)")
for product in products:
    connection.execute("INSERT INTO Product(ProductId,Name,Color) VALUES(?,?,?)",[product.productId,product.name,product.color])
    connection.commit()

connection.close()

productsJson=[]
for product in products:
    productsJson.append(product.__dict__)

file=open("products.json","w")
json.dump(productsJson,file)
file.close()