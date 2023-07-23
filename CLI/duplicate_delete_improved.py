import os
import hashlib
import filecmp
import index_display_delete

import readline

readline.set_completer_delims(' \t\n=')
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


def delete_files(file_list):
    for file_path in file_list[1:]:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")


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
                        print(file_path, " ", other_file_path)
                        if filecmp.cmp(file_path, other_file_path, shallow=False):
                            print("hello")
                            verified_group.append(other_file_path)
                        else:
                            print("bye")
                            verified_group.clear()
                            break

                if len(verified_group) > 1:
                    verified_duplicates.append(verified_group)

    return verified_duplicates


def main():

    readline.parse_and_bind("tab: complete")
    
    directory_to_scan = input("Enter the directory to scan: ").strip()

    duplicate_files = find_duplicate_files(directory_to_scan)

    verified_duplicates = verify_duplicates(duplicate_files)

    if not verified_duplicates:
        print("No duplicate files found.")
    else:
        print(f"{len(verified_duplicates)} Groups of Duplicate files found!")
        for i, file_list in enumerate(verified_duplicates, 1):
            list_to_send = []
            for file_path in file_list:
                list_to_send.append(
                    [file_path, get_size_formatted(os.path.getsize(file_path))])
            index_display_delete.main(list_to_send)


# if __name__ == "__main__":
#     main()
