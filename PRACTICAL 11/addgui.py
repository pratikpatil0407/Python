from tkinter import *

def add():
    n11 = int(n1.get())
    n22 = int(n2.get())
    res = n11 + n22
    l3.config(text=res)

top = Tk(className="Arithmetic Operation")
l1 = Label(top, text="number1:")
n1 = Entry(top)
l2 = Label(top, text="number2:")
n2 = Entry(top)
b1 = Button(top, text="Add", command=add)
l3 = Label(top, text="Result:")

l1.grid(row=0, column=0)
n1.grid(row=0, column=1)
l2.grid(row=1, column=0)
n2.grid(row=1, column=1)
b1.grid(row=2, column=0)
l3.grid(row=2, column=1)

top.geometry("600x600")
top.mainloop()