import os
import subprocess
from prettytable import PrettyTable
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

def get_temp_files_size(isSafe=True):
    total_size=0
    cmd=""
    if isSafe:
        cmd = "sudo find /tmp -type f \( ! -user root \) -atime +3"
    else: 
        cmd = "sudo find /tmp -type f \( ! -user root \)"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    file_str = result.stdout.strip().split('\n')
    with tqdm(total=len(file_str), ascii=" #" ,desc=f"Scanning: ", unit=" files") as pbar:
        for file in file_str:
            try:
                file_size=os.path.getsize(file)
                total_size+=file_size
            except:
                pass
            pbar.update(1)
    return total_size

def get_temp_files(isSafe=True):
    cmd=""
    if isSafe:
        cmd="sudo find /tmp -type f \( ! -user root \) -atime +3"
    else:
        cmd="sudo find /tmp -type f \( ! -user root \)"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    file_str = result.stdout.strip().split('\n')
    for file in file_str:
        print(file)

def delete_temp_files(isSafe=True, number_of_unsed_days=3):
    cmd="" 
    if isSafe:
        cmd=f"sudo find /tmp -type f \( ! -user root \) -print -atime +{number_of_unsed_days} -delete"
    else:
        cmd="sudo find /tmp -type f \( ! -user root \) -print -delete"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    file_str = result.stdout.strip().split('\n')
    if file_str==['']:
        print("No files found to delete")
    else:
        for file_str in file_str:
            print(file_str)


def main():
    while 1:
        hometable = PrettyTable()
        hometable.field_names = ["", "What do you desire?"]
        hometable.add_row(["1.", "Get safe temporary files size"], divider=True)
        hometable.add_row(["2.", "Get all temporary files size"], divider=True)
        hometable.add_row(["3.", "Print safe to delete temporary files"], divider=True)
        hometable.add_row(["4.", "Print all temporary files"], divider=True)
        hometable.add_row(["5.", "Delete temporary files that are safe to delete"], divider=True)
        hometable.add_row(["6.", "Delete all temporary files(may crash your system)"], divider=True)
        hometable.add_row(["7.", "Delete temporary files (advance)"], divider=True)
        hometable.add_row(["8.", "Exit"], divider=True)
        print(hometable)
        xin = input("\nEnter Your Choice: \n")
        x = 0
        a = 0
        try:
            x = int(xin)
        except:
            print(
                "Unkown Input Detected, please Stick to the above number range, and try again!\n"
            )
            continue
        print(f"\n{'*'*100}\n")
        if x == 1:
            print("Getting safe temporary files size:\n")
            while 1:
                print(get_temp_files_size(isSafe=True))
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break
                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        if x == 2:
            print("Getting all temporary files size:\n")
            while 1:
                size_in_bytes= get_temp_files_size(isSafe=False)
                print(get_size_formatted(size_in_bytes))
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break
                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        elif x == 3:
            print("Printing safe to delete temporary files:\n")
            while 1:
                get_temp_files(isSafe=True)
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break
                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        
        elif x == 4:
            print("Printing all temporary files:\n")
            while 1:
                get_temp_files(isSafe=False)
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break
                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break

        elif x == 5:
            print("Deleting temporary files that are safe to delete:\n")
            while 1:
                delete_temp_files(isSafe=True)
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break
                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        
        elif x == 6:
            print("Deleting all temporary files:\n")
            while 1:
                delete_temp_files(isSafe=False)
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break
                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        
        elif x == 7:
            flag=1
            while flag:
                print("Deleting temporary files(advance):\n")
                try:
                    unused_num_days=input("Please specify the number of days for which the file remain unused that you want to delete temporary files: ")
                    unused_num_days=int(unused_num_days)
                    delete_temp_files(isSafe=False, number_of_unsed_days=unused_num_days)
                    while 1:
                        a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                        if a == 1 or a == 2:
                            break
                    if a == 1:
                        continue
                    else:
                        print(f"\n{'*'*100}\n")
                        flag=0
                        break            
                except:
                    print("Invalid input detected, please try again!\n")
                    continue
        elif x == 8:
            break
        else:
            print(
                "Unkown Input Detected, Please Stick to the above number range, and lets try again ,shall we?\n"
            )


if __name__ == "__main__":
    main()
