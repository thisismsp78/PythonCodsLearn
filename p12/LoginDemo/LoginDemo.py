import hashlib

username="admin"
password=hashlib.md5(b"0000").digest()
file=open("login.bin","wb")
file.write(username)
file.write(password)
file.close()
