import os
import subprocess
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
    cmd="du -s "+directory
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    total_size_str = result.stdout.strip()
    total_size = total_size_str.split("\t")[0]
    return total_size

def main():
    image_extensions = ["jpg","tif","tiff","eps", "jpeg", "png", "gif", "bmp", "raw", "cr2","nef","orf","sr2","webp","svg"]
    video_extensions = ["mp4", "avi", "mkv", "mov", "wmv"]
    document_extensions = ["pdf", "doc", "docx", "txt", "ppt", "pptx"]
    audio_extensions = ["mp3", "wav", "ogg", "flac", "aac"]
    compressed_extensions = ["zip", "rar", "tar", "gz", "7z"]
    code_extensions = ["py", "java", "cpp", "h", "html", "css", "js"]

    current_directory = input("Enter the directory you want to search in\n(leave blank for home directory)\n(enter . for searching current directory): ")
    if current_directory=="":
        current_directory='/home/manav/'

    extensions = image_extensions + video_extensions + document_extensions + audio_extensions + compressed_extensions + code_extensions
    total_image_size_bytes = get_total_size(current_directory, "images", image_extensions)
    total_video_size_bytes = get_total_size(current_directory, "videos", video_extensions)
    total_document_size_bytes = get_total_size(current_directory, "documents", document_extensions)
    total_audio_size_bytes = get_total_size(current_directory, "audio", audio_extensions)
    total_compressed_size_bytes = get_total_size(current_directory, "archives",  compressed_extensions)
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
    total_directory_size=int(total_directory_size)*1024
    other_files_size=total_directory_size-total_extensions_size
    other_files_size=get_size_formatted(other_files_size)
    print(f"images: {total_image_size}")
    print(f"videos: {total_video_size}")
    print(f"documents: {total_document_size}")
    print(f"audio files: {total_audio_size}")
    print(f"compressed files: {total_compressed_size}")
    print(f"code files: {total_code_size}")
    print(f"other files: {other_files_size}")

if __name__ == "__main__":
    main()
