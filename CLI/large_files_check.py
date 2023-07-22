from run_command import run_command
import os
from Spinner_Loder import SpinnerThread
from prettytable import PrettyTable
import index_display_delete


def get_size_formatted(size_bytes):
    size_kb = size_bytes / 1024
    if size_kb < 1024:
        return f"{size_kb:.2f}KB"
    size_mb = size_kb / 1024
    if size_mb < 1024:
        return f"{size_mb:.2f}MB"
    size_gb = size_mb / 1024
    return f"{size_gb:.2f}GB"


def convert_size(size, unit, convert_bytes_to_unit):
    units = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 * 1024,
        'GB': 1024 * 1024 * 1024,
        'TB': 1024 * 1024 * 1024 * 1024
    }
    if convert_bytes_to_unit:
        return size / units[unit]
    else:
        return size * units[unit]


def get_large_files():
    path = input("Enter Path of Directory to Search or press ENTER for Home\n")
    spinner_thread = SpinnerThread()
    spinner_thread.start()
    if path == "/":
        out = run_command(
            f"sudo find {path} -maxdepth 4 -type f -print0 | xargs -0 du -sh |  sort -hr  | head -n 10"
        )
        # print(out)
        return

    elif path == "":
        path = os.path.expanduser("~")
    elif path[len(path) - 1 != "/"]:
        path += "/*"

    else:
        path += "*"
    a = run_command(
        f"find {path} -type f -print0 | xargs -0 du -sh |  sort -hr  | head -n 10"
    )
    spinner_thread.stop()
    # print(a)
    # print("\n")
    if a:
        a = a.split("\n")
        # table = PrettyTable()
        # table.field_names = ["Size", "File Name"]
        list = []
        total_size = 0
        for line in a:
            size = line.split("\t")[0]
            nam = line.split("\t")[1]
            # print(line)
            # print(size)
            list.append([nam, size])
            if size[-1] == "B":
                size = float(size[:-1])
            elif size[-1] == "K":
                size = convert_size(float(size[:-1]), "KB", False)
            elif size[-1] == "M":
                size = convert_size(float(size[:-1]), "MB", False)
            elif size[-1] == "G":
                size = convert_size(float(size[:-1]), "GB", False)
            total_size += int(size)
        # print("\nTotal size: ", total_size)")
        total_size = get_size_formatted(total_size)
        list.append(["Total size", total_size])
        index_display_delete.main(list)
        # table.add_row([size, nam], divider=True)
        # print(table)
