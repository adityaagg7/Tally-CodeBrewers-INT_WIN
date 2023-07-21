import os
import subprocess
from tqdm import tqdm

image_set={"jpg","tif","tiff","eps", "jpeg", "png", "gif", "bmp", "raw", "cr2","nef","orf","sr2","webp","svg"}
video_set={"mp4", "avi", "mkv", "mov", "wmv"}
document_set={"pdf", "doc", "docx", "txt", "ppt", "pptx"}
audio_set={"mp3", "wav", "ogg", "flac", "aac"}
compressed_set={"zip", "rar", "tar", "gz", "7z"}
code_set={"py", "java", "cpp", "h", "html", "css", "js", "json"}



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

def get_total_size(directory, map):
    total_size=0
    cmd = f"find {directory} -type f -iname '*.*'"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    file_str = result.stdout.strip().split('\n')
    with tqdm(total=len(file_str), ascii=" #" ,desc=f"Searching: ", unit=" files") as pbar:
        for file in file_str:
            file_extension=file.split(".")[-1]
            try:
                file_size=os.path.getsize(file)
                if file_extension in image_set:
                    map["image_sizes"]+=file_size
                elif file_extension in video_set:
                    map["video_sizes"]+=file_size
                elif file_extension in document_set:
                    map["document_sizes"]+=file_size
                elif file_extension in audio_set:
                    map["audio_sizes"]+=file_size
                elif file_extension in compressed_set:
                    map["compressed_sizes"]+=file_size
                elif file_extension in code_set:
                    map["code_sizes"]+=file_size
                total_size+=file_size
            except:
                pass
            pbar.update(1)
    return total_size

def get_total_size_of_directory(directory):
    cmd="du -s "+directory
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    total_size_str = result.stdout.strip()
    total_size = total_size_str.split("\t")[0]
    return total_size

def main():
    map={"image_sizes":0,"video_sizes":0,"document_sizes":0,"audio_sizes":0,"compressed_sizes":0,"code_sizes":0}

    current_directory = input("Enter the directory you want to search in\n(leave blank for home directory)\n(enter . for searching current directory): ")
    if current_directory=="":
        current_directory='/home/manav/'
    if current_directory==".":
        current_directory=os.getcwd()

    total_extensions_size=get_total_size(current_directory, map)

    total_image_size = get_size_formatted(map["image_sizes"])
    total_video_size = get_size_formatted(map["video_sizes"])
    total_document_size = get_size_formatted(map["document_sizes"])
    total_audio_size = get_size_formatted(map["audio_sizes"])
    total_compressed_size = get_size_formatted(map["compressed_sizes"])
    total_code_size = get_size_formatted(map["code_sizes"])
    

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
