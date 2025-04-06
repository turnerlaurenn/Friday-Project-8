# print_database_tables.py
import sqlite3

def print_tables(database_name="customerInfo.db"):
    """Connects to the SQLite database and prints the names of all tables."""
    try:
        conn = sqlite3.connect(database_name)
        cursor = conn.cursor()

        # Get a list of all tables in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()

        if tables:
            print(f"Tables in the database '{database_name}':")
            for table in tables:
                print(f"- {table[0]}")
        else:
            print(f"The database '{database_name}' contains no tables.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print_tables()