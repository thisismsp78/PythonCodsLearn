class Person:
    family=""
    name=""

    def __lt__(self, value):
        if self.family==value.family:
            return self.name<value.name
        return self.family<value.family


first=Person()
second=Person()
first.family="family"
first.name="name3"
second.family="family"
second.name="name2"

print(first<second)
