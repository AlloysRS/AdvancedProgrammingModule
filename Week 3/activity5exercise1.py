import tkinter as tk
from tkinter import ttk
import csv

# Load definitions from a CSV file if it exists
def load_definitions():
    definitions = {}
    try:
        with open("definitions.csv", "r") as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:
                    definitions[row[0].lower()] = row[1]
    except FileNotFoundError:
        pass
    return definitions

# Save all definitions to a CSV file
def save_definitions():
    with open("definitions.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for term, definition in computer_defs.items():
            writer.writerow([term, definition])

# Look up a term in the dictionary and show the definition
def get_definition():
    term = term_entry.get().strip().lower()
    output.delete("1.0", tk.END)
    if term in computer_defs:
        output.insert(tk.END, computer_defs[term])
    else:
        output.insert(tk.END, "Sorry, that term is not in the dictionary.")

# Add a new term and definition to the dictionary
def add_definition():
    term = new_term_entry.get().strip().lower()
    definition = new_definition_entry.get().strip()
    output.delete("1.0", tk.END)
    if term and definition:
        computer_defs[term] = definition
        output.insert(tk.END, f"Added '{term}' to the dictionary!")
    else:
        output.insert(tk.END, "Please enter both a term and a definition.")

# Remove a term from the dictionary
def remove_definition():
    term = term_entry.get().strip().lower()
    output.delete("1.0", tk.END)
    if term in computer_defs:
        del computer_defs[term]
        output.insert(tk.END, f"Removed '{term}' from the dictionary.")
    else:
        output.insert(tk.END, "Sorry, that term is not in the dictionary.")

# Show all terms and definitions in the output box
def show_all_definitions():
    output.delete("1.0", tk.END)
    if computer_defs:
        definitions_text = "\n".join(f"{term}: {definition}" for term, definition in computer_defs.items())
        output.insert(tk.END, definitions_text)
    else:
        output.insert(tk.END, "No definitions available.")

# Main function to set up the window and widgets
def main():
    global computer_defs, term_entry, new_term_entry, new_definition_entry, output

    # Load initial definitions from file
    computer_defs = load_definitions()

    # Set up the main window
    window = tk.Tk()
    window.title("Simple CS Dictionary")
    window.configure(background='black')

    # Instructions
    tk.Label(window, text="Enter a term:", bg='black', fg='white').grid(row=0, column=0, sticky='E')
    term_entry = tk.Entry(window, width=30)
    term_entry.grid(row=0, column=1)
    ttk.Button(window, text="Get Definition", command=get_definition).grid(row=0, column=2, sticky='W')

    # Display output for the definition with a scrollbar
    tk.Label(window, text="Definition:", bg='black', fg='white').grid(row=1, column=0, sticky='W')

    output_frame = tk.Frame(window)  # Frame to hold the text box and scrollbar
    output_frame.grid(row=2, column=0, columnspan=3, sticky='W')

    output = tk.Text(output_frame, width=50, height=6, wrap='word', bg='white')
    output.grid(row=0, column=0)

    # Adding scrollbar to the output text box
    scrollbar = tk.Scrollbar(output_frame, command=output.yview)
    scrollbar.grid(row=0, column=1, sticky='NS')
    output.config(yscrollcommand=scrollbar.set)

    # Section to add a new definition
    tk.Label(window, text="New Term:", bg='black', fg='white').grid(row=3, column=0, sticky='E')
    new_term_entry = tk.Entry(window, width=30)
    new_term_entry.grid(row=3, column=1)

    tk.Label(window, text="Definition:", bg='black', fg='white').grid(row=4, column=0, sticky='E')
    new_definition_entry = tk.Entry(window, width=50)
    new_definition_entry.grid(row=4, column=1, columnspan=2)

    ttk.Button(window, text="Add Definition", command=add_definition).grid(row=5, column=1, sticky='W')

    # Button to show all definitions
    ttk.Button(window, text="Show All Definitions", command=show_all_definitions).grid(row=6, column=1, sticky='W')

    # Button to remove a definition
    ttk.Button(window, text="Remove Definition", command=remove_definition).grid(row=0, column=3, sticky='W')

    # Automatically save definitions when the window is closed
    def on_close():
        save_definitions()  # Save all terms to the file before closing
        window.destroy()

    window.protocol("WM_DELETE_WINDOW", on_close)

    window.mainloop()

# Run the main function
if __name__ == "__main__":
    main()
