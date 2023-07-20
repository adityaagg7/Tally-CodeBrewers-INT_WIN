import os
import subprocess
import tkinter as tk
from tkinter import filedialog, messagebox

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

def browse_directory():
    directory_path = filedialog.askdirectory()
    if directory_path:
        entry_directory_path.delete(0, tk.END)
        entry_directory_path.insert(0, directory_path)

def search_files():
    file_type = entry_file_type.get().strip()
    directory_to_scan = entry_directory_path.get().strip()

    if not file_type or not directory_to_scan:
        messagebox.showinfo("Error", "Please enter both file type and directory path.")
        return

    if directory_to_scan == "/":
        directory_to_scan = "/ -maxdepth 3"
        command = f"sudo find {directory_to_scan} -type f \\( -name *.{file_type} \\) -print0 | xargs -0 du -sh | sort -rh"
    else:
        command = f"find {directory_to_scan} -type f \\( -name *.{file_type} \\) -print0 | xargs -0 du -sh | sort -rh"

    files_found = run_command(command=command)
    text_result.config(state=tk.NORMAL)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, files_found)
    text_result.config(state=tk.DISABLED)

def delete_all_files():
    file_type = entry_file_type.get().strip()
    directory_to_scan = entry_directory_path.get().strip()

    if not file_type or not directory_to_scan:
        messagebox.showinfo("Error", "Please enter both file type and directory path.")
        return

    if directory_to_scan == "/":
        directory_to_scan = "/ -maxdepth 3"
        command = f"sudo find {directory_to_scan} -type f \\( -name *.{file_type} \\) -print0 | xargs -0 rm -rf"
    else:
        command = f"find {directory_to_scan} -type f \\( -name *.{file_type} \\) -print0 | xargs -0 rm -rf"

    run_command(command=command)
    messagebox.showinfo("Deletion Complete", "All files have been deleted.")

def delete_specific_file():
    file_path = entry_specific_file.get().strip()

    if not file_path:
        messagebox.showinfo("Error", "Please enter the path of the file to delete.")
        return

    try:
        os.remove(file_path)
        messagebox.showinfo("Deletion Complete", "The file has been deleted.")
    except Exception as e:
        messagebox.showinfo("Error", f"Failed to delete the file: {e}")

# Create the main application window
window = tk.Tk()
window.title("File Search and Delete")
window.geometry("600x400")

# Create the widgets
label_file_type = tk.Label(window, text="Enter the file type you want to search for:")
entry_file_type = tk.Entry(window, width=20)
label_directory_path = tk.Label(
    window,
    text=(
        "Enter the directory path to scan\n(leave blank for home directory)\n"
        "(for root directory enter / (maxdepth will be 3))\n(for current directory just enter .):"
    ),
)
entry_directory_path = tk.Entry(window, width=40)
button_browse = tk.Button(window, text="Browse", command=browse_directory)
button_search = tk.Button(window, text="Search Files", command=search_files)
text_result = tk.Text(window, height=10, width=60, state=tk.DISABLED)
label_specific_file = tk.Label(window, text="Enter the path of the file to delete:")
entry_specific_file = tk.Entry(window, width=40)
button_delete_specific_file = tk.Button(window, text="Delete Specific File", command=delete_specific_file)
button_delete_all_files = tk.Button(window, text="Delete All Files", command=delete_all_files)

# Pack the widgets
label_file_type.pack()
entry_file_type.pack(pady=5)
label_directory_path.pack()
entry_directory_path.pack(pady=5, side=tk.LEFT)
button_browse.pack(pady=5, side=tk.LEFT)
button_search.pack(pady=10)
text_result.pack(pady=10)
label_specific_file.pack()
entry_specific_file.pack(pady=5, side=tk.LEFT)
button_delete_specific_file.pack(pady=5, side=tk.LEFT)
button_delete_all_files.pack(pady=5)

# Run the tkinter main loop
window.mainloop()
