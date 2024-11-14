from tkinter import *

top=Tk(className="Registration Form")

l1=Label(top,text="First Name",bg="lightpink")
n1=Entry(top)

l2=Label(top,text="Middle Name",bg="lightpink")
n2=Entry(top)

l3=Label(top,text="Last Name",bg="lightpink")
n3=Entry(top)

l4=Label(top,text="Roll No",bg="lightpink")
n4=Entry(top)

l5=Label(top,text="Phone No",bg="lightpink")
n5=Entry(top)

l5=Label(top,text="Email address",bg="lightpink")
n5=Entry(show='*')

l6=Label(top,text="Roll No",bg="lightpink")
n6=Entry(top)

b1=Button(top,text="Register")

l1.grid(row=0, column=0,sticky='e', padx=70, pady=10)
n1.grid(row=0, column=1,sticky='e', padx=70, pady=10)
l2.grid(row=1, column=0,sticky='e', padx=70, pady=10)
n2.grid(row=1, column=1,sticky='e', padx=70, pady=10)
l3.grid(row=2, column=0,sticky='e', padx=70, pady=10)
n3.grid(row=2, column=1,sticky='e', padx=70, pady=10)
l4.grid(row=3, column=0,sticky='e', padx=70, pady=10)
n4.grid(row=3, column=1,sticky='e', padx=70, pady=10)
l5.grid(row=4, column=0,sticky='e', padx=70, pady=10)
n5.grid(row=4, column=1,sticky='e', padx=70, pady=10)
l6.grid(row=5, column=0,sticky='e', padx=70, pady=10)
n6.grid(row=5, column=1,sticky='e', padx=70, pady=10)
# b1.grid(row=6, column=0,sticky='e', padx=70, pady=10)

top.geometry("500x500")
top.configure(bg="lightpink")
top.mainloop()