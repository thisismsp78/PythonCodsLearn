courses={'Python':60,'Java':50,'SQL':80}
#print(courses)
#print(courses['Python'])
#for key in courses:
#    print(key,courses[key])
print(courses)
#courses.update(Java=90)
#print(courses)
key=input("Enter new course title : ")
time=int(input("Enter new course time : "))
#courses.update(key=time)
#courses.update(C=70)
#courses.update([('C++',30)])
#courses.update([('C++',30),('C#',45)])
#new={'C++':30,'C#':45}
#courses.update(new)
courses.update([(key,time)])
print(courses)