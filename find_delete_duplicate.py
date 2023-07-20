import os
import hashlib
from tqdm import tqdm


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
            if file_hash in file_hash_dict:
                duplicate_files.append(file_path)
            else:
                file_hash_dict[file_hash] = file_path

    return duplicate_files


def delete_files(file_list):
    for file_path in tqdm(file_list):
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")
    print("\nDeletion Complete \n ")


def main():
    # print("Use these paths as Reference ")
    # print("/home/Bob/Desktop/example.txt")

    while True:
        dup_files = input("Enter the directory path to scan for duplicate files: ")
        dup_files = os.path.normpath(dup_files)
        print(dup_files, "ASDF")
        if os.path.exists(dup_files) and os.path.isdir(dup_files):
            break
        print(f"Invalid directory: {dup_files}")
        print("Please make sure the directory path exists and is a valid directory.")

    directory_to_scan = dup_files

    duplicate_files = find_duplicate_files(directory_to_scan)

    if not duplicate_files:
        print("No duplicate files found.")
    else:
        print("Duplicate files found:")
        for duplicate_file in duplicate_files:
            print(duplicate_file, "\n")
        while 1:
            confirm_deletion = (
                input("Do you want to delete these files? (Yes/No): ").strip().lower()
            )
            if confirm_deletion == "yes":
                delete_files(duplicate_files)
                break
            elif confirm_deletion == "no":
                break
            else:
                print("Sorry, I did not get it? Lets try again!")

    return
