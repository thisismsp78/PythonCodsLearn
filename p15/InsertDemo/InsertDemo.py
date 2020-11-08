


from pony.orm import *


db=Database()

class Person(db.Entity):
    personId=PrimaryKey(int,auto=True)
    family=Required(str)
    name=Required(str)

db.bind(provider='sqlite',filename='database.db',create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    person=Person(family="ramezani",name="shahram")