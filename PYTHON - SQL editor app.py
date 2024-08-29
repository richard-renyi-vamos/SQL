import tkinter as tk
from tkinter import messagebox, scrolledtext
import sqlite3

# Initialize the main application window
root = tk.Tk()
root.title("Simple SQL Editor")
root.geometry("800x600")

# Create a function to execute SQL commands
def execute_sql():
    query = sql_input.get("1.0", tk.END)  # Get SQL input from the user
    try:
        # Connect to a database (or create it if it doesn't exist)
        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()
        cursor.execute(query)  # Execute the SQL query

        # If the query is a SELECT statement, fetch the results
        if query.strip().lower().startswith("select"):
            rows = cursor.fetchall()
            output = '\n'.join([str(row) for row in rows])
        else:
            conn.commit()  # Commit the transaction
            output = "Query executed successfully."

        conn.close()  # Close the connection
    except Exception as e:
        output = f"An error occurred: {e}"

    sql_output.delete("1.0", tk.END)  # Clear previous output
    sql_output.insert(tk.END, output)  # Insert new output

# Create input text box for SQL commands
sql_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=10)
sql_input.pack(pady=10)

# Create a button to run the SQL command
execute_button = tk.Button(root, text="Execute SQL", command=execute_sql)
execute_button.pack(pady=10)

# Create output text box for query results
sql_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=20)
sql_output.pack(pady=10)

# Start the main event loop
root.mainloop()
