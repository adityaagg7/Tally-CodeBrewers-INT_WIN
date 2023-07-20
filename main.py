import shutil
import subprocess
import psutil
import os
from prettytable import PrettyTable
import find_delete_duplicate as duplicate_deleter
import search_by_specific_file_type as file_type_module
import efficient_delete_find_pipe_rm
import breakdown_by_file_types as breakdown_types


def run_command(command):
    print("Starting Check\n")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print("Done\n")
    return result.stdout.strip()


def get_large_files():
    path = input("Enter Path of Directory to Search or press ENTER for Home\n")
    if path == "/":
        out = run_command(
            f"sudo find {path} -maxdepth 4 -type f -print0 | xargs -0 du -sh | sort -rh | head -n 10"
        )
        print(out)
        return

    elif path == "":
        path = os.path.expanduser("~")
    elif path[len(path) - 1 != "/"]:
        path += "/*"

    else:
        path += "*"
    out = run_command(
        f"sudo find {path} -type f -print0 | xargs -0 du -sh | sort -rh | head -n 10"
    )
    print(out)


def get_disk_usage():
    total, used, free = shutil.disk_usage("/Users")
    table = PrettyTable()
    table.field_names = [" ", "Size"]

    table.add_row(["Total", f"{(total // (1e9))} GB"], divider=True)
    table.add_row(["Used", f"{(used // (1e9))} GB"], divider=True)
    table.add_row(["Free", f"{(free // (1e9))} GB"], divider=True)
    print(table)
    percent = ("{0:." + str(3) + "f}").format(100 * (used / float(total)))

    filledLength = int(100 * used // total)
    bar = "█" * filledLength + "-" * (100 - filledLength)
    print(f"\n [{bar}] {percent}% ", end="\n")


def get_disk_partition():
    partitions = psutil.disk_partitions(all=False)
    table = PrettyTable()
    table.field_names = ["Name", "Total Size(GB)", "Used(GB)", "Free(GB)"]

    for disk in partitions:
        if disk.fstype:
            nam = disk.device
            disk = psutil.disk_usage(disk.mountpoint)
            total = round(disk.total * 1e-9, 3)
            used = round(disk.used * 1e-9, 3)
            free = round(disk.free * 1e-9, 3)
            table.add_row([nam, total, used, free], divider=True)

    print(table)


def main():
    while 1:
        print(
            "What do you desire ..?\n\n1) Check Overall Disk Usage\n2) Check Duplicate Files\n3) Get Files and Usage by Type\n4) Disk Partitions\n5) Check for Large Files\n6) Efficient Delete\n7) Breakdown on Basis of File Type\n8) Exit"
        )
        xin = input("\nINPUT->")
        x = 0
        try:
            x = int(xin)
        except:
            print(
                "Unkown Input Detected, Please Stick to the above number range, and lets try again ,shall we?\n"
            )
            continue

        print("\n")

        if x == 1:
            get_disk_usage()
            input("\n\nPRESS 'ENTER' to go HOME\n\n")
        elif x == 4:
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
