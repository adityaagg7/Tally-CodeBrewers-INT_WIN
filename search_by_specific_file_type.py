import subprocess
import os


def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    print(result.stdout.strip())
    return result.stdout.strip()


def main():
    file_type = input("Please enter the file type you want to search for: ")
    directory_to_scan = input(
        """Please enter the directory you want to scan\n(leave blank for home directory)\n(for root directory enter / (maxdepth will be 3))\n(for current directory just enter .): """
    )

    if directory_to_scan == "":
        directory_to_scan = os.path.expanduser("~")
        command = f"sudo find {directory_to_scan} maxdepth 3 -type f \\( -name \\*.{file_type} \\)   -print0 | xargs -0 du -sh | sort -rh"
    elif directory_to_scan == "/":
        command = f"sudo find / maxdepth 3 -type f \\( -name \\*.{file_type} \\)   -print0 | xargs -0 du -sh | sort -rh"
    else:
        command = f"find {directory_to_scan} -type f \\( -name \\*.{file_type} \\)   -print0 | xargs -0 du -sh | sort -rh"

    a = run_command(command=command)
    s=""
    if a:
        print(
            "Enter 'X' to delete all above files, or \nEnter 'Y' to not delete any, or \nEnter the path of the file to delete a single file"
        )
        s = input()
    if s == "X":
        command += " | rm -rf"
        run_command(command=command)
    elif s != "Y":
        os.remove(s)


# main()
