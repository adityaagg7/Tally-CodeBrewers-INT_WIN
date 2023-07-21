import os
import hashlib
import filecmp

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

    duplicate_files = [file_list for file_list in file_hash_dict.values() if len(file_list) > 1]
    return duplicate_files

def delete_files(file_list):
    for file_path in file_list[1:]:  # Skip the first file (original file)
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

def verify_duplicates(duplicate_files):
    verified_duplicates = []

    for file_list in duplicate_files:
        # Create a dictionary to group files by size
        size_group = {}
        for file_path in file_list:
            size = os.path.getsize(file_path)
            size_group.setdefault(size, []).append(file_path)

        # For each size group, compare files byte-by-byte if there are more than one file
        for group_files in size_group.values():
            if len(group_files) > 1:
                verified_group = []
                # Compare files byte-by-byte
                for file_path in group_files:
                    if verified_group:
                        # If any file in the group is not a duplicate, skip the group
                        break
                    verified_group.append(file_path)
                    for other_file_path in group_files:
                        if other_file_path == file_path:
                            continue
                        if filecmp.cmp(file_path, other_file_path):
                            verified_group.append(other_file_path)
                        else:
                            # If any file is not a duplicate, skip the group
                            verified_group.clear()
                            break

                # If more than one file in the group, consider them verified duplicates
                if len(verified_group) > 1:
                    verified_duplicates.append(verified_group)

    return verified_duplicates

def main():
    # Same as before
    directory_to_scan = "C:/Users/DELL/OneDrive/Desktop/h1"

    duplicate_files = find_duplicate_files(directory_to_scan)

    verified_duplicates = verify_duplicates(duplicate_files)

    if not verified_duplicates:
        print("No duplicate files found.")
    else:
        print("Duplicate files found:")
        for i, file_list in enumerate(verified_duplicates, 1):
            print(f"Group {i}:")
            for file_path in file_list:
                print(file_path)

        confirm_deletion = input("Do you want to delete these files? (yes/no): ").strip().lower()
        if confirm_deletion == "yes":
            for file_list in verified_duplicates:
                delete_files(file_list)

# if __name__ == "__main__":
#     main()
