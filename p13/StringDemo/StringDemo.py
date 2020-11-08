import tkinter
import tkinter.messagebox

form=tkinter.Tk()

def btnSum_Clicked():
    first=int(firstValue.get())
    second=int(secondValue.get())
    resultLabel["text"]=f"{first}+{second}={first+second}"
    firstValue.set("")
    secondValue.set("")

firstValue=tkinter.StringVar()
secondValue=tkinter.StringVar()
tkinter.Label(text="First number : ").pack()
firstInput=tkinter.Entry(textvariable=firstValue)
firstInput.pack()
tkinter.Label(text="Second number : ").pack()
secondInput=tkinter.Entry(textvariable=secondValue)
secondInput.pack()
tkinter.Button(text="+",command=btnSum_Clicked).pack()
resultLabel=tkinter.Label()
resultLabel.pack()



form.mainloop()

