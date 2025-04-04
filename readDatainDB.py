import tkinter as tk
from tkinter import ttk
import sqlite3

def fetch_and_display_data():
    """Fetches all data from the customers table and displays it."""
    conn = sqlite3.connect("customerInfo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    data = cursor.fetchall()
    conn.close()

    # Clear previous data
    for row in data_tree.get_children():
        data_tree.delete(row)

    # Insert new data
    for row in data:
        data_tree.insert("", tk.END, values=row)

# Create the main window
root = tk.Tk()
root.title("Customer Data")

# Create a Treeview widget to display the data in a table format
columns = ("ID", "Name", "Birthday", "Email", "Phone", "Address", "Preferred Contact")
data_tree = ttk.Treeview(root, columns=columns, show="headings")

# Set column headings
for col in columns:
    data_tree.heading(col, text=col)
    data_tree.column(col, width=100, anchor="center")  # Adjust width as needed

# Configure scrollbars for the Treeview
scrollbar_y = ttk.Scrollbar(root, orient="vertical", command=data_tree.yview)
data_tree.configure(yscrollcommand=scrollbar_y.set)
scrollbar_y.pack(side="right", fill="y")
data_tree.pack(padx=10, pady=10, fill="both", expand=True)

# Fetch and display data when the script runs
fetch_and_display_data()

root.mainloop()