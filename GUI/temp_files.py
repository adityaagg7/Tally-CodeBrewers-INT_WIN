import os
import subprocess
from prettytable import PrettyTable
from tqdm import tqdm


def get_size_formatted(size_bytes):
    size_kb = size_bytes / 1024
    if size_kb < 1024:
        return f"{size_kb:.2f}KB"
    size_mb = size_kb / 1024
    if size_mb < 1024:
        return f"{size_mb:.2f}MB"
    size_gb = size_mb / 1024
    return f"{size_gb:.2f}GB"


def get_temp_files(isSafe=True, number_of_unused_days="+3", get_root_files=False):
    cmd = ""
    if isSafe:
        cmd = f"sudo find /tmp -type f \( ! -user root \) -atime {number_of_unused_days}"
    else:
        if get_root_files:
            cmd = f"sudo find /tmp -atime {number_of_unused_days}"
        else:
            cmd = f"sudo find /tmp -type f \( ! -user root \) -atime {number_of_unused_days}"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    file_str = result.stdout.strip().split('\n')
    if file_str == ['']:
        return 0, ""
    else:
        total_size = 0
        with tqdm(total=len(file_str), ascii=" #", desc=f"Scanning: ", unit=" files") as pbar:
            for file in file_str:
                try:
                    file_size = os.path.getsize(file)
                    total_size += file_size
                except:
                    pass
                pbar.update(1)
        for file in file_str:
            print(file)
        return total_size, get_size_formatted(total_size)


def delete_temp_files(isSafe=True, number_of_unused_days="+3", get_root_files=False):
    cmd = ""
    if isSafe:
        cmd = f"sudo find /tmp -type f \( ! -user root \) -print -atime {number_of_unused_days} -delete"
    else:
        if get_root_files:
            cmd = f"sudo find /tmp -atime {number_of_unused_days} -print -delete"
        else:
            cmd = f"sudo find /tmp -type f \( ! -user root \) -print -atime {number_of_unused_days} -delete"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    file_str = result.stdout.strip().split('\n')
    if file_str == ['']:
        print("No files found to delete")
    else:
        for file_str in file_str:
            print(file_str)
        print("\nAll files deleted\n")


def main():
    while 1:
        hometable = PrettyTable()
        hometable.field_names = ["", "What do you desire?"]
        hometable.add_row(["1.", "Get safe temporary files"], divider=True)
        hometable.add_row(
            ["2.", "Get temporary files (advance)"], divider=True)
        hometable.add_row(["3.", "Exit"], divider=True)
        print(hometable)
        xin = ""
        x = 0
        a = 0
        try:
            xin = input("\nEnter Your Choice: \n")
            x = int(xin)
        except:
            print(
                "Unkown Input Detected, please Stick to the above number range, and try again!\n")
            continue
        print(f"\n{'*'*100}\n")
        if x == 1:
            print("Getting safe temporary files size:\n")
            flag = 1
            while flag:
                size_bytes, size_formatted = get_temp_files(isSafe=True)
                if size_bytes == 0:
                    print("No files found")
                else:
                    print(f"\nTotal size: {size_formatted}")
                    want_to_delete = input(
                        "\nDo you want to delete these files? (y/n): ")
                    if want_to_delete == "y" or want_to_delete == "Y":
                        delete_temp_files(isSafe=True)
                    else:
                        print("No files deleted")
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break
                print(f"\n{'*'*100}\n")
                if a == 1:
                    continue
                else:
                    flag = 0
                    break

        elif x == 2:
            flag = 1
            while flag:
                print("Temporary files(advance):\n")
                try:
                    unused_num_days = input(
                        "Please specify the number of days for which the temporary file remain unused that you want to get (enter -1 for all files otherwise enter like +3 for 3 days): ")
                    unused_num_days = int(unused_num_days)

                    get_root_files = input(
                        "Do you also want to fetch all temp files created by root user/services? (y/n):")
                    if get_root_files == "y" or get_root_files == "Y":
                        bool_get_root = True
                    else:
                        bool_get_root = False
                    size_bytes, size_formatted = get_temp_files(
                        isSafe=False, number_of_unused_days=unused_num_days, get_root_files=bool_get_root)
                    if size_bytes == 0:
                        print("No files found")
                    else:
                        print(f"\nTotal size: {size_formatted}")
                        want_to_delete = input(
                            "Do you want to delete all these files? (y/n): ")
                        if want_to_delete == "y" or want_to_delete == "Y":
                            delete_temp_files(
                                isSafe=False, number_of_unused_days=unused_num_days, get_root_files=bool_get_root)
                        else:
                            print("No files deleted")
                    while 1:
                        a = int(
                            input("\nEnter 1 to redo and 2 to exit to Home\n"))
                        if a == 1 or a == 2:
                            break
                    print(f"\n{'*'*100}\n")
                    if a == 1:
                        continue
                    else:
                        flag = 0
                        break
                except:
                    print("Invalid input detected, please try again!\n")
                    continue
        elif x == 3:
            break
        else:
            print(
                "Unkown Input Detected, Please Stick to the above number range, and lets try again ,shall we?\n"
            )


if __name__ == "__main__":
    main()