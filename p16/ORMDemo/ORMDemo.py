
from pony.orm import *

database=Database()

class Subcategory(database.Entity):
    subcategoryId=PrimaryKey(int,auto=True)
    name=Required(str)
    category=Required("Category")

class Category(database.Entity):
    categoryId=PrimaryKey(int,auto=True)
    name=Required(str)
    subcategories=Set("Subcategory")



database.bind(provider="sqlite",filename="database.db",create_db=True)
database.generate_mapping(create_tables=True)

"""
with db_session:
    category=Category(name="Hardware")
    subcategory=Subcategory(name="Case",category=category)
    subcategory=Subcategory(name="Monitor",category=category)
    subcategory=Subcategory(name="CPU",category=category)
"""

"""
with db_session:
    for category in Category.select():
        print(category.name)
        for subcategory in category.subcategories:
            print(f"\t{subcategory.name}")
"""

with db_session:
    for subcategory in Subcategory.select():
        print(f"{subcategory.name}{''.join(' ' for i in range(10-len(subcategory.name)))} | {subcategory.category.name}")