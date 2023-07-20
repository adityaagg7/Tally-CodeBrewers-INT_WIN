import shutil
import subprocess
import psutil
import os
from prettytable import PrettyTable


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def get_disk_usage():
    usage = psutil.disk_usage("./")

    # # print(os.getcwd())
    # total_space = usage.total
    # used_space = usage.used
    # free_space = usage.free
    # perc = usage.percent
    # total_gb = round(total_space*1e-9, 3)
    # used_gb = round(used_space*1e-9, 3)
    # free_gb = round(free_space*1e-9, 3)
    # print(
    #     f"\n\nTotal Space = {total_gb} GB \nUsed Space = {used_gb} GB \nFree Space = {free_gb} GB\nPercentage Used = {perc}%")

    total, used, free = shutil.disk_usage("/")

    print(f"Total:  {(total // (2**30))}")
    print(f"Used:  {(used // (2**30))})")
    print(f"Free:  {(free // (2**30))})")
    percent = ("{0:." + str(3) + "f}").format(100 * (used / float(total)))

    filledLength = int(100 * used // total)
    bar = "█" * filledLength + "-" * (100 - filledLength)
    print(f"\n |{bar}| {percent}% ", end="\n")


def get_disk_partition():
    partitions = psutil.disk_partitions(all=False)
    table = PrettyTable()
    table.field_names = ["Name", "Total Size", "Used", "Free"]

    for disk in partitions:
        if disk.fstype:
            # print(disk.device, psutil.disk_usage(disk.mountpoint))
            nam = disk.device
            disk = psutil.disk_usage(disk.mountpoint)
            total = disk.total
            used = disk.used
            free = disk.free
            table.add_row([nam, total, used, free], divider=True)

    print(table)


def main():
    while 1:
        print(
            "What do you desire ..? \n1) Check Overall Disk Usage\n2) Check Duplicate Files\n3) Get Files and Usage by Type\n4) Disk Partitions\n5) Exit"
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

        elif x == 45:
            break
        else:
            print(
                "Unkown Input Detected, Please Stick to the above number range, and lets try again ,shall we?\n"
            )


if __name__ == "__main__":
    main()
