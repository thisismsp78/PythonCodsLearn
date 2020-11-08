import sqlite3

connection=sqlite3.connect("database.db")
connection.execute("CREATE TABLE IF NOT EXISTS Product(ProductId INTEGER PRIMARY KEY AUTOINCREMENT,Name TEXT,Color TEXT)")
file=open("Products.txt","r")
for row in file:
    fields=row.strip().split(",")
    connection.execute("INSERT INTO Product(ProductId,Name,Color) VALUES(?,?,?)",fields)
    connection.commit()
file.close()
cursor=connection.cursor()
cursor.execute("SELECT * FROM Product")
for product in cursor:
    print(product[0],product[1],product[2])
cursor.close()
connection.close()
