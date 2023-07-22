import subprocess
import time
import os
import tkinter as tk
from tkinter import filedialog, messagebox
def main():
    def delete_files_in_directory(directory):
        try:
            start_time = time.time()
            command = f"find {directory} -type f -print0 | xargs -0 rm -f"
            subprocess.run(command, shell=True)
            end_time = time.time()
            elapsed_time = end_time - start_time
            messagebox.showinfo("Deletion Complete", f"Deletion completed in {elapsed_time:.2f} seconds.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete files: {e}")

    def browse_directory():
        directory_path = filedialog.askdirectory()
        if directory_path:
            entry_directory.delete(0, tk.END)
            entry_directory.insert(0, directory_path)

    def delete_files():
        directory_to_delete = entry_directory.get().strip()
        if not directory_to_delete:
            directory_to_delete = os.path.expanduser("~")
        delete_files_in_directory(directory_to_delete)

    window = tk.Tk()
    window.title("File Deletion")
    window.geometry("700x150")

    custom_font = ("Helvetica", 12)
    
    
    label_directory = tk.Label(window, text="Enter the directory path to delete files:",font = custom_font)
    entry_directory = tk.Entry(window, width=30)
    button_browse = tk.Button(window, text="Browse", command=browse_directory,font = custom_font)
    button_delete = tk.Button(window, text="Delete Files", command=delete_files,font = custom_font,bg="#3c8dbc",fg="white")

    label_directory.grid(row=0, column=0, padx=5, pady=5)
    entry_directory.grid(row=0, column=1, padx=5, pady=5)
    button_browse.grid(row=0, column=2, padx=5, pady=5)
    button_delete.grid(row=1, column=0, columnspan=3, padx=5, pady=10)

    window.mainloop()
