from AgeException import *

class Person:
    age=0
    family=""
    name=""

    def __init__(self,age,family,name):
        if age<0:
            #raise Exception("Invalid age !")
            raise AgeException()
        else:
            self.age=age
            self.family=family
            self.name=name


