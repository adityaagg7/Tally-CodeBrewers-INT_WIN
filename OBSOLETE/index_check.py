import os
import tkinter as tk
from tkinter import ttk,messagebox
from prettytable import PrettyTable

def delete_files(indices, files):
    for index in indices:
        if index.count('-') > 0:
            index1, index2 = map(int, index.split('-'))
            for i in range(index1, index2 + 1):
                if os.path.exists(files[i][0]):
                    os.remove(files[i][0])
                    print("Deleted ", files[i][0], "\n")
                else:
                    print(f"File {files[i][0]} not found \n")
        else:
            if os.path.exists(files[int(index)][0]):
                os.remove(files[int(index)][0])
                print("Deleted ", files[int(index)][0], "\n")
            else:
                print(f"File {files[int(index)][0]} not found \n")

def delete_selected_files():
    indices = entry_indices.get().split(',')
    delete_files(indices, files)

def delete_all_files():
    delete_files([str(i) for i in range(len(files))], files)

def update_table():
    table.delete(*table.get_children())
    for i, (path, size) in enumerate(files):
        table.insert("", "end", values=(i, size, path))

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

# Sample list of files
files = [("/home/suare/Desktop/hi/h2.txt", "10KB"), ("/home/suare/Desktop/hi/h3.txt", "20KB"), ("/home/suare/Desktop/hi/h4.txt", "15KB")]

# Create the main application window
window = tk.Tk()
window.title("File Deletion Tool")
window.geometry("700x500")
window.protocol("WM_DELETE_WINDOW", on_closing)

# Create the table to display the files
table_frame = tk.Frame(window)
table_frame.pack(pady=10)
table = tk.ttk.Treeview(table_frame, columns=("Index", "Size", "FilePath"), show="headings")
table.heading("Index", text="Index")
table.heading("Size", text="Size")
table.heading("FilePath", text="FilePath")
table.column("Index", width=60)
table.column("Size", width=100)
table.column("FilePath", width=300)
table.pack()

# Insert data into the table
update_table()

# Create the widgets
label_info = tk.Label(window, text="Enter the comma-separated indices or hyphen-separated range of the files to be deleted or leave empty to exit:")
entry_indices = tk.Entry(window, width=50)
button_delete_selected = tk.Button(window, text="Delete Selected Files", command=delete_selected_files)
button_delete_all = tk.Button(window, text="Delete All Files", command=delete_all_files)
button_refresh = tk.Button(window, text="Refresh", command=update_table)
button_quit = tk.Button(window, text="Quit", command=on_closing)

# Pack the widgets with proper formatting
label_info.pack()
entry_indices.pack()
button_delete_selected.pack(pady=5)
button_delete_all.pack(pady=5)
button_refresh.pack(pady=5)
button_quit.pack(pady=5)

# Run the tkinter main loop
window.mainloop()
