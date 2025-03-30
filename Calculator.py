from tkinter import *

app = Tk()
app.title("Simple Calculator")
app.config(background="#54AB80")
app.resizable(True, True)

def click(num):
    exp = entry_field.get()
    entry_field.delete(0, END)
    entry_field.insert(0, str(exp) + str(num))

def add_button():
    global expression, operation
    operation = "add"
    expression = int(entry_field.get())
    entry_field.delete(0, END)

def subtract_button():
    global expression, operation
    operation = "subtract"
    expression = int(entry_field.get())
    entry_field.delete(0, END)

def multiply_button():
    global expression, operation
    operation = "multiply"
    expression = int(entry_field.get())
    entry_field.delete(0, END)

def divide_button():
    global expression, operation
    operation = "divide"
    expression = int(entry_field.get())
    entry_field.delete(0, END)

def clear():
    entry_field.delete(0, END)

def equal_button():
    second_num = entry_field.get()
    entry_field.delete(0, END)
    if operation == "add":
        entry_field.insert(0, expression + int(second_num))
    elif operation == "subtract":
        entry_field.insert(0, expression - int(second_num))
    elif operation == "multiply":
        entry_field.insert(0, expression * int(second_num))
    elif operation == "divide":
        result = expression / int(second_num)
        entry_field.insert(0, int(result) if expression % int(second_num) == 0 else result)
    else:
        entry_field.insert(0, "error")

entry_field = Entry(app, width=35, justify="right", borderwidth=5)
entry_field.grid(row=0, column=0, columnspan=3, ipadx=10, pady=10)

buttons = [
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2),
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2),
    ("0", 4, 0), ("+", 4, 1, add_button),
    ("-", 4, 2, subtract_button), ("x", 5, 0, multiply_button),
    ("/", 6, 0, divide_button), ("=", 5, 1, equal_button, 2),
    ("clear", 6, 1, clear, 2)
]

for btn in buttons:
    text, row, col, *cmd = btn
    Button(app, text=text, height=1, width=7, padx=20, pady=10, 
           command=(cmd[0] if cmd else lambda t=text: click(t))).grid(row=row, column=col, 
                                                                      columnspan=(cmd[1] if len(cmd) > 1 else 1))

app.mainloop()
