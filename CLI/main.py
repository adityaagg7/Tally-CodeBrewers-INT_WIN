import find_similar_files as text_similar
import  dhash_similar as image_similar
from prettytable import PrettyTable
import filter_search as file_type_module
import duplicate_delete_improved
import breakdown_by_file_types as breakdown_types
from disk_usage_stats import get_disk_usage, get_disk_partition
from large_files_check import get_large_files
import temp_files
import efficient_delete_find_pipe_rm as effdelete
import schedule_tasks


def main():
    while 1:
        hometable = PrettyTable()
        hometable.field_names = ["", "What do you desire?"]
        hometable.add_row(["1.", "Check Disk Usage"], divider=True)
        hometable.add_row(["2.", "Check For Duplicate Files"], divider=True)
        hometable.add_row(["3.", "Filter Search"], divider=True)
        hometable.add_row(["4.", "Get Disk Partioning Info"], divider=True)
        hometable.add_row(["5.", "Check For Large Sized Files"], divider=True)
        hometable.add_row(
            ["6.", "Efficiently Delete High Number of Files"], divider=True
        )
        hometable.add_row(
            ["7.", "Check Space Used by Each File Type "], divider=True)
        hometable.add_row(["8.", "Temporary Files"], divider=True)
        hometable.add_row(["9.", "Schedule Jobs"], divider=True)
        hometable.add_row(["10.", "Find Similar Document Files"], divider=True)
        hometable.add_row(["11.", "Find Similar Image Files"], divider=True)
        hometable.add_row(["12.", "Exit"], divider=True)
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
            print("Showing Disk Usage Statistics:\n")
            while 1:
                get_disk_usage()
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or a == 2:
                        break

                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        elif x == 2:
            while 1:
                duplicate_delete_improved.main()
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or 2:
                        break

                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        elif x == 3:
            while 1:
                file_type_module.main()
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or 2:
                        break

                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        elif x == 4:
            print("Showing Disk Usage Statistics:\n")
            while 1:
                get_disk_partition()
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or 2:
                        break

                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        elif x == 5:
            while 1:
                get_large_files()
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or 2:
                        break

                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        elif x == 6:
            while 1:
                effdelete.main()
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or 2:
                        break

                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break

        elif x == 7:
            while 1:
                breakdown_types.main()
                while 1:
                    a = int(input("\nEnter 1 to redo and 2 to exit to Home\n"))
                    if a == 1 or 2:
                        break

                if a == 1:
                    continue
                else:
                    print(f"\n{'*'*100}\n")
                    break
        elif x == 8:
            while 1:
                temp_files.main()
                print(f"\n{'*'*100}\n")
                break

        elif x == 9:
            while 1:
                schedule_tasks.main()
                print(f"\n{'*'*100}\n")
                break
        elif x == 10:
            while 1:
                text_similar.main()
                print(f"\n{'*'*100}\n")
                break
        elif x == 11:
            while 1:
                image_similar.main()
                print(f"\n{'*'*100}\n")
                break

        elif x == 12:
            break
        else:
            print(
                "Unkown Input Detected, Please Stick to the above number range, and lets try again ,shall we?\n"
            )


if __name__ == "__main__":
    main()
