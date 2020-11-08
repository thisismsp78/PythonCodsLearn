import hashlib

"""
username="admin"
password="0000"
row=f"{username}|{password}".encode()
hash=hashlib.md5(row).digest()
file=open("login.bin","wb")
file.write(hash)
file.close()
"""

username=input("Username : ")
password=input("Password : ")
row=f"{username}|{password}".encode()
hash=hashlib.md5(row).digest()
file=open("login.bin","rb")
current=file.read()
file.close()
if hash==current:
    print("Ok")
else:
    print("Invalid !")
