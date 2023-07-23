import subprocess
import time
import os

import readline

readline.set_completer_delims(' \t\n=')

def delete_files_in_directory(directory):
    try:
        start_time = time.time()
        command = f"find {directory} -type f -print0 | xargs -0 rm -f"
        subprocess.run(command, shell=True)

    except Exception as e:
        print(f"Failed to delete files: {e}")


def main():
    readline.parse_and_bind("tab: complete")
    
    directory_to_delete = input("Enter path for directory of leave empty for Home ")
    if directory_to_delete == "":
        directory_to_delete = os.path.expanduser("~")

    delete_files_in_directory(directory_to_delete)
