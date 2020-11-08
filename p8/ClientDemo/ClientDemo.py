import requests

response=requests.get("http://checkip.dyndns.com/")
content=response.text
#print(response.text)
print(content[76:len(content)-16])
