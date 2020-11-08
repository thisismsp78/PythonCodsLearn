import requests
import json
import subprocess

location=input("Enter location : ")
response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=53bb44b780354480e8d6b33e7efd6bbe")
jsonData=json.loads(response.text)
weather=jsonData["weather"][0]
main=weather["main"]
description=weather["description"]
icon=weather["icon"]
print(main,description,icon)
response=requests.get(f"http://openweathermap.org/img/wn/{icon}@2x.png")
file=open("C:\\Files\\photo.png","wb")
for byte in response:
    file.write(byte)

file.close()
subprocess.call("mspaint C:\\Files\\photo.png",shell=True)