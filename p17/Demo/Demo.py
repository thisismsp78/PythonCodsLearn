
import threading
import time


def operation(name):
    while True:
        print(name)


first=threading.Thread(target=operation,args=("a"))
first.start()
second=threading.Thread(target=operation,args=("b"))
second.start()