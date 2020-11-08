from threading import *

class Resource:
    value=True
    def change(self):
        if self.value:
            print("Changed")
            self.value=False
            


resource=Resource()

first=Thread(target=resource.change)
second=Thread(target=resource.change)

first.start()
second.start()