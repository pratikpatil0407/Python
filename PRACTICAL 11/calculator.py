import tkinter as tk

def button_click(value):
    entry.insert(tk.END, value)

def button_clear():
    entry.delete(0, tk.END)

def button_equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Basic Calculator")

entry = tk.Entry(root, width=20, font=('Arial', 16), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('/', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=button_clear,bg="green")
    elif text == '=':
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=button_equal)
    else:
        button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: button_click(t))
    
    button.grid(row=row, column=col)

root.mainloop()