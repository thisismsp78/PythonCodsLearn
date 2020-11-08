from threading import *
import time

def show(name):
    while True:
        print(name)
        time.sleep(1)


firstThread=Thread(target=show,args=("First",))
secondThread=Thread(target=show,args=("Second",))

firstThread.start()
secondThread.start()
