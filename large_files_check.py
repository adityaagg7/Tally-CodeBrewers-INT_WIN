from run_command import run_command
import os


def get_large_files():
    path = input("Enter Path of Directory to Search or press ENTER for Home\n")
    if path == "/":
        out = run_command(
            f"sudo find {path} -maxdepth 4 -type f -print0 | xargs -0 du -sh | sort -rh | head -n 10"
        )
        print(out)
        return

    elif path == "":
        path = os.path.expanduser("~")
    elif path[len(path) - 1 != "/"]:
        path += "/*"

    else:
        path += "*"
    out = run_command(
        f"sudo find {path} -type f -print0 | xargs -0 du -sh | sort -rh | head -n 10"
    )
    print(out)
