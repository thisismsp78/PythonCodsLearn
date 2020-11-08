def gcd(first,second):
    if first%second==0:
        return second
    return gcd(second,first%second)

print(gcd(32,24))
print(gcd(24,32))
