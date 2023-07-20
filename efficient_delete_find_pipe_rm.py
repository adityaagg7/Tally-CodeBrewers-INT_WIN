import subprocess
import time


def delete_files_in_directory(directory):
    """Delete all files in the specified directory using find and xargs."""
    try:
        start_time = time.time()
        # subprocess.run(["find", directory, "-type", "f", "-print0", "|", "xargs", "-0", "rm", "-f"])
        command = f"find {directory} -type f -print0 | xargs -0 rm -f"
        subprocess.run(command, shell=True)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(
            f"Successfully deleted all files in the directory in {elapsed_time:.2f} seconds."
        )
    except Exception as e:
        print(f"Failed to delete files: {e}")


def main():
    directory_to_delete = "/home/manav/Workspaces/vscode/cli/test2"  # Replace with the directory where you want to delete files

    delete_files_in_directory(directory_to_delete)
