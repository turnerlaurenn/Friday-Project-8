import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3

def populate_list():
    """Populates the listbox with customer names and IDs."""
    customer_list.delete(0, tk.END)
    conn = sqlite3.connect("customerInfo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM customers")
    rows = cursor.fetchall()
    for row in rows:
        customer_list.insert(tk.END, f"{row[0]}: {row[1]}")
    conn.close()

def delete_customer():
    """Deletes the selected customer from the database."""
    selected_item = customer_list.curselection()
    if not selected_item:
        messagebox.showerror("Error", "Please select a customer to delete.")
        return

    selected_index = selected_item[0]
    selected_text = customer_list.get(selected_index)
    customer_id = selected_text.split(":")[0]

    confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete customer ID {customer_id}?")
    if confirm:
        conn = sqlite3.connect("customerInfo.db")
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM customers WHERE id=?", (customer_id,))
            conn.commit()

            # Vacuum the database to reclaim space
            cursor.execute("VACUUM")
            
            # Reset the auto-increment counter to the last highest ID
            cursor.execute("UPDATE sqlite_sequence SET seq = (SELECT MAX(id) FROM customers) WHERE name = 'customers'")
            conn.commit()

            messagebox.showinfo("Success", f"Customer ID {customer_id} deleted successfully.")
            populate_list()  # Refresh the list after deletion
        except sqlite3.Error as e:
            messagebox.showerror("Database Error", f"An error occurred: {e}")
            conn.rollback()
        finally:
            conn.close()

# Create the main window
root = tk.Tk()
root.title("Delete Customer")

# Customer List
customer_label = tk.Label(root, text="Select Customer to Delete:")
customer_label.pack(pady=5)
customer_list = tk.Listbox(root, width=50)
customer_list.pack(padx=10, pady=5)
populate_list()  # Initial population of the list

# Delete Button
delete_button = tk.Button(root, text="Delete Selected Customer", command=delete_customer)
delete_button.pack(pady=10)

root.mainloop()