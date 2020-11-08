import json

class Product:
    productId=0
    name=""
    color=""

    def __repr__(self):
        return f"{self.productId} | {self.name} | {self.color}"


products=[]
file=open("Products.txt","r")
for row in file:
    product=Product()
    fields=row.strip().split(",")
    product.productId=int(fields[0])
    product.name=fields[1]
    product.color=fields[2]
    #products.append(product)
    products.append(product.__dict__)

file.close()

"""
for product in products:
    print(product)
"""

#print(json.dumps(products.__dict__))

#print(json.dumps(products))

file=open("Products.json","w")
json.dump(products,file)
file.close()