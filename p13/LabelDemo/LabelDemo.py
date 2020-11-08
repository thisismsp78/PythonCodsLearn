import tkinter
import tkinter.messagebox

form=tkinter.Tk()

def btnShow_Clicked():
    tkinter.messagebox.showinfo("Name",f"Your name is {nameInput.get()}")

label=tkinter.Label(text="Name : ")
label.pack()
nameInput=tkinter.Entry()
nameInput.pack()
tkinter.Button(text="show",command=btnShow_Clicked).pack()

form.mainloop()
