import tkinter
from PIL import Image,ImageTk

form=tkinter.Tk()
image=Image.open("copy.png")
photo=ImageTk.PhotoImage(image)
#label=tkinter.Label(image=photo)
#label.pack()
tkinter.Button(image=photo).pack()
form.mainloop()

