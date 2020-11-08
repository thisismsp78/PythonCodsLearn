import requests
import subprocess

response=requests.get("https://cdn.isna.ir/d/2019/07/28/2/57917006.jpg")
file=open("C:\\Files\\photo.jpg","wb")
for byte in response:
    file.write(byte)
file.close()
subprocess.call("mspaint C:\\Files\\photo.jpg",shell=True)
