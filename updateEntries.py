import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

class UpdateCustomerWindow:
    def __init__(self, master):
        self.master = master
        master.title("Update Customer Information")

        self.vars = {field: tk.StringVar() for field in ["customer_id", "name", "birthday", "email", "phone", "address", "preferred_contact"]}
        self.contact_methods = ["Email", "Phone Number", "Mail"]
        self.vars["preferred_contact"].set(self.contact_methods[0])

        # UI Elements
        tk.Label(master, text="Customer ID:").grid(row=0, column=0)
        self.id_entry = tk.Entry(master, textvariable=self.vars["customer_id"], width=10)
        self.id_entry.grid(row=0, column=1)
        tk.Button(master, text="Load Customer", command=self.load_customer_data).grid(row=0, column=2)

        for i, field in enumerate(["name", "birthday", "email", "phone", "address"]):
            tk.Label(master, text=f"{field.capitalize()}:").grid(row=i+1, column=0)
            tk.Entry(master, textvariable=self.vars[field], width=30).grid(row=i+1, column=1)

        tk.Label(master, text="Preferred Contact:").grid(row=6, column=0)
        ttk.Combobox(master, textvariable=self.vars["preferred_contact"], values=self.contact_methods, width=30).grid(row=6, column=1)

        tk.Button(master, text="Update Customer", command=self.update_customer_info).grid(row=7, column=0, columnspan=3)

    def load_customer_data(self):
        customer_id = self.vars["customer_id"].get()
        if not customer_id.isdigit():
            messagebox.showerror("Error", "Invalid Customer ID.")
            return

        conn = sqlite3.connect("customerInfo.db")
        cursor = conn.cursor()
        cursor.execute("SELECT name, birthday, email, phone, address, preferred_contact FROM customers WHERE id=?", (customer_id,))
        customer_data = cursor.fetchone()
        conn.close()

        if customer_data:
            self.vars["name"].set(customer_data[0])
            self.vars["birthday"].set(customer_data[1])
            self.vars["email"].set(customer_data[2])
            self.vars["phone"].set(customer_data[3])
            self.vars["address"].set(customer_data[4])  # Using the entire address
            self.vars["preferred_contact"].set(customer_data[5])
        else:
            messagebox.showerror("Error", f"Customer with ID {customer_id} not found.")

    def update_customer_info(self):
        fields = {key: var.get() for key, var in self.vars.items()}
        if not all(fields.values()):
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        conn = sqlite3.connect("customerInfo.db")
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE customers
            SET name=?, birthday=?, email=?, phone=?, address=?, preferred_contact=?
            WHERE id=?
        """, (
            fields["name"], fields["birthday"], fields["email"], fields["phone"],
            fields["address"], fields["preferred_contact"], fields["customer_id"]
        ))
        conn.commit()
        conn.close()

        messagebox.showinfo("Success", f"Customer with ID {fields['customer_id']} updated successfully!")

if __name__ == "__main__":
    root = tk.Tk()
    UpdateCustomerWindow(root)
    root.mainloop()
