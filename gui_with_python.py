import tkinter
from tkinter import * # Import all definitions from tkinter

win = Tk() # Create a top-level window

def pr():
    print("Hello World")
def pr2():
    print("What's Up?")

# GUI logic goes here
#How to add size and position to the window
win.geometry("400x400")
# win.minsize(width=400, height=400)
# win.maxsize(width=400, height=400)


#How to add a Button?

b = Button(win,text = "Button", command= pr, activebackground="red", activeforeground="blue", padx=50, pady=50)
b1 = Button(win,text = "Button2", command= pr2)

#To show a button, you need to pack it

b.place(x=100,y=100)
b1.grid(row=0,column=1)

win.mainloop() # Tells Tk to enter its event loop
