file=open("C:\\Files\\Courses.txt","r")
for row in file:
    print(row.strip())
file.close()