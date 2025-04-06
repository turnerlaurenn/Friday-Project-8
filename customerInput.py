import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def create_table_if_not_exists():
    """Creates the 'customers' table in the database if it doesn't exist."""
    db_file = "customerInfo.db"
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
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
        conn.commit()
        print(f"Table 'customers' created or already exists in {db_file}")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")
    finally:
        if conn:
            conn.close()

def format_birthday(event):
    """Automatically adds dashes to the birthday field (YYYY-MM-DD) and limits length."""
    current_text = birthday_entry.get()
    new_text = ''.join(filter(str.isdigit, current_text))  # Keep only digits

    if len(new_text) > 8:
        new_text = new_text[:8]  # Limit to 8 digits

    formatted_text = ""
    for i, char in enumerate(new_text):
        formatted_text += char
        if i == 3 or i == 5:
            formatted_text += "-"

    birthday_entry.delete(0, tk.END)
    birthday_entry.insert(0, formatted_text)

def format_phone(event):
    """Automatically adds dashes to the phone number field (XXX-XXX-XXXX) and limits length."""
    current_text = phone_entry.get()
    cleaned_text = ''.join(filter(str.isdigit, current_text))  # Keep only digits

    if len(cleaned_text) > 10:
        cleaned_text = cleaned_text[:10]  # Limit to 10 digits

    formatted_text = ""
    for i, char in enumerate(cleaned_text):
        formatted_text += char
        if i == 2 or i == 5:
            formatted_text += "-"

    phone_entry.delete(0, tk.END)
    phone_entry.insert(0, formatted_text)

def submit_customer_info():
    """Submits the customer information to the database."""
    name = name_entry.get()
    birthday = birthday_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()
    street = street_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()
    address = f"{street}, {city}, {state} {zip_code}"
    preferred_contact = preferred_contact_var.get()

    if not all([name, len(birthday) == 10, is_valid_email(email), len(phone) == 12, street, city, state, zip_code, preferred_contact]):
        messagebox.showerror("Error", "Please fill in all fields correctly with the proper format (YYYY-MM-DD for Birthday, XXX-XXX-XXXX for Phone).")
        return

    conn = sqlite3.connect("customerInfo.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO customers (name, birthday, email, phone, address, preferred_contact)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (name, birthday, phone, email, address, preferred_contact))
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
    street_entry.delete(0, tk.END)
    city_entry.delete(0, tk.END)
    state_entry.delete(0, tk.END)
    zip_entry.delete(0, tk.END)
    preferred_contact_var.set(contact_methods[0])  # Reset to the first option

def is_valid_email(email):
    """Basic email validation."""
    return "@" in email and "." in email

def is_valid_phone(phone):
    """Basic phone number validation (allows digits and dashes)."""
    cleaned_phone = ''.join(filter(lambda x: x.isdigit() or x == '-', phone))
    parts = cleaned_phone.split('-')
    return len(parts) == 3 and all(len(part) in [3, 4] for part in parts)

# Create the main window
root = tk.Tk()
root.title("Customer Information Form")

# Create the table when the script starts
create_table_if_not_exists()

# --- Input Fields ---

# Name
name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

# Birthday
birthday_label = tk.Label(root, text="Birthday (YYYY-MM-DD):")
birthday_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
birthday_entry = tk.Entry(root, width=12)
birthday_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
birthday_entry.bind("<KeyRelease>", format_birthday)

# Email
email_label = tk.Label(root, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")

# Phone Number
phone_label = tk.Label(root, text="Phone Number (XXX-XXX-XXXX):")
phone_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
phone_entry = tk.Entry(root, width=15)
phone_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
phone_entry.bind("<KeyRelease>", format_phone)

# Address Breakdown
address_label = tk.Label(root, text="Address:")
address_label.grid(row=4, column=0, padx=5, pady=5, sticky="w", rowspan=4)

street_label = tk.Label(root, text="Street:")
street_label.grid(row=4, column=1, padx=5, pady=2, sticky="w")
street_entry = tk.Entry(root, width=30)
street_entry.grid(row=4, column=2, padx=5, pady=2, sticky="ew")

city_label = tk.Label(root, text="City:")
city_label.grid(row=5, column=1, padx=5, pady=2, sticky="w")
city_entry = tk.Entry(root, width=30)
city_entry.grid(row=5, column=2, padx=5, pady=2, sticky="ew")

state_label = tk.Label(root, text="State:")
state_label.grid(row=6, column=1, padx=5, pady=2, sticky="w")
state_entry = tk.Entry(root, width=5)
state_entry.grid(row=6, column=2, padx=5, pady=2, sticky="w")

zip_label = tk.Label(root, text="Zip Code:")
zip_label.grid(row=7, column=1, padx=5, pady=2, sticky="w")
zip_entry = tk.Entry(root, width=10)
zip_entry.grid(row=7, column=2, padx=5, pady=2, sticky="w")

# Preferred Contact Method
preferred_contact_label = tk.Label(root, text="Preferred Contact:")
preferred_contact_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
contact_methods = ["Email", "Phone Number", "Mail"]
preferred_contact_var = tk.StringVar(root)
preferred_contact_var.set(contact_methods[0])  # Set the default value
preferred_contact_dropdown = ttk.Combobox(root, textvariable=preferred_contact_var, values=contact_methods, width=27)
preferred_contact_dropdown.grid(row=8, column=1, columnspan=2, padx=5, pady=5, sticky="ew")

# --- Buttons ---
submit_button = tk.Button(root, text="Submit", command=submit_customer_info)
submit_button.grid(row=9, column=0, columnspan=3, padx=5, pady=10)

# Configure grid column weights to make the entry fields expand
root.grid_columnconfigure(2, weight=1)

root.mainloop()