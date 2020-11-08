class Student:
    family=""
    name=""
    courses=[]

    def __len__(self):
        return len(self.courses)



student=Student()
student.family="ramezani"
student.name="shahram"
student.courses=["C++","SQL","Python"]

print(len(student))

