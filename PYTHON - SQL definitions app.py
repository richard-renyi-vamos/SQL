import tkinter as tk
from tkinter import messagebox
import sqlparse

# Simple dictionary for SQL keyword definitions
sql_definitions = {
    "SELECT": "The SELECT statement is used to select data from a database.",
    "FROM": "The FROM clause is used to specify the table to query data from.",
    "WHERE": "The WHERE clause is used to filter records that meet a certain condition.",
    "JOIN": "JOIN is used to combine rows from two or more tables, based on a related column.",
    "INSERT": "The INSERT INTO statement is used to add new records to a table.",
    "UPDATE": "The UPDATE statement is used to modify existing records in a table.",
    "DELETE": "The DELETE statement is used to delete existing records from a table.",
    "CREATE": "The CREATE TABLE statement is used to create a new table in a database.",
    "DROP": "The DROP TABLE statement is used to delete a table from a database.",
    "ALTER": "The ALTER TABLE statement is used to modify the structure of an existing table.",
    "GROUP BY": "The GROUP BY statement groups rows that have the same values in specified columns.",
    "ORDER BY": "The ORDER BY statement is used to sort the result-set in ascending or descending order.",
    "LIMIT": "The LIMIT clause is used to specify the number of records to return.",
    "HAVING": "The HAVING clause was added to SQL because the WHERE keyword could not be used with aggregate functions.",
    # Add more definitions as needed
}

def get_sql_definitions(sql_code):
    # Parse the SQL code
    parsed = sqlparse.parse(sql_code)[0]
    tokens = [token.value.upper() for token in parsed.tokens if not token.is_whitespace]

    # Find and return definitions
    definitions = []
    for token in tokens:
        if token in sql_definitions:
            definitions.append(f"{token}: {sql_definitions[token]}")

    return definitions if definitions else ["No SQL keywords found or defined."]

def show_definitions():
    sql_code = entry.get("1.0", tk.END).strip()
    if not sql_code:
        messagebox.showinfo("Info", "Please enter SQL code to search for definitions.")
        return
    
    definitions = get_sql_definitions(sql_code)
    result_text.set("\n\n".join(definitions))

# Initialize the main window
app = tk.Tk()
app.title("SQL Code Definition Finder")
app.geometry("500x400")

# Add a label
label = tk.Label(app, text="Enter SQL Code:")
label.pack(pady=10)

# Add a text entry box
entry = tk.Text(app, height=5, width=50)
entry.pack(pady=10)

# Add a button to get definitions
button = tk.Button(app, text="Get Definitions", command=show_definitions)
button.pack(pady=10)

# Add a label to show the results
result_text = tk.StringVar()
result_label = tk.Label(app, textvariable=result_text, justify="left", wraplength=450)
result_label.pack(pady=10)

# Run the application
app.mainloop()
