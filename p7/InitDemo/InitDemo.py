class Person:
    family=""
    name=""

    def __repr__(self):
        return f"{self.family}-{self.name}"

    def __init__(self,family="",name=""):
        self.family=family
        self.name=name

    #def __init__(self):
    #    self.family=""
    #    self.name=""

people=[Person("ramezani","shahram"),Person("family1","name1"),Person("family2","name2")]
print(people)
for person in people:
    print(person)

person=Person()
print(person)