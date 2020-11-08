import sqlite3

connection=sqlite3.connect("database.db")
cursor=connection.cursor()
cursor.execute("SELECT * FROM Product")
file=open("Products.txt","w")
for product in cursor:
    file.write(f"{product[0]},{product[1]},{product[2]}\n")
file.close()
cursor.close()
connection.close()
