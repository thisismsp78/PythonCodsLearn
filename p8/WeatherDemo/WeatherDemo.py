import requests
import json

name=input("Enter name : ")
response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={name}&appid=53bb44b780354480e8d6b33e7efd6bbe")
content=response.text
data=json.loads(content)
print(data["weather"][0]["main"])
print(data["weather"][0]["description"])
