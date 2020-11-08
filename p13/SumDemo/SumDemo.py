import tkinter
import tkinter.messagebox

form=tkinter.Tk()

def btnSum_Clicked():
    first=int(firstInput.get())
    second=int(secondInput.get())
    #tkinter.messagebox.showinfo("Sum",str(first+second))
    #resultLabel["text"]=str(first+second)
    resultLabel["text"]=f"{first}+{second}={first+second}"
    firstInput.delete(0,len(firstInput.get()))
    secondInput.delete(0,len(secondInput.get()))

tkinter.Label(text="First number : ").pack()
firstInput=tkinter.Entry()
firstInput.pack()
tkinter.Label(text="Second number : ").pack()
secondInput=tkinter.Entry()
secondInput.pack()
tkinter.Button(text="+",command=btnSum_Clicked).pack()
resultLabel=tkinter.Label()
resultLabel.pack()



form.mainloop()
