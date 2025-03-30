import sqlite3
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Contact Book")
root.geometry("500x600")
root.configure(bg="#2C3E50")

conn = sqlite3.connect("contacts.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    name TEXT,
    phone TEXT,
    email TEXT
)
""")
conn.commit()

def add_contact():
    name, phone, email = name_entry.get(), phone_entry.get(), email_entry.get()
    if name and phone:
        cursor.execute("INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)", (name, phone, email))
        conn.commit()
        show_contacts()
        clear_entries()
    else:
        messagebox.showwarning("Warning", "Name and Phone are required!")

def show_contacts():
    contact_list.delete(0, END)
    cursor.execute("SELECT * FROM contacts")
    for row in cursor.fetchall():
        contact_list.insert(END, f"{row[1]} - {row[2]} - {row[3]}")

def search_contact():
    query = search_entry.get()
    contact_list.delete(0, END)
    cursor.execute("SELECT * FROM contacts WHERE name LIKE ? OR phone LIKE ?", (f"%{query}%", f"%{query}%"))
    for row in cursor.fetchall():
        contact_list.insert(END, f"{row[1]} - {row[2]} - {row[3]}")

def update_contact():
    selected = contact_list.curselection()
    if selected:
        contact = contact_list.get(selected[0]).split(" - ")[0]
        new_name, new_phone, new_email = name_entry.get(), phone_entry.get(), email_entry.get()
        cursor.execute("UPDATE contacts SET name=?, phone=?, email=? WHERE name=?", (new_name, new_phone, new_email, contact))
        conn.commit()
        show_contacts()
    else:
        messagebox.showwarning("Warning", "Select a contact to update!")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        contact = contact_list.get(selected[0]).split(" - ")[0]
        cursor.execute("DELETE FROM contacts WHERE name = ?", (contact,))
        conn.commit()
        show_contacts()
    else:
        messagebox.showwarning("Warning", "Select a contact to delete!")

def clear_entries():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)

Label(root, text="Contact Book", font=("Arial", 20, "bold"), fg="white", bg="#2C3E50").pack(pady=10)

frame = Frame(root, bg="#34495E", padx=20, pady=10)
frame.pack(pady=10)

Label(frame, text="Name:", font=("Arial", 12), fg="white", bg="#34495E").grid(row=0, column=0, sticky=W)
name_entry = Entry(frame, width=30)
name_entry.grid(row=0, column=1, pady=5)
Label(frame, text="Phone:", font=("Arial", 12), fg="white", bg="#34495E").grid(row=1, column=0, sticky=W)
phone_entry = Entry(frame, width=30)
phone_entry.grid(row=1, column=1, pady=5)
Label(frame, text="Email:", font=("Arial", 12), fg="white", bg="#34495E").grid(row=2, column=0, sticky=W)
email_entry = Entry(frame, width=30)
email_entry.grid(row=2, column=1, pady=5)

button_frame = Frame(root, bg="#2C3E50")
button_frame.pack()
Button(button_frame, text="Add Contact", command=add_contact, bg="#27AE60", fg="white", width=15).grid(row=0, column=0, padx=5, pady=5)
Button(button_frame, text="Update Contact", command=update_contact, bg="#F39C12", fg="white", width=15).grid(row=0, column=1, padx=5, pady=5)
Button(button_frame, text="Delete Contact", command=delete_contact, bg="#C0392B", fg="white", width=15).grid(row=0, column=2, padx=5, pady=5)

Label(root, text="Search:", font=("Arial", 12), fg="white", bg="#2C3E50").pack()
search_entry = Entry(root, width=40)
search_entry.pack(pady=5)
Button(root, text="Search", command=search_contact, bg="#2980B9", fg="white", width=15).pack(pady=5)

contact_list = Listbox(root, width=50, height=15, bg="#ECF0F1", font=("Arial", 12))
contact_list.pack(pady=10)
show_contacts()

root.mainloop()
conn.close()
