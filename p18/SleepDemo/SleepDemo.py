from threading import *
import time

def first():
    while True:
        print("First")
        time.sleep(1)


def second():
    while True:
        print("Second")
        time.sleep(1)


firstThread=Thread(target=first)
secondThread=Thread(target=second)

firstThread.start()
secondThread.start()

