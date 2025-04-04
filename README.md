# Customer Information Management System

## Overview

This project is a simple GUI-based system for managing customer information. It allows users to input, view, update, and delete customer records stored in a local SQLite database (`customerInfo.db`).

## Files Included

This project consists of the following files:

1.  **`customerInfo.db`**: This is the SQLite database file where all customer information is stored. The database contains a table named `customers` with the following columns:
    * `id` (INTEGER PRIMARY KEY AUTOINCREMENT)
    * `name` (TEXT NOT NULL)
    * `birthday` (TEXT)
    * `email` (TEXT)
    * `phone` (TEXT)
    * `address` (TEXT) - Stores the full address as a comma-separated string (Street, City, State Zip).
    * `preferred_contact` (TEXT)

2.  **`customerInput.py`**: This Python script provides a graphical user interface (GUI) built with Tkinter. Users can enter new customer information into various fields (Name, Birthday, Email, Phone Number, Street, City, State, Zip Code, Preferred Contact Method) and submit it.
    * **Formatting:** The script automatically adds dashes to the "Birthday" (YYYY-MM-DD) and "Phone Number" (XXX-XXX-XXXX) fields as the user types.
    * **Address Handling:** The address is broken down into separate input fields in the GUI but is combined into a single string (comma-separated) before being stored in the `address` column of the database.
    * **Validation:** Basic email and phone number format validation is performed before submission.

3.  **`deleteEntry.py`**: This Python script provides a GUI that allows users to delete existing customer entries from the `customerInfo.db` database.
    * It fetches all customer names and IDs from the database and displays them in a list.
    * Users can select a customer from the list, and upon confirmation, their record will be permanently deleted from the database.

4.  **`readDatainDB.py`**: This Python script provides a GUI that displays all the current entries in the `customerInfo.db` database in a table format using Tkinter's `Treeview` widget.
    * It fetches all data from the `customers` table and presents it with column headers for each field.
    * Horizontal and vertical scrollbars are included to allow viewing of all data, even if it exceeds the window size.

5.  **`update_customer.py`**: This Python script provides a GUI for updating existing customer information in the `customerInfo.db` database.
    * Users can enter a Customer ID to load the existing data for that customer into the form.
    * The script attempts to split the stored comma-separated address back into the individual Street, City, State, and Zip Code fields for easier editing.
    * Users can modify any of the fields and click "Update Customer" to save the changes to the database.
    * Basic input validation is also included.

## How to Run

1.  **Ensure Python is Installed:** Make sure you have Python 3 installed on your system.
2.  **Install Tkinter (if needed):** Tkinter is usually included with standard Python installations. If you encounter issues, you might need to install it separately.
3.  **Place Files in the Same Directory:** Ensure all five files (`customerInfo.db`, `customerInput.py`, `deleteEntry.py`, `readDatainDB.py`, `update_customer.py`) are located in the same directory on your computer.
4.  **Run the Scripts:** You can run each Python script individually from your terminal or within VS Code using the command `python filename.py`.

## Using the System

1.  **`customerInput.py`**: Run this script to add new customer information.
2.  **`readDatainDB.py`**: Run this script to view all customer entries.
3.  **`update_customer.py`**: Run this script to modify existing customer information.
4.  **`deleteEntry.py`**: Run this script to remove customer entries.

## Suitability for VS Code (Python)

This project is well-suited for development and running within VS Code with the Python extension installed, offering features like code editing, an integrated terminal, and debugging capabilities.