import os
from run_command import run_command
from prettytable import PrettyTable


def main():
    file_type = input("Please enter the file type you want to search for: ")
    directory_to_scan = input(
        """\nPlease enter the directory you want to scan\n(leave blank for home directory)\n(for root directory enter / (maxdepth will be 3))\n(for current directory just enter .): """
    )
    command = ""
    while 1:
        if directory_to_scan == "":
            directory_to_scan = os.path.expanduser("~")
            command = f"find {directory_to_scan} -type f \\( -name \\*.{file_type} \\)   -print0 | xargs -0 du -sh | sort -h "
            break
        elif directory_to_scan == "/":
            command = f"sudo find / maxdepth 3 -type f \\( -name \\*.{file_type} \\)   -print0 | xargs -0 du -sh | sort -h "
            break
        else:
            if os.path.exists(directory_to_scan) and os.path.isdir(directory_to_scan):
                command = f"find {directory_to_scan} -type f \\( -name \\*.{file_type} \\)   -print0 | xargs -0 du -sh | sort -h "
                break
            else:
                print(
                    f"{directory_to_scan} doesnt exist or is not a Directory, Try again!"
                )

    a = run_command(command=command)
    s = ""
    if a:
        # print(a)
        a = a.split("\n")
        table = PrettyTable()
        table.field_names = ["Size", "File Name"]

        for line in a:
            size = line.split("\t")[0]
            nam = line.split("\t")[1]
            table.add_row([size, nam], divider=True)
        print(table)
        print(
            "\nEnter 'X' to delete all above files, or \nEnter 'Y' to not delete any, or \nEnter the path of the file to delete a single file"
        )
        s = input()
        if s == "X":
            command += " | rm -rf"
            run_command(command=command)
        elif s != "Y":
            os.remove(s)
    else:
        print("No Duplicates Found!")
