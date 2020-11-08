import tkinter
from PIL import Image,ImageTk
import requests
from io import *
import binascii
import urllib


form=tkinter.Tk()
image=Image.open(requests.get("http://172.20.87.25/red.png").text)
photo=ImageTK.PhotoImage(image)
tkinter.Label(image=photo).pack()
form.mainloop()
