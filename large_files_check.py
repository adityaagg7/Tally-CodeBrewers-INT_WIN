from run_command import run_command
import os
from Spinner_Loder import SpinnerThread
from prettytable import PrettyTable


def get_large_files():
    path = input("Enter Path of Directory to Search or press ENTER for Home\n")
    spinner_thread = SpinnerThread()
    spinner_thread.start()
    if path == "/":
        out = run_command(
            f"sudo find {path} -maxdepth 4 -type f -print0 | xargs -0 du -sh |  sort -rh  | head -n 10"
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
        f"find {path} -type f -print0 | xargs -0 du -sh |  sort -rh  | head -n 10"
    )
    spinner_thread.stop()

    if a:
        a = a.split("\n")
        table = PrettyTable()
        table.field_names = ["Size", "File Name"]

        for line in a:
            size = line.split("\t")[0]
            nam = line.split("\t")[1]
            table.add_row([size, nam], divider=True)
        print(table)
