import filecmp
import hashlib
import os
import tkinter as tk
from tkinter import filedialog

import index_display_delete

result_list = []


def get_size_formatted(size_bytes):
    size_kb = size_bytes / 1024
    if size_kb < 1024:
        return f"{size_kb:.2f}KB"
    size_mb = size_kb / 1024
    if size_mb < 1024:
        return f"{size_mb:.2f}MB"
    size_gb = size_mb / 1024
    return f"{size_gb:.2f}GB"


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
            file_hash_dict.setdefault(file_hash, []).append(file_path)

    duplicate_files = [
        file_list for file_list in file_hash_dict.values() if len(file_list) > 1]
    return duplicate_files


def verify_duplicates(duplicate_files):
    verified_duplicates = []

    for file_list in duplicate_files:

        size_group = {}
        for file_path in file_list:
            size = os.path.getsize(file_path)
            size_group.setdefault(size, []).append(file_path)

        for group_files in size_group.values():
            if len(group_files) > 1:
                verified_group = []

                for file_path in group_files:
                    if verified_group:
                        break
                    verified_group.append(file_path)
                    for other_file_path in group_files:
                        if other_file_path == file_path:
                            continue
                        if filecmp.cmp(file_path, other_file_path):
                            verified_group.append(other_file_path)
                        else:

                            verified_group.clear()
                            break

                if len(verified_group) > 1:
                    verified_duplicates.append(verified_group)

    return verified_duplicates


def main():
    def browse_directory():
        directory_path = filedialog.askdirectory()
        if directory_path:
            entry_path.delete(0, tk.END)
            entry_path.insert(0, directory_path)

    def find_and_display_duplicates():
        directory_to_scan = entry_path.get().strip()

        duplicate_files = find_duplicate_files(directory_to_scan)
        verified_duplicates = verify_duplicates(duplicate_files)

        if not verified_duplicates:
            result_text.set("No duplicate files found.")
        else:
            result_text.set(f"{len(verified_duplicates)} Groups of Duplicate files found!")
            for i, file_list in enumerate(verified_duplicates, 1):
                group_files = []
                for file_path in file_list:
                    group_files.append([file_path, get_size_formatted(os.path.getsize(file_path))])
                result_list.append(group_files)

            # index_display_delete.main(result_list)

    def helper():
        print(result_list)
        for i in range(len(result_list)):
            index_display_delete.main(result_list[i])
            print("hello")

    window = tk.Tk()
    window.title("Duplicate File Finder")
    window.geometry("600x400")

    label_path = tk.Label(window, text="Enter the directory path to scan for duplicates:")
    entry_path = tk.Entry(window, width=40)
    button_browse = tk.Button(window, text="Browse", command=browse_directory)
    button_find_display_duplicates = tk.Button(window, text="Find and Display Duplicates",
                                               command=find_and_display_duplicates)
    result_text = tk.StringVar()
    button_delete = tk.Button(window, text="Delete", command=helper)
    result_label = tk.Label(window, textvariable=result_text)

    label_path.pack(pady=10)
    entry_path.pack(pady=5)
    button_browse.pack(pady=5)
    button_delete.pack(pady=5)
    button_find_display_duplicates.pack(pady=10)
    result_label.pack(pady=10)

    window.mainloop()


if __name__ == "__main__":
    main()
