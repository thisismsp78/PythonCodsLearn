import re

file=open("data.txt","r")
#print(file.read())
content=file.read()
file.close()
pattern=r"\d+"
matches=re.findall(pattern,content)
for match in matches:
    print(match)
    
print("------------------------")
pattern=r"http://www[.](\w{3,})[.]com"
matches=re.findall(pattern,content)
for match in matches:
    print(match)
print("------------------------")
pattern=r"http://www[.](\w{3,})[.](\w{2,4})"
matches=re.findall(pattern,content)
for match in matches:
    print(match)
print("------------------------")
for match in matches:
    print(match[0])
    print(match[1])
