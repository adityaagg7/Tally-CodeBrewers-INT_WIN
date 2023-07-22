import os
import tkinter as tk
from tkinter import filedialog

from run_command import run_command


def main(files):
    def get_large_files():
        path = entry_path.get().strip()
        if path == "/":
            out = run_command(
                f"sudo find {path} -maxdepth 4 -type f -print0 | xargs -0 du -sh | sort -rh | head -n 10"
            )
        elif not path:
            path = os.path.expanduser("~")
        elif path[-1] != "/":
            path += "/*"
        else:
            path += "*"
        out = run_command(
            f"sudo find {path} -type f -print0 | xargs -0 du -sh | sort -rh | head -n 10"
        )
        # text_output.config(state=tk.NORMAL)
        # text_output.delete("1.0", tk.END)
        # text_output.insert(tk.END, out)
        # text_output.config(state=tk.DISABLED)
        a = a.split("\n")

        list = []
        total_size = 0
        for line in a:
            size = line.split("\t")[0]
            nam = line.split("\t")[1]
            # print(line)
            # print(size)
            list.append([nam, size])
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
        list.append(["Total size", total_size])

    def browse_directory():
        directory_path = filedialog.askdirectory()
        if directory_path:
            entry_path.delete(0, tk.END)
            entry_path.insert(0, directory_path)

    window = tk.Tk()
    window.title("Largest Files Finder")
    window.geometry("600x400")

    custom_font = ("Helvetica", 12)

    label_path = tk.Label(window, text="Enter the path of the directory to search or press 'Browse' for Home:")
    entry_path = tk.Entry(window, width=50)
    button_browse = tk.Button(window, text="Browse", command=browse_directory)
    button_find_large_files = tk.Button(window, text="Find Largest Files", command=get_large_files, font=custom_font,
                                        bg="#3c8dbc", fg="white")
    text_output = tk.Text(window, wrap=tk.WORD, state=tk.DISABLED, height=15, width=70)

    label_path.grid(row=0, column=0, padx=5, pady=5, columnspan=2)
    entry_path.grid(row=1, column=0, padx=5, pady=5, columnspan=2)
    button_browse.grid(row=1, column=2, padx=5, pady=5)
    button_find_large_files.grid(row=2, column=0, columnspan=3, padx=5, pady=10)
    text_output.grid(row=3, column=0, columnspan=3, padx=5, pady=5)

    window.mainloop()
