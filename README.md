# Customer Information Management System

## Overview

This project is a GUI-based system for managing customer information. It allows users to input, view, update, and delete customer records stored in a local SQLite database (`customerInfo.db`). Additionally, a utility script is included to list the tables within the database. This project was developed as part of a coding class assignment that initially only required a customer input GUI and database storage. The additional features for reading, updating, deleting entries, and listing tables were implemented to enhance the functionality and provide a more comprehensive system.

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
    * _Note: SQLite may also create internal tables like `sqlite_sequence`._

2.  **`customerInput.py`**: This Python script provides a graphical user interface (GUI) built with Tkinter. Users can enter new customer information into various fields (Name, Birthday, Email, Phone Number, Street, City, State, Zip Code, Preferred Contact Method) and submit it.
    * **Formatting:** The script automatically adds dashes to the "Birthday" (YYYY-MM-DD) and "Phone Number" (XXX-XXX-XXXX) fields as the user types.
    * **Address Handling:** The address is broken down into separate input fields in the GUI but is combined into a single string (comma-separated) before being stored in the `address` column of the database.
    * **Validation:** Basic email and phone number format validation is performed before submission, and all primary fields are checked for completion.

3.  **`deleteEntry.py`**: This Python script provides a GUI that allows users to delete existing customer entries from the `customerInfo.db` database.
    * It fetches all customer names and IDs from the database and displays them in a list.
    * Users can select a customer from the list, and upon confirmation, their record will be permanently deleted from the database.

4.  **`readDatainDB.py`**: This Python script provides a GUI that displays all the current entries in the `customerInfo.db` database in a table format using Tkinter's `Treeview` widget.
    * It fetches all data from the `customers` table and presents it with column headers for each field.
    * Horizontal and vertical scrollbars are included to allow viewing of all data, even if it exceeds the window size.

5.  **`updateEntries.py`**: This Python script provides a GUI for updating existing customer information in the `customerInfo.db` database.
    * Users can enter a Customer ID to load the existing data for that customer into the form.
    * The script attempts to split the stored comma-separated address back into the individual Street, City, State, and Zip Code fields for easier editing.
    * Users can modify any of the fields and click "Update Customer" to save the changes to the database.
    * After a successful update, the input fields (except Customer ID) are cleared.

6.  **`readTablesinDB.py`**: This Python script is a utility that, when executed, connects to the `customerInfo.db` database and prints a list of all the tables found within it to the terminal. This is helpful for verifying the database structure.

## How to Run

1.  **Ensure Python is Installed:** Make sure you have Python 3 installed on your system.
2.  **Install Tkinter (if needed):** Tkinter is usually included with standard Python installations. If you encounter issues, you might need to install it separately (e.g., `sudo apt-get install python3-tk` on Debian/Ubuntu or `brew install python-tk` on macOS).
3.  **Place Files in the Same Directory:** Ensure all six files (`customerInfo.db`, `customerInput.py`, `deleteEntry.py`, `readDatainDB.py`, `updateEntries.py`, `readTablesinDB.py`) are located in the same directory on your computer.
4.  **Run the Scripts:** You can run each Python script individually from your terminal or within VS Code using the command `python filename.py` (e.g., `python customerInput.py`).

## Using the System

1.  **`customerInput.py`**: Run this script to open the customer information entry form. Fill in the details and click "Submit" to add a new customer to the database.
2.  **`readDatainDB.py`**: Run this script to view all the current customer entries in a table.
3.  **`updateEntries.py`**: Run this script to update existing customer information. Enter the Customer ID you want to modify and click "Load Customer". Edit the fields as needed and click "Update Customer".
4.  **`deleteEntry.py`**: Run this script to delete customer entries. Select a customer from the list and click "Delete Entry" after confirming.
5.  **`readTablesinDB.py`**: Run this script to see a list of tables in your `customerInfo.db` printed in the terminal.

## Suitability for VS Code (Python)

This project is well-suited for development and running within VS Code with the Python extension installed. VS Code provides excellent features for editing Python code, an integrated terminal for running scripts, and debugging tools.

## Additional Features (Beyond Initial Requirements)

The `deleteEntry.py`, `readDatainDB.py`, `update_customer.py`, and `print_database_tables.py` files were added beyond the initial coding  requirement of just a customer input GUI and database storage. This was done to create a more comprehensive and functional customer information management system, allowing for data retrieval, modification, and deletion, as well as inspection of the database structure.