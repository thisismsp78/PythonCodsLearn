from random import randint

number=randint(0,100)
while True:
    value=int(input("Guess the number : "))
    if value>number:
        print("Smaller")
    elif value<number:
        print("Bigger")
    else:
        print("You win")
        break
