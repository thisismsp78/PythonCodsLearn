def search(numbers,value):
    for number in numbers:
        if number==value:
            return True
    return False

numbers=[2,4,6]
while True:
    value=int(input("Enter number : "))
    print(search(numbers,value))
