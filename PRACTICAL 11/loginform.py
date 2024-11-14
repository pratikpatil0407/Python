# import tkinter
# print("Tkinter is installed and ready to use.")

from tkinter import *

# def login():


# def clear():
    
 
top=Tk(className="Login Form")

l1=Label(top,text="Username",bg='lightpink').place(x=90,y=50)
n1=Entry(top).place(x=150,y=50)

l2=Label(top,text="Password",bg='lightpink').place(x=90,y=100)
n2=Entry(show='*').place(x=150,y=100)

b1=Button(top,text="Login").place(x=100,y=150)
b2=Button(top,text="Clear").place(x=150,y=150)

# l1.grid(row=0,column=0)
# n1.grid(row=0,column=1)
# l2.grid(row=1,column=0)
# n2.grid(row=1,column=1)
# b1.grid(row=2,column=1)

top.geometry("600x600")
top.configure(bg='lightpink')
top.mainloop()