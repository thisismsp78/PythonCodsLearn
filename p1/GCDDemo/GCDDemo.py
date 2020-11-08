first=int(input("Enter first number : "))
second=int(input("Enter second number : "))
while first%second!=0:
    remain=first%second
    #adade dovom biyad jaye adade aval
    first=second
    #baghimande biyad jaye adade dovom
    second=remain
print(second)
