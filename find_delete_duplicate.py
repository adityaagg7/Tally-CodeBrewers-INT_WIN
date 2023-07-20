import os
import hashlib


def get_file_hash(filename, block_size=65536):
    """
    Calculate the SHA-256 hash of a file.

    Parameters:
        filename (str): The path to the file.
        block_size (int): The size of blocks to read from the file for hashing.

    Returns:
        str: The hexadecimal representation of the file's SHA-256 hash.
    """
    hasher = hashlib.sha256()
    with open(filename, "rb") as file:
        while True:
            data = file.read(block_size)
            if not data:
                break
            hasher.update(data)
    return hasher.hexdigest()


def find_duplicate_files(directory):
    """
    Find duplicate files in a given directory and its subdirectories.

    Parameters:
        directory (str): The path to the directory to search.

    Returns:
        list: A list of paths to the duplicate files found.
    """
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
    """
    Delete the given list of files.

    Parameters:
        file_list (list): A list of file paths to delete.

    Note:
        This function will attempt to delete the files and print a message
        for each file indicating whether it was deleted successfully or not.
    """
    for file_path in file_list:
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

    # Directory to start the search from (e.g., user home directory)


def main():
    print("Use these paths as Reference ")
    print("/home/Bob/Desktop/example.txt")

    while True:
        dup_files = input("Enter the directory path to scan for duplicates: ").strip()
        dup_files = os.path.normpath(dup_files)
        if os.path.exists(dup_files) and os.path.isdir(dup_files):
            break
        print(f"Invalid directory: {dup_files}")
        print("Please make sure the directory path exists and is a valid directory.")

    directory_to_scan = dup_files  # Replace this with the actual directory path

    duplicate_files = find_duplicate_files(directory_to_scan)

    if not duplicate_files:
        print("No duplicate files found.")
    else:
        print("Duplicate files found:")
        for duplicate_file in duplicate_files:
            print(duplicate_file)

        confirm_deletion = (
            input("Do you want to delete these files? (yes/no): ").strip().lower()
        )
        if confirm_deletion == "yes":
            delete_files(duplicate_files)
    return
