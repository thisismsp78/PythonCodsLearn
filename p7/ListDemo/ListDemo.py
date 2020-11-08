class Person:
    family=""
    name=""

    def __repr__(self):
        return f"{self.family}-{self.name}"

    def __eq__(self, value):
        return self.family==value.family and self.name==value.name

    def __lt__(self, value):        
        if self.family==value.family:
            return self.name<value.name
        return self.family<value.family
        #return self.__gt__(value)

    #def __gt__(self, value):
    #    if self.family==value.family:
    #        return self.name>value.name
    #    return self.family>value.family        

people=[]
while True:
    print("1-New")
    print("2-Print")
    print("3-Remove")
    print("4-Sort")
    print("5-Exit")
    select=int(input("Select : "))
    if select==1:
        person=Person()
        person.family=input("Enter family : ")
        person.name=input("Enter name : ")
        people.append(person)
    elif select==2:
        print(people)
        for person in people:
            print(person)
    elif select==3:
        person=Person()
        person.family=input("Enter family : ")
        person.name=input("Enter name : ")
        people.remove(person)
    elif select==4:
        people.sort()
        print(people)
        for person in people:
            print(person)
        print("-----------")
        people.sort(reverse=True)
        print(people)
        for person in people:
            print(person)
    else:
        break