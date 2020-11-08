import json

content="{'personId':1,'family':'ramezani','name':'shahram'}"
#content='{"personId":1,"family":"ramezani","name":"shahram"}'
data=json.loads(content)
print(data)