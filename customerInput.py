import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def submit_customer_info():
    """Submits the customer information to the database."""
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    address = address_entry.get("1.0", tk.END).strip()  # Get text from Text widget
    preferred_contact = preferred_contact_var.get()

    if not all([name, birthday, is_valid_email(email), is_valid_phone(phone), address, preferred_contact]):
        messagebox.showerror("Error", "Please fill in all fields correctly.")
        return

    conn = sqlite3.connect("customerInfo.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                birthday TEXT,
                email TEXT,
                phone TEXT,
                address TEXT,
                preferred_contact TEXT
            )
        """)
        cursor.execute("""
            INSERT INTO customers (name, birthday, email, phone, address, preferred_contact)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, birthday, email, phone, address, preferred_contact))
        conn.commit()
        messagebox.showinfo("Success", "Customer information submitted successfully!")
        clear_fields()
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()

def clear_fields():
    """Clears the input fields in the GUI."""
    name_entry.delete(0, tk.END)
    birthday_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    address_entry.delete("1.0", tk.END)
    preferred_contact_var.set(contact_methods[0])  # Reset to the first option

def is_valid_email(email):
    """Basic email validation."""
    return "@" in email and "." in email

def is_valid_phone(phone):
    """Basic phone number validation (allows digits, spaces, hyphens, parentheses)."""
    cleaned_phone = ''.join(filter(str.isdigit, phone))
    return len(cleaned_phone) >= 7  # Basic check for a reasonable length

# Create the main window
root = tk.Tk()
root.title("Customer Information Form")

# --- Input Fields ---

# Name
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Birthday
birthday_label = tk.Label(root, text="Birthday (YYYY-MM-DD):")
birthday_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
birthday_entry = tk.Entry(root, width=30)
birthday_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Phone Number
phone_label = tk.Label(root, text="Phone Number (e.g., 123-456-7890):")
phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")

# Address
address_label = tk.Label(root, text="Address:")
address_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
address_entry = tk.Text(root, width=25, height=3)
address_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")

# Preferred Contact Method
preferred_contact_label = tk.Label(root, text="Preferred Contact:")
preferred_contact_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")
contact_methods = ["Email", "Phone Number", "Mail"]
preferred_contact_var = tk.StringVar(root)
preferred_contact_var.set(contact_methods[0])  # Set the default value
preferred_contact_dropdown = ttk.Combobox(root, textvariable=preferred_contact_var, values=contact_methods, width=27)
preferred_contact_dropdown.grid(row=5, column=1, padx=5, pady=5, sticky="ew")

# --- Buttons ---

submit_button = tk.Button(root, text="Submit", command=submit_customer_info)
submit_button.grid(row=6, column=0, columnspan=2, padx=5, pady=10)

# Configure grid column weights to make the entry fields expand
root.grid_columnconfigure(1, weight=1)

root.mainloop()