class Person:
    family=""
    name=""
    def __eq__(self, value):
        return self.family==value.family and self.name==value.name


first=Person()
second=Person()
first.family="family"
first.name="name"
second.family="family"
second.name="name"
print(first==second)
#print(first==first)
