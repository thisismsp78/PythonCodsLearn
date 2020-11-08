import tkinter

def btnAdd_Clicked():
    list.insert(0,name.get())

form=tkinter.Tk()
tkinter.Label(text="New name : ").grid(row=0,column=0)
name=tkinter.StringVar()
tkinter.Entry(textvariable=name).grid(row=0,column=1)
tkinter.Button(text="Add",command=btnAdd_Clicked).grid(row=0,column=2)
list=tkinter.Listbox()
list.grid(row=2,column=0,columnspan=3,sticky="WE")

form.mainloop()
