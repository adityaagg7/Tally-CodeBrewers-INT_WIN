import os
import tkinter as tk
from tkinter import ttk


def delete_files_select(files):
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            # print(f"Deleted {file}")
        else:
            pass
            # print(f"{file} not found!")


def delete_files(indices, files):
    # indices=indices.spilt(',')
    for index in indices:
        if index.count('-') > 0:
            index1, index2 = map(int, index.split('-'))
            for i in range(index1, index2 + 1):
                if os.path.exists(files[i][0]):
                    os.remove(files[i][0])
                    # print("Deleted ", files[i][0], "\n")
                else:
                    pass
                    # print(f"File {files[i][0]} not found \n")
        else:
            if os.path.exists(files[int(index)][0]):
                os.remove(files[int(index)][0])
                # print("Deleted ", files[int(index)][0], "\n")
            else:
                pass
                # print(f"File {files[int(index)][0]} not found \n")


def delete_selected_files(table):
    # print(table.selection())
    items = table.selection()
    path = []
    for item in items:
        path.append(table.item(item)['values'][2])
        table.delete(item)
    delete_files_select(path)


def delete_all_files(table, files):
    # print("in delete all files")
    children = table.get_children("")
    for item in children:
        table.delete(item)
    delete_files([str(i) for i in range(len(files))], files)


def update_table(table, files):
    table.delete(*table.get_children())
    for i, (path, size) in enumerate(files):
        table.insert("", "end", values=(i, size, path))


def on_closing(window):
    window.quit()
    window.destroy()


def main(files):

    # print(files)
    window = tk.Tk()
    window.title("File Deletion Tool")
    window.geometry("800x500")
    # window.protocol("WM_DELETE_WINDOW", on_closing(window))

    table_frame = tk.Frame(window)
    table_frame.pack(pady=10)
    table = tk.ttk.Treeview(table_frame, columns=(
        "Index", "Size", "FilePath"), show="headings")
    table.heading("Index", text="Index")
    table.heading("Size", text="Size")
    table.heading("FilePath", text="FilePath")
    table.column("Index", width=60)
    table.column("Size", width=100)
    table.column("FilePath", width=640)
    table.pack()

    # print("updating table")
    update_table(table, files)

    label_info = tk.Label(
        window,
        text="Select the files you want to delete: ")

    button_delete_selected = tk.Button(window, text="Delete Selected Files",
                                       command=lambda: delete_selected_files(table))
    button_delete_all = tk.Button(
        window, text="Delete All Files", command=lambda: delete_all_files(table, files))
    # button_refresh = tk.Button(window, text="Refresh", command=update_table)
    button_quit = tk.Button(window, text="Quit",
                            command=lambda: on_closing(window))

    label_info.pack()
    # entry_indices.pack()
    # button_delete_indices.pack()
    button_delete_selected.pack(pady=5)
    button_delete_all.pack(pady=5)
    # button_refresh.pack(pady=5)
    button_quit.pack(pady=5)

    # Run the tkinter main loop
    window.mainloop()
    # print("henlo")
