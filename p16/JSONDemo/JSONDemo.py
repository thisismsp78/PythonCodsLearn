
import json
from pony.orm import *

database=Database()

class Product(database.Entity):
    productId=PrimaryKey(int,auto=True)
    #name=Required(str)
    name=Optional(str)
    #color=Required(str)
    color=Optional(str)

database.bind(provider="sqlite",filename="database.db",create_db=True)
database.generate_mapping(create_tables=True)

file=open("product.json","r")
jsonProduct=json.load(file)
file.close()

with db_session:
    #product=Product(productId=jsonProduct["productId"],name=jsonProduct["name"],color=jsonProduct["color"])
    product=Product()    
    product.__dict__.update(jsonProduct)
    #print(product.productId)
    print(product.productId)