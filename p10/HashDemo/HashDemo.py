import hashlib

#password=b"0000"
password=input("Enter password : ").encode()
hash=hashlib.md5(password)
#print(hash.digest())
if hashlib.md5(b"0000").digest()==hash.digest():
    print("Ok")
else:
    print("Invalid !")