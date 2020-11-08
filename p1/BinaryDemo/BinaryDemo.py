number=int(input("Enter number : "))
bin=""
while number>0:
    bin=f"{number%2}{bin}"
    number//=2
print(bin)
