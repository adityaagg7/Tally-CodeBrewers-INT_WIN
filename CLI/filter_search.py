import os
import index_display_delete

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
    print(category_or_extensions, "STARTING")
    category_or_extensions = category_or_extensions.split(",")
    print(category_or_extensions)
    for category in category_or_extensions:
        # print(category)
        # print(extensions)
        category = category.strip()
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
    print(extensions)
    extensions = set(extensions)
    print(extensions)
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


def main():
    print("Find Files by Extensions and Size")
    extensions = input(
        "Enter the file extensions separated by commas (e.g. txt, jpg, etc.)\nor type out the category (e.g. images, videos, documents, audios, or compressed): ")
    directory = input("Enter the directory path to search: ")
    min_size = float(input("Enter the minimum file size: "))
    max_size = float(input("Enter the maximum file size: "))
    unit = input("Enter the unit of file size (B, KB, MB, GB, TB): ").upper()

    matched_files = find_files_by_extensions_and_size(
        directory, extensions, min_size, max_size, unit)

    if matched_files:
        matched_files.sort(key=lambda x: x[1])
        for i in range(0, len(matched_files)):
            matched_files[i][1] = get_size_formatted(matched_files[i][1])
        index_display_delete.main(matched_files)

    else:
        print("No files found matching the criteria.")


if __name__ == "__main__":
    main()
