from threading import *

def first():
    while True:
        print("First")


def second():
    while True:
        print("Second")


firstThread=Thread(target=first)
secondThread=Thread(target=second)

firstThread.start()
secondThread.start()
