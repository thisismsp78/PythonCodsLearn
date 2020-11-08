def factorial(number):
    if number==0:
        return 1
    return number*factorial(number-1)



#print(factorial(0))
#print(factorial(5))
#print(factorial(7))
#print(factorial(1000000))

while True:
    print(factorial(int(input("Enter number : "))))