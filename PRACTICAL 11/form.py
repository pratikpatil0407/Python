import tkinter as tk

root = tk.Tk()
root.title("Validation Form")

def validate():
    name = NameE.get()
    email = emailE.get()
    phone = NoE.get()

    if not name:
        Status.config(text="Please enter your name.", fg="red")
        return

    if not email:
        Status.config(text="Please enter your email.", fg="red")
        return
    
    if not phone:
        Status.config(text="Please enter your phone number.", fg="red")
        return

    if not phone.isdigit() or len(phone) != 10:
        Status.config(text="Phone number must be 10 digits.", fg="red")
        return

    Status.config(text="Form Submitted Successfully!", fg="green")


Name = tk.Label(root, text="Name:")
Name.grid(row=0, column=0, padx=10, pady=10)
NameE = tk.Entry(root)
NameE.grid(row=0, column=1, padx=10, pady=10)

Email = tk.Label(root, text="Email:")
Email.grid(row=1, column=0, padx=10, pady=10)
emailE = tk.Entry(root)
emailE.grid(row=1, column=1, padx=10, pady=10)


Phone_No = tk.Label(root, text="Phone_No:")
Phone_No.grid(row=2, column=0, padx=10, pady=10)
NoE = tk.Entry(root)
NoE.grid(row=2, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit",command=validate)
submit_button.grid(row=3, column=0, columnspan=2, pady=20)

Status = tk.Label(root, text="", fg="black")
Status.grid(row=4, column=0, columnspan=2, pady=10)


root.mainloop()
