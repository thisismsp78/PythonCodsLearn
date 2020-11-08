import tkinter
import requests
import json
from PIL import Image,ImageTk




def btnAdd_Clicked():
    location=name.get()
    jsonData=json.loads(requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid=53bb44b780354480e8d6b33e7efd6bbe").text)
    weather=jsonData["weather"][0]
    main=weather["main"]
    description=weather["description"]
    icon=weather["icon"]
    bytes=requests.get(f"http://openweathermap.org/img/wn/{icon}@2x.png")
    file=open("icon.png","wb")
    for byte in bytes:
        file.write(byte)
    file.close()
    list.insert(0,f"Description : {description}")
    list.insert(0,f"Main : {main}")
    image=Image.open("icon.png")
    photo=ImageTk.PhotoImage(image)
    label=tkinter.Label(image=photo)
    label.image=photo
    label.grid(row=3,column=0,columnspan=3)


form=tkinter.Tk()
tkinter.Label(text="New name : ").grid(row=0,column=0)
name=tkinter.StringVar()
tkinter.Entry(textvariable=name).grid(row=0,column=1)
tkinter.Button(text="Add",command=btnAdd_Clicked).grid(row=0,column=2)
list=tkinter.Listbox(height=2)
list.grid(row=2,column=0,columnspan=3,sticky="WE")

form.mainloop()

