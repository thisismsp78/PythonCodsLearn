from Person import Person
from AgeException import *

try:
    age=int(input("Enter age : "))
    family=input("Enter family : ")
    name=input("Enter name : ")
    person=Person(age,family,name)
except AgeException as ex1:
    print(ex1)
except Exception as ex:
    print("Error !")