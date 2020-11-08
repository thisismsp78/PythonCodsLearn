def reverse1(name):
    if len(name)<2:
        return name
    return reverse1(name[1:])+name[0]

def reverse2(name):
    if len(name)<2:
        return name
    return name[len(name)-1]+reverse2(name[0:len(name)-1])

def reverse3(name):
    if len(name)<2:
        return name
    return name[len(name)-1]+reverse3(name[1:len(name)-1])+name[0]

def reverse4(name):
    result=""
    for index in range(1,len(name)+1):
        result+=name[-1*index]
    return result

#print(reverse1("sample"))
#print(reverse2("sample"))
#print(reverse3("sample"))
#print(reverse4("sample"))
data="".join([" " for x in range(3000000)])
#print(len(data))
reverse4(data)
print("Done")
