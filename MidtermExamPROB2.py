import tkinter as tk

def show_full_name():
    full_name = f"{first_name_entry.get()} {middle_name_entry.get()} {last_name_entry.get()}"
    full_name_entry.delete(0, tk.END)
    full_name_entry.insert(0, full_name)

root = tk.Tk()
root.title("Midterm Exam Problem 2")
root.geometry("600x420")  # Set the size of the window


# Set the font for the labels and entry widgets
font = ("Arial", 10)

# Create Labels
tk.Label(root, text="Enter Given Name:", font=font).grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Enter Middle Name:", font=font).grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Enter Last Name:", font=font).grid(row=2, column=0, padx=10, pady=10)
tk.Label(root, text="My Full Name is:", font=font).grid(row=3, column=0, padx=10, pady=10)

# Create Entry Widgets
first_name_entry = tk.Entry(root, font=font)
middle_name_entry = tk.Entry(root, font=font)
last_name_entry = tk.Entry(root, font=font)
full_name_entry = tk.Entry(root, font=font)

# Position Entry Widgets
first_name_entry.grid(row=0, column=1, padx=10, pady=10)
middle_name_entry.grid(row=1, column=1, padx=10, pady=10)
last_name_entry.grid(row=2, column=1, padx=10, pady=10)
full_name_entry.grid(row=3, column=1, padx=10, pady=10)

# Create Button
tk.Button(root, text="Show Full Name", font=font, command=show_full_name).grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
