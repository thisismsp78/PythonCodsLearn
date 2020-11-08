
from pony.orm import *

database=Database()

class Person(database.Entity):
    personId=PrimaryKey(int,auto=True)
    family=Required(str)
    name=Required(str)

class Employee(Person):
    hiredate=Required(str)
    employeeId=Required(int)

class Student(Person):
    birthdate=Required(str)
    studentId=Required(int)


database.bind(provider="sqlite",filename="database.db",create_db=True)
database.generate_mapping(create_tables=True)

"""
with db_session:
    person=Person(family="person family 1",name="person name 1")

    employee=Employee(family="emp family 1",name="empl name 1",hiredate="1398/5/15",employeeId=1)

    student=Student(family="std family 1",name="stdl name 1",birthdate="1398/5/15",studentId=1)
"""


with db_session:
    print("Employee")
    print("----------------")
    for employee in Employee.select():
        print(employee.family,employee.name)

    print("Student")
    print("----------------")
    for student in Student.select():
        print(student.family,student.name)

    print("Person")
    print("----------------")
    for person in Person.select():
        print(person.family,person.name)
