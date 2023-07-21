import psutil
import shutil
from prettytable import PrettyTable
from run_command import run_command


def get_disk_usage():
    total, used, free = shutil.disk_usage("/")
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
