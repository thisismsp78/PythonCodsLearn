
import json
import sqlite3
from fpdf import FPDF
 

"""
class Product:
    productId=0
    name=""
    color=""

file=open("products.json","r")
productsJSON=json.load(file)
file.close()
products=[]
for row in productsJSON:
    product=Product()
    product.__dict__.update(row)
    products.append(product)

connection=sqlite3.connect("database.db")
connection.execute("CREATE TABLE IF NOT EXISTS Product(ProductId INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Color TEXT)")
for product in products:
    connection.execute("INSERT INTO Product(ProductId,Name,Color) VALUES(?,?,?)",[product.productId,product.name,product.color])
connection.commit()
connection.close()
"""

connection=sqlite3.connect("database.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM Product")

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
line=1
for product in cursor:
    pdf.cell(w=100,h=10,txt=product[1],ln=line)
    line+=1
pdf.output("products.pdf")
cursor.close()
connection.close()