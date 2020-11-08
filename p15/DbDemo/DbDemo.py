
from pony.orm import *
import subprocess

db=Database()

class Product(db.Entity):
    productId=PrimaryKey(int,auto=True)
    name=Required(str)
    color=Required(str)


db.bind(provider='sqlite',filename='database.db',create_db=True)
db.generate_mapping(create_tables=True)

while True:
    subprocess.call('cls',shell=True)
    print("1-New")
    print("2-Print")
    print("3-Edit")
    print("4-Delete")
    print("5-Exit")
    menu=int(input("Select : "))
    if menu==1:
        subprocess.call('cls',shell=True)
        name=input("Enter name : ")
        color=input("Enter color : ")
        with db_session:
            product=Product(name=name,color=color)
        print("Press enter to continue ...")
        input()
    elif menu==2:
        subprocess.call('cls',shell=True)
        with db_session:
            for product in Product.select():
                print(f"{product.productId}{''.join([' ' for i in range(5-len(str(product.productId)))])}|{product.name}{''.join([' ' for i in range(20-len(product.name))])}|{product.color}")
        print("Press enter to continue ...")
        input()
    elif menu==3:
        subprocess.call('cls',shell=True)
        productId=int(input("Enter productId : "))
        name=input("Enter new name : ")
        color=input("Enter new color : ")
        with db_session:
            product=select(product for product in Product if product.productId==productId).first()
            product.name=name
            product.color=color
        print("Press enter to continue ...")
        input()
    elif menu==4:
        subprocess.call('cls',shell=True)
        productId=int(input("Enter productId : "))
        with db_session:
            product=select(product for product in Product if product.productId==productId).first()
            product.delete()
        print("Press enter to continue ...")
        input()
    elif menu==5:
        break