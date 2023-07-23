import tkinter as tk
from tkinter import filedialog, messagebox
import os
import index_display_delete


def main():
    image_set = ["jpg", "tif", "tiff", "eps", "jpeg", "png", "gif",
                "bmp", "raw", "cr2", "nef", "orf", "sr2", "webp", "svg"]
    video_set = ["mp4", "avi", "mkv", "mov", "wmv"]
    document_set = ["pdf", "doc", "docx", "txt", "ppt", "pptx"]
    audio_set = ["mp3", "wav", "ogg", "flac", "aac"]
    compressed_set = ["zip", "rar", "tar", "gz", "7z"]
    code_set = ["py", "java", "cpp", "h", "html", "css", "js", "json", "md"]


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


    def find_files_by_extensions_and_size(directory, category_or_extensions, min_size, max_size, unit):
        matched_files = []
        extensions = []
        # print(category_or_extensions, "STARTING")
        category_or_extensions = category_or_extensions.split(",")
        # print(category_or_extensions)
        for category in category_or_extensions:
            # print(category)
            # print(extensions)
            category = category.strip().lower()
            if category == "images":
                extensions.extend(image_set)
            elif category == "videos":
                extensions.extend(video_set)
            elif category == "documents":
                extensions.extend(document_set)
            elif category == "audios":
                extensions.extend(audio_set)
            elif category == "compressed":
                extensions.extend(compressed_set)
            elif category == "code":
                extensions.extend(code_set)
            else:
                extensions.append(category)
        # print(extensions)
        extensions = set(extensions)
        # print(extensions)
        if unit != "B":
            min_size = convert_size(min_size, unit, False)
            max_size = convert_size(max_size, unit, False)
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                for extension in extensions:
                    if filename.endswith("." + extension.strip()):
                        file_path = os.path.join(root, filename)
                        file_size_bytes = os.path.getsize(file_path)
                        if min_size <= file_size_bytes <= max_size:
                            matched_files.append([file_path, file_size_bytes])
                        break
        # print(matched_files)
        return matched_files

    def browse_directory():
        directory_path = filedialog.askdirectory()
        if directory_path:
            entry_directory_path.delete(0, tk.END)
            entry_directory_path.insert(0, directory_path)

    def on_category_selected(event):
        selected_categories = category_listbox.curselection()
        extensions = []

        for index in selected_categories:
            category = categories[index]
            if category == "Images":
                extensions.extend(image_set)
            elif category == "Videos":
                extensions.extend(video_set)
            elif category == "Audio":
                extensions.extend(audio_set)
            elif category == "Code":
                extensions.extend(code_set)
            elif category == "Compressed":
                extensions.extend(compressed_set)
            elif category == "Documents":
                extensions.extend(document_set)

        manual_extensions = entry_extensions.get().strip().split(',')
        extensions.extend(manual_extensions)

        entry_extensions.delete(0, tk.END)
        entry_extensions.insert(0, ",".join(extensions))


    def on_search_button():
        extensions = entry_extensions.get().strip()
        directory = entry_directory_path.get().strip()
        min_size = float(entry_min_size.get())
        max_size = float(entry_max_size.get())
        unit = unit_var.get().upper()

        matched_files = find_files_by_extensions_and_size(
            directory, extensions, min_size, max_size, unit)

        if matched_files:
            matched_files.sort(key=lambda x: x[1])
            for i in range(len(matched_files)):
                matched_files[i][1] = get_size_formatted(matched_files[i][1])
            index_display_delete.main(matched_files)
        else:
            messagebox.showinfo("No Files Found", "No files found matching the criteria.")


    # Create the main tkinter window
    window = tk.Tk()
    window.title("Find Files by Extensions and Size")
    window.geometry("900x300")

    # Labels and Entry widgets for file extensions
    label_extensions = tk.Label(window, text="Enter file extensions (comma-separated):")
    entry_extensions = tk.Entry(window, width=40)

    # Labels and Entry widgets for other input fields
    label_directory_path = tk.Label(window, text="Enter the directory path to search:")
    entry_directory_path = tk.Entry(window, width=40)
    label_min_size = tk.Label(window, text="Enter the minimum file size:")
    entry_min_size = tk.Entry(window, width=10)
    label_max_size = tk.Label(window, text="Enter the maximum file size:")
    entry_max_size = tk.Entry(window, width=10)

    # Dropdown menu for file size unit
    units = ["B", "KB", "MB", "GB", "TB"]
    unit_var = tk.StringVar()
    unit_dropdown = tk.OptionMenu(window, unit_var, *units)
    unit_var.set("B")

    # Search button
    button_search = tk.Button(window, text="Search Files", command=on_search_button, font=("Helvetica", 12), bg="#3c8dbc",
                            fg="white", padx=5)
    button_browse = tk.Button(window, text="Browse", command=browse_directory, font=("Helvetica", 12), bg="#f0f0f0",
                            padx=5)

    button_browse.grid(row=1, column=2, padx=5, pady=5, sticky="w")

    categories = ["Images", "Videos", "Audio", "Code", "Compressed", "Documents"]
    category_listbox = tk.Listbox(window, selectmode=tk.MULTIPLE, height=len(categories), width=20, exportselection=False)
    for category in categories:
        category_listbox.insert(tk.END, category)
    category_listbox.grid(row=0, column=2, columnspan=2, padx=5, pady=5, sticky="w")
    category_listbox.bind('<<ListboxSelect>>', on_category_selected)


    # Grid layout for widgets
    label_extensions.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_extensions.grid(row=0, column=1, padx=5, pady=5, sticky="w")
    label_directory_path.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_directory_path.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    label_min_size.grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_min_size.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    label_max_size.grid(row=2, column=2, padx=5, pady=5, sticky="w")
    entry_max_size.grid(row=2, column=3, padx=5, pady=5, sticky="w")
    unit_dropdown.grid(row=2, column=4, columnspan=2, padx=5, pady=5, sticky="w")
    button_search.grid(row=3, column=1, columnspan=2, padx=5, pady=10)

    # Run the tkinter main loop
    window.mainloop()
