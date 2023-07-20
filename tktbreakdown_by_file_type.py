import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm

def get_size_formatted(size_bytes):
    # Function to convert bytes to a human-readable format (e.g., KB, MB, GB, etc.)
    size_kb = size_bytes / 1024
    if size_kb < 1024:
        return f"{size_kb:.2f}KB"
    size_mb = size_kb / 1024
    if size_mb < 1024:
        return f"{size_mb:.2f}MB"
    size_gb = size_mb / 1024
    return f"{size_gb:.2f}GB"

def get_total_size(directory, type, extensions):
    total_size_bytes = 0
    with tqdm(total=len(extensions), ascii=" #" ,desc=f"Searching {type}", unit="type") as pbar:
        for extension in extensions:
            cmd = f'find {directory} -type f -iname "*.{extension}" -exec stat -c %s {{}} +'
            result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
            file_sizes_str = result.stdout.strip()
            if file_sizes_str:
                file_sizes = map(int, file_sizes_str.split('\n'))
                total_size_bytes += sum(file_sizes)
            pbar.update(1)
    return total_size_bytes

def get_total_size_of_directory(directory):
    cmd = "du -s " + directory
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    total_size_str = result.stdout.strip()
    total_size = total_size_str.split("\t")[0]
    return total_size

def calculate_sizes():
    current_directory = entry_directory.get().strip()
    if not current_directory:
        current_directory = os.path.expanduser("~")

    image_extensions = ["jpg", "tif", "tiff", "eps", "jpeg", "png", "gif", "bmp", "raw", "cr2", "nef", "orf", "sr2", "webp", "svg"]
    video_extensions = ["mp4", "avi", "mkv", "mov", "wmv"]
    document_extensions = ["pdf", "doc", "docx", "txt", "ppt", "pptx"]
    audio_extensions = ["mp3", "wav", "ogg", "flac", "aac"]
    compressed_extensions = ["zip", "rar", "tar", "gz", "7z"]
    code_extensions = ["py", "java", "cpp", "h", "html", "css", "js"]

    extensions = image_extensions + video_extensions + document_extensions + audio_extensions + compressed_extensions + code_extensions
    total_image_size_bytes = get_total_size(current_directory, "images", image_extensions)
    total_video_size_bytes = get_total_size(current_directory, "videos", video_extensions)
    total_document_size_bytes = get_total_size(current_directory, "documents", document_extensions)
    total_audio_size_bytes = get_total_size(current_directory, "audio", audio_extensions)
    total_compressed_size_bytes = get_total_size(current_directory, "archives", compressed_extensions)
    total_code_size_bytes = get_total_size(current_directory, "programming files", code_extensions)
    total_image_size = get_size_formatted(total_image_size_bytes)
    total_video_size = get_size_formatted(total_video_size_bytes)
    total_document_size = get_size_formatted(total_document_size_bytes)
    total_audio_size = get_size_formatted(total_audio_size_bytes)
    total_compressed_size = get_size_formatted(total_compressed_size_bytes)
    total_code_size = get_size_formatted(total_code_size_bytes)
    total_extensions_size = (
        total_image_size_bytes + total_video_size_bytes +
        total_document_size_bytes + total_audio_size_bytes +
        total_compressed_size_bytes + total_code_size_bytes
    )
    total_directory_size = get_total_size_of_directory(current_directory)
    total_directory_size = int(total_directory_size) * 1024
    other_files_size = total_directory_size - total_extensions_size
    other_files_size = get_size_formatted(other_files_size)

    text_result.config(state=tk.NORMAL)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, f"Images: {total_image_size}\n")
    text_result.insert(tk.END, f"Videos: {total_video_size}\n")
    text_result.insert(tk.END, f"Documents: {total_document_size}\n")
    text_result.insert(tk.END, f"Audio Files: {total_audio_size}\n")
    text_result.insert(tk.END, f"Compressed Files: {total_compressed_size}\n")
    text_result.insert(tk.END, f"Code Files: {total_code_size}\n")
    text_result.insert(tk.END, f"Other Files: {other_files_size}\n")
    text_result.config(state=tk.DISABLED)

# Create the main application window
window = tk.Tk()
window.title("File Size Calculator")
window.geometry("675x675")  # Set width and height to the same value for a square window

# Create the widgets
label_directory = tk.Label(window, text="Enter the directory path to calculate file sizes:")
entry_directory = tk.Entry(window, width=30)
button_browse = tk.Button(window, text="Browse", command=lambda: entry_directory.insert(tk.END, filedialog.askdirectory()))
button_calculate = tk.Button(window, text="Calculate Sizes", command=calculate_sizes)
text_result = tk.Text(window, wrap=tk.WORD, state=tk.DISABLED)

# Pack the widgets using grid layout
label_directory.grid(row=0, column=0, padx=5, pady=5)
entry_directory.grid(row=0, column=1, padx=5, pady=5)
button_browse.grid(row=0, column=2, padx=5, pady=5)
button_calculate.grid(row=1, column=0, columnspan=3, padx=5, pady=10)
text_result.grid(row=2, column=0, columnspan=3, padx=5, pady=5)

# Run the tkinter main loop
window.mainloop()
