class Person:
    family=""
    name=""
    def __str__(self):
        return f"{self.family}-{self.name}"
    


person=Person()
person.family="ramezani"
person.name="shahram"
print(person)

people=[person]
print(people)