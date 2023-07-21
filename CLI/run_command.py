import subprocess


def run_command(command):
    # print("Starting Check\n")
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    # print("Done\n")
    return result.stdout.strip()
