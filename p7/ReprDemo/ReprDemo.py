class Person:
    family=""
    name=""

    def __repr__(self):
        return f"{self.family}-{self.name}"


people=[Person(),Person(),Person(),Person()]
print(people)
print(Person())
person=Person()
person.family="ramezani"
person.name="shahram"
print(person)