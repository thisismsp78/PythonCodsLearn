students=["student1","student2","student3"]
courses=["Python","C++","Java"]
resultList=[f"{student} - {course} : ----" for student in students for course in courses]
for row in resultList:
    print(row)
