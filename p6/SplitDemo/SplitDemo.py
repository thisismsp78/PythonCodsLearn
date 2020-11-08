file=open("Products.txt","r")
products=[]
for row in file:
    fields=row.strip().split(",")
    products.append({'productId':fields[0],'name':fields[1],'color':fields[2]})
file.close()
while True:
    name=input("Enter name : ")
    color=input("Enter color : ")
    for product in products:
        if name in product['name'] and color in product['color']:
            print(f"{product['productId']} | {product['name']} | {product['color']}")