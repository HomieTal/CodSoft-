from tkinter import *
from random import randint
from tkinter import messagebox

root = Tk()
root.title('Password Generator by Charles Lughas')
root.geometry('500x500')
root.configure(background="#190032")

def generate_pass():
    pass_entry.delete(0, END)
    pass_length = int(my_entry.get())
    the_password = "".join(chr(randint(33, 126)) for _ in range(pass_length))
    pass_entry.insert(0, the_password)

def copy_pass():
    root.clipboard_clear()
    root.clipboard_append(pass_entry.get())
    popup()

def popup():
    messagebox.showinfo("Copy Password", "Password is copied to clipboard")

label_frame = LabelFrame(root, text="How many characters?", font=("Helvetic", 20, "normal"))
label_frame.pack(pady=20)

my_entry = Entry(label_frame, font=("Helvetica", 25))
my_entry.pack(padx=20, pady=20)

output_label_frame = LabelFrame(root, text="Your Password!", font=("Helvetic", 20, "bold"))
output_label_frame.pack(pady=10)

pass_entry = Entry(output_label_frame, font=('Helvetica', 25), bd=0, bg="systemButtonFace")
pass_entry.pack(pady=20)

btn_frame = Frame(root, background="#190032")
btn_frame.pack(pady=20)

gen_btn = Button(btn_frame, fg="green", text="Generate Strong Password", command=generate_pass)
gen_btn.grid(column=0, row=0, padx=20)

clip_btn = Button(btn_frame, fg="red", text="Copy to Clipboard", command=copy_pass)
clip_btn.grid(column=1, row=0, padx=10)

root.mainloop()
