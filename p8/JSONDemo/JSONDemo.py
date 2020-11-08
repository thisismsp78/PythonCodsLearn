import json

names=["C++","Python","C#","SQL"]
print(json.dumps(names))

person={'personId':1,'family':'ramezani','name':'shahram'}
print(json.dumps(person))

numbers=(2,4,6)
print(json.dumps(numbers))