import os
import hashlib
import tkinter as tk
from tkinter import filedialog, messagebox
def main():
    def get_file_hash(filename, block_size=65536):
        hasher = hashlib.sha256()
        with open(filename, "rb") as file:
            while True:
                data = file.read(block_size)
                if not data:
                    break
                hasher.update(data)
        return hasher.hexdigest()

    def find_duplicate_files(directory):
        file_hash_dict = {}
        duplicate_files = []

        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(root, filename)
                file_hash = get_file_hash(file_path)
                if file_hash in file_hash_dict:
                    duplicate_files.append(file_path)
                else:
                    file_hash_dict[file_hash] = file_path

        return duplicate_files

    def delete_files(file_list):
        for file_path in file_list:
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}: {e}")


    def browse_directory():
        directory_path = filedialog.askdirectory()
        if directory_path:
            entry_path.delete(0, tk.END)
            entry_path.insert(0, directory_path)

    def find_and_delete_duplicates():
        directory_to_scan = entry_path.get().strip()
        if not directory_to_scan:
            messagebox.showinfo("Error", "Please enter a directory path.")
            return

        if not os.path.exists(directory_to_scan) or not os.path.isdir(directory_to_scan):
            messagebox.showinfo("Error", "Invalid directory path. Please enter a valid directory.")
            return

        duplicate_files = find_duplicate_files(directory_to_scan)

        if not duplicate_files:
            messagebox.showinfo("Result", "No duplicate files found.")
        else:
            result_text = "Duplicate files found:\n" + "\n".join(duplicate_files)
            result_text += "\n\nDo you want to delete these files?"
            confirmation = messagebox.askyesno("Confirmation", result_text)
            if confirmation:
                delete_files(duplicate_files)
                messagebox.showinfo("Deletion Complete", "Duplicate files have been deleted.")

    # Create the main application window
    window = tk.Tk()
    window.title("Duplicate File Finder and Deleter")
    window.geometry("500x250")

    # Create the widgets
    label_intro = tk.Label(window, text="Use these paths as Reference: ")
    label_example = tk.Label(window, text="/home/Bob/Desktop/example.txt")
    label_path = tk.Label(window, text="Enter the directory path to scan for duplicates:")
    entry_path = tk.Entry(window, width=40)
    button_browse = tk.Button(window, text="Browse", command=browse_directory)
    button_find_delete = tk.Button(window, text="Find and Delete Duplicates", command=find_and_delete_duplicates)

    # Pack the widgets
    label_intro.pack()
    label_example.pack()
    label_path.pack()
    entry_path.pack(padx=10, pady=5, side=tk.LEFT)
    button_browse.pack(pady=5, side=tk.LEFT)
    button_find_delete.pack(pady=10)

    # Run the tkinter main loop
    window.mainloop()