from prettytable import PrettyTable
import find_delete_duplicate as duplicate_deleter
import search_by_specific_file_type as file_type_module
import efficient_delete_find_pipe_rm
import breakdown_by_file_types as breakdown_types
from disk_usage_stats import get_disk_usage, get_disk_partition
from large_files_check import get_large_files


def main():
    while 1:
        hometable = PrettyTable()
        hometable.field_names = ["", "What do you desire?"]
        hometable.add_row(["1.", "Check Disk Usage"], divider=True)
        hometable.add_row(["2.", "Check For Duplicate Files"], divider=True)
        hometable.add_row(["3.", "Get File Details By Type"], divider=True)
        hometable.add_row(["4.", "Get Disk Partioning Info"], divider=True)
        hometable.add_row(["5.", "Check For Large Sized Files"], divider=True)
        hometable.add_row(
            ["6.", "Efficiently Delete High Number of Files"], divider=True
        )
        hometable.add_row(["7.", "Check Space Used by Each File Type "], divider=True)
        hometable.add_row(["8.", "Exit"], divider=True)
        print(hometable)
        xin = input("\nEnter Your Choice: \n")
        x = 0
        try:
            x = int(xin)
        except:
            print(
                "Unkown Input Detected, please Stick to the above number range, and try again!\n"
            )
            continue

        print(f"\n{'*'*100}\n")

        if x == 1:
            print("Showing Disk Usage Statistics:\n")
            get_disk_usage()
            input("\n\nPRESS 'ENTER' to go HOME\n\n")
        elif x == 4:
            print("Showing Disk Usage Statistics:\n")
            get_disk_partition()
            input("\n\nPRESS 'ENTER' to go HOME\n\n")
        elif x == 5:
            get_large_files()
            input("\n\nPRESS 'ENTER' to go HOME\n\n")
        elif x == 2:
            duplicate_deleter.main()
            input("\n\nPRESS 'ENTER' to go HOME\n\n")
        elif x == 3:
            file_type_module.main()
            input("\n\nPRESS 'ENTER' to go HOME\n\n")
        elif x == 6:
            efficient_delete_find_pipe_rm.main()
            input("\n\nPRESS 'ENTER' to go HOME\n\n")

        elif x == 7:
            breakdown_types.main()
            input("\n\nPRESS 'ENTER' to go HOME\n\n")

        elif x == 8:
            break
        else:
            print(
                "Unkown Input Detected, Please Stick to the above number range, and lets try again ,shall we?\n"
            )


if __name__ == "__main__":
    main()
