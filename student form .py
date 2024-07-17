import tkinter as tk
from tkinter import messagebox

# Function to handle the form submission
def submit_form():
    roll_no = roll_no_entry.get()
    name = name_entry.get()
    subjects = subjects_entry.get()
    address = address_entry.get()

    # Simple form validation
    if not roll_no or not name or not subjects or not address:
        messagebox.showwarning("Validation Error", "All fields are required!")
        return

    # Show submitted data (you can save this data to a file or database)
    messagebox.showinfo("Form Submitted", f"Roll No: {roll_no}\nName: {name}\nSubjects: {subjects}\nAddress: {address}")

    # Clear the form fields
    roll_no_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    subjects_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Student Admission Form")

# Create and place labels and entry widgets
tk.Label(root, text="Roll No").grid(row=0, column=0, padx=10, pady=5)
roll_no_entry = tk.Entry(root)
roll_no_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Subjects").grid(row=2, column=0, padx=10, pady=5)
subjects_entry = tk.Entry(root)
subjects_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Address").grid(row=3, column=0, padx=10, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=10, pady=5)

# Create and place the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)
submit_button.grid(row=4, columnspan=2, pady=10)

# Run the application
root.mainloop()