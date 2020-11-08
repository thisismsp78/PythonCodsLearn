

from pony.orm import *


db=Database()


"""
class Person(db.Entity):
    personId=PrimaryKey(int)
    family=Required(str)
    name=Required(str)
"""

class Person(db.Entity):
    personId=PrimaryKey(int)
    family=Optional(str)
    name=Optional(str)


db.bind(provider='sqlite',filename='database.db',create_db=True)
db.generate_mapping(create_tables=True)