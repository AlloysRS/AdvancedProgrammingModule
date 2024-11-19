import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def main():
    # Initialise main window
    root = tk.Tk()
    root.title("Digital Address Book")
    root.geometry("800x500")
    root.config(bg="lightgrey")

    # Sample data with additional details for each contact
    sample_data = [
        ("John", "Doe", "Math", "Eng", "Sci", "XXXXX1", "john.doe@uni.ac.uk", "No", "98%", "2 days"),
        ("Jane", "Smith", "Math", "Geo", "Bio", "XXXXX2", "jane.smith@uni.ac.uk", "Yes", "95%", "1 day")
    ]

    # Function to update the details section based on the selected contact
    def on_contact_selected(event):
        selected_item = contact_list.selection()
        if selected_item:
            item = contact_list.item(selected_item)
            values = item['values']
            for contact in sample_data:
                if contact[:5] == tuple(values):
                    details_labels["Name"].config(text=f"{contact[0]} {contact[1]}")
                    details_labels["ID"].config(text=contact[5])
                    details_labels["Email"].config(text=contact[6])
                    details_labels["Absent"].config(text=contact[7])
                    details_labels["Attendance"].config(text=contact[8])
                    details_labels["Sick"].config(text=contact[9])

    # Menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    edit_menu = tk.Menu(menu_bar, tearoff=0)
    view_menu = tk.Menu(menu_bar, tearoff=0)
    reports_menu = tk.Menu(menu_bar, tearoff=0)

    menu_bar.add_cascade(label="File", menu=file_menu)
    menu_bar.add_cascade(label="Edit", menu=edit_menu)
    menu_bar.add_cascade(label="View", menu=view_menu)
    menu_bar.add_cascade(label="Reports", menu=reports_menu)

    # Reports submenu
    reports_menu.add_command(label="Absent")
    reports_menu.add_command(label="Attendance")
    reports_menu.add_command(label="Class List")

    # Tabs (Students, Modules)
    notebook = ttk.Notebook(root)
    students_tab = ttk.Frame(notebook)
    modules_tab = ttk.Frame(notebook)
    notebook.add(students_tab, text="Students")
    notebook.add(modules_tab, text="Modules")
    notebook.pack(expand=True, fill="both")

    # Contact list on the left side
    contact_list_frame = ttk.Frame(students_tab)
    contact_list_frame.pack(side="left", fill="y", padx=10, pady=10)

    columns = ("Name", "Surname", "L1", "L2", "L3")
    contact_list = ttk.Treeview(contact_list_frame, columns=columns, show="headings", height=10)
    for col in columns:
        contact_list.heading(col, text=col)
        contact_list.column(col, width=80)
    contact_list.pack(expand=True, fill="both")

    # Insert sample data into the contact list
    for data in sample_data:
        contact_list.insert("", "end", values=data[:5])

    # Right side with details, image, and actions
    details_frame = ttk.Frame(students_tab, padding="10", relief="groove")
    details_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

    # Placeholder image area
    image_frame = tk.Frame(details_frame, width=198, height=100, relief="solid", bd=1)
    image_frame.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
    image_placeholder = tk.Label(image_frame, text="198 x 300", font=("Arial", 10))
    image_placeholder.place(relx=0.5, rely=0.5, anchor="center")

    # Contact details section
    details_label = ttk.Label(details_frame, text="Details", font=("Arial", 10, "bold"))
    details_label.grid(row=1, column=0, columnspan=2, sticky="w", pady=(10, 5))

    # Dynamic labels to display selected contact details
    details_labels = {
        "Name": ttk.Label(details_frame, text=""),
        "ID": ttk.Label(details_frame, text=""),
        "Email": ttk.Label(details_frame, text=""),
        "Absent": ttk.Label(details_frame, text=""),
        "Attendance": ttk.Label(details_frame, text=""),
        "Sick": ttk.Label(details_frame, text="")
    }

    # Define and position labels for each detail field
    fields = ["Name:", "ID:", "Email:", "Absent:", "Attendance:", "Sick:"]
    for i, field in enumerate(fields):
        ttk.Label(details_frame, text=field).grid(row=i+2, column=0, sticky="w")
        details_labels[field[:-1]].grid(row=i+2, column=1, sticky="w")

    # Actions section with buttons (Edit, Suspend, Delete)
    actions_frame = ttk.Frame(details_frame, padding="10", relief="groove")
    actions_frame.grid(row=8, column=0, columnspan=2, sticky="w", pady=10)

    def edit_contact():
        messagebox.showinfo("Edit Contact", "Edit functionality is not yet implemented.")

    def suspend_contact():
        messagebox.showinfo("Suspend Contact", "Suspend functionality is not yet implemented.")

    def delete_contact():
        popup = tk.Toplevel(root)
        popup.title("Title")
        popup.geometry("300x150")
        popup.transient(root)
        popup.grab_set()

        question_label = ttk.Label(popup, text="Are you sure?", font=("Arial", 10, "bold"))
        question_label.pack(pady=10, padx=10)

        description_label = ttk.Label(popup, text="This will delete the student's record, are you sure?")
        description_label.pack(padx=10)

        button_frame = ttk.Frame(popup)
        button_frame.pack(pady=10)

        cancel_button = ttk.Button(button_frame, text="Cancel", command=popup.destroy)
        ok_button = ttk.Button(button_frame, text="OK", command=lambda: confirm_delete(popup))

        cancel_button.grid(row=0, column=0, padx=5)
        ok_button.grid(row=0, column=1, padx=5)

    def confirm_delete(popup):
        popup.destroy()
        messagebox.showinfo("Deleted", "Delete functionality is not yet implemented.")

    edit_button = ttk.Button(actions_frame, text="Edit", command=edit_contact)
    suspend_button = ttk.Button(actions_frame, text="Suspend", command=suspend_contact)
    delete_button = ttk.Button(actions_frame, text="Delete", command=delete_contact)

    edit_button.grid(row=0, column=0, padx=5)
    suspend_button.grid(row=0, column=1, padx=5)
    delete_button.grid(row=0, column=2, padx=5)

    # Bind the selection event to the contact list to update details
    contact_list.bind("<<TreeviewSelect>>", on_contact_selected)

    # Run the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
