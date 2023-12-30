import tkinter as tk
from tkinter import messagebox

contacts = []


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contacts.append(contact)
        update_contact_list()
        clear_fields()
    else:
        messagebox.showwarning("Warning", "Please enter at least a name and phone number.")


def update_contact_list():
    contact_list.delete(0, tk.END)
    for contact in contacts:
        contact_list.insert(tk.END, contact["Name"] + " - " + contact["Phone"])


def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def search_contact():
    query = search_entry.get().lower()
    contact_list.delete(0, tk.END)
    for idx, contact in enumerate(contacts):
        if query in contact["Name"].lower() or query in contact["Phone"]:
            contact_list.insert(tk.END, contact["Name"] + " - " + contact["Phone"])
    if contact_list.size() > 0:
        contact_list.selection_set(0)



def view_contact():
    try:
        selected_contact_index = contact_list.curselection()[0]
        selected_contact = contacts[selected_contact_index]
        messagebox.showinfo(
            "Contact Details",
            f"Name: {selected_contact['Name']}\nPhone: {selected_contact['Phone']}\n"
            f"Email: {selected_contact['Email']}\nAddress: {selected_contact['Address']}"
        )
    except IndexError:
        pass


def update_contact():
    try:
        selected_contact_index = contact_list.curselection()[0]
        selected_contact = contacts[selected_contact_index]

        selected_contact["Name"] = name_entry.get()
        selected_contact["Phone"] = phone_entry.get()
        selected_contact["Email"] = email_entry.get()
        selected_contact["Address"] = address_entry.get()

        update_contact_list()
        clear_fields()
    except IndexError:
        pass


def delete_contact():
    try:
        selected_contact_index = contact_list.curselection()[0]
        contacts.pop(selected_contact_index)
        update_contact_list()
        clear_fields()
    except IndexError:
        pass

root = tk.Tk()
root.title("Contact Management")

name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root, width=40)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root, width=40)
phone_entry.pack()

email_label = tk.Label(root, text="Email:")
email_label.pack()
email_entry = tk.Entry(root, width=40)
email_entry.pack()

address_label = tk.Label(root, text="Address:")
address_label.pack()
address_entry = tk.Entry(root, width=40)
address_entry.pack()

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.pack()

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.pack()

view_button = tk.Button(root, text="View Contact", command=view_contact)
view_button.pack()

search_label = tk.Label(root, text="Search:")
search_label.pack()
search_entry = tk.Entry(root, width=40)
search_entry.pack()
search_button = tk.Button(root, text="Search", command=search_contact)
search_button.pack()

contact_list = tk.Listbox(root, height=10, width=50)
contact_list.pack()

root.mainloop()
