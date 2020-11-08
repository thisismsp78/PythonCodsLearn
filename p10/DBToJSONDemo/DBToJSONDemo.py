import sqlite3
import json

connection=sqlite3.connect("database.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM Product")
products=[]
for row in cursor:
    #print(dict(zip(["productId","name","color"],row)))
    products.append(dict(zip(["productId","name","color"],row)))
cursor.close()
connection.close()
file=open("Products.json","w")
json.dump(products,file)
file.close()