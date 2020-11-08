
import tkinter
import tkinter.messagebox

def testButton_Clicked():
    tkinter.messagebox.showinfo("title","message")

form=tkinter.Tk()
button=tkinter.Button(text="Test",command=testButton_Clicked)
button.pack()

form.mainloop()