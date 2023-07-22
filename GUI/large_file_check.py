import os
import tkinter as tk
from tkinter import filedialog, messagebox
from run_command import run_command
from prettytable import PrettyTable
import index_display_delete
# entry_path=[]
list_2 = []
def get_size_formatted(size_bytes):
    size_kb = size_bytes / 1024
    if size_kb < 1024:
        return f"{size_kb:.2f}KB"
    size_mb = size_kb / 1024
    if size_mb < 1024:
        return f"{size_mb:.2f}MB"
    size_gb = size_mb / 1024
    return f"{size_gb:.2f}GB"


def convert_size(size, unit, convert_bytes_to_unit):
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 * 1024,
        'GB': 1024 * 1024 * 1024,
        'TB': 1024 * 1024 * 1024 * 1024
    }
    if convert_bytes_to_unit:
        return size / units[unit]
    else:
        return size * units[unit]


def get_large_files(entry_path):
    path = entry_path.get().strip()

    if path == "/":
        out = run_command(
            f"sudo find {path} -maxdepth 4 -type f -print0 | xargs -0 du -sh |  sort -hr  | head -n 10"
        )
        # print(out)
        return

    elif path == "":
        path = os.path.expanduser("~")
    elif path[len(path) - 1 != "/"]:
        path += "/*"

    else:
        path += "*"
    a = run_command(
        f"find {path} -type f -print0 | xargs -0 du -sh |  sort -hr  | head -n 10")
    if a:
        a = a.split("\n")
        # table = PrettyTable()
        # table.field_names = ["Size", "File Name"]
        
        total_size = 0
        for line in a:
            size = line.split("\t")[0]
            nam = line.split("\t")[1]
            print(line)
            print(size)
            list_2.append([nam, size])
            if size[-1] == "B":
                size = float(size[:-1])
            elif size[-1] == "K":
                size = convert_size(float(size[:-1]), "KB", False)
            elif size[-1] == "M":
                size = convert_size(float(size[:-1]), "MB", False)
            elif size[-1] == "G":
                size = convert_size(float(size[:-1]), "GB", False)
            total_size += int(size)
        # print("\nTotal size: ", total_size)")
        total_size = get_size_formatted(total_size)
        list_2.append(["Total size", total_size])
        # index_display_delete.main(list_2)
        # table.add_row([size, nam], divider=True)
        # print(table)
        index_display_delete.main(list_2)
# def delete_items(list_2):

def browse_directory(entry_path):
    # Function to browse and set the directory path using a file dialog
    directory_path = filedialog.askdirectory()
    if directory_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, directory_path)
        
def main():
    # Create the main application window
    window = tk.Tk()
    window.title("Large Files Finder")
    window.geometry("700x600")

    # Create the widgets
    label_path = tk.Label(window, text="Enter the directory path to search or browse:")
    entry_path = tk.Entry(window, width=40)
    button_browse = tk.Button(window, text="Browse", command=lambda: browse_directory(entry_path))
    button_find_large_files = tk.Button(window, text="Find Large Files", command=lambda: get_large_files(entry_path))
    # text_box = tk.Text(window, wrap=tk.WORD, width=80, height=15)  # Create the text box
    # button_delete = tk.Button(window, text="Delete Files", command=lambda: delete_items(list_2))

    # Pack the widgets
    label_path.pack(pady=10)
    entry_path.pack(pady=5)
    button_browse.pack(pady=5)
    button_find_large_files.pack(pady=10)
    # text_box.pack(pady=10)  # Pack the text box
    # button_delete.pack(pady=5)

    # Run the tkinter main loop
    window.mainloop()