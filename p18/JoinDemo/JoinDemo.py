
from threading import *
import time
from random import randint

def operation(name):
    time.sleep(randint(1,5))
    print(name)


for i in range(10):
    firstThread=Thread(target=operation,args=("First",))
    secondThread=Thread(target=operation,args=("Second",))
    firstThread.start()
    secondThread.start()
    firstThread.join()
    secondThread.join()
    print("------------------")


