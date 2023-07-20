import subprocess


def run_command(command):
    result = subprocess.run(command, shell=True,
                            capture_output=True, text=True)
    print(result.stdout.strip())
    return result.stdout.strip()


def main():
    
    file_type=input("Please enter the file type you want to search for: ")
    directory_to_scan = input("""Please enter the directory you want to scan\n(leave blank for home directory)\n(for root directory enter / (maxdepth will be 3))\n(for current directory just enter .): """)
    command=f"sudo find {directory_to_scan} -iname '*.{file_type}' -print0 | du -ch --files0-from=- | sort -h" 

    if directory_to_scan=="":
        directory_to_scan="/home/manav/"
        command=f"sudo find {directory_to_scan} -iname '*.{file_type}' -print0 | du -ch --files0-from=- | sort -h" 
    elif directory_to_scan == "/":
        command=f"sudo find {directory_to_scan} -maxdepth 3 -iname '*.{file_type}' -print0 | du -ch --files0-from=- | sort -h" 
    
    run_command(command=command)
