import tkinter

form=tkinter.Tk()
tkinter.Label(text="First : ").grid(row=0,column=0,sticky="W")
tkinter.Label(text="Second : ").grid(row=1,column=0)
tkinter.Entry().grid(row=0,column=1)
tkinter.Entry().grid(row=1,column=1)
tkinter.Button(text="+").grid(row=2,column=1,sticky="WE")
form.mainloop()
