import json

file=open("Products.json","r")
products=json.load(file)
file.close()
file=open("Products.txt","w")
for product in products:
    file.write(f"{product['productId']},{product['name']},{product['color']}\n")    

file.close()
