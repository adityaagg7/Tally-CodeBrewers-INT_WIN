from nlp_similarity import main as nlp_similarity_main
import os
import readline

readline.set_completer_delims(' \t\n=')

doc_set = {".docx", ".doc", ".odt", ".pdf", ".txt"}


def split_file_path(file_path):
    base_path, file_extension = os.path.splitext(file_path)
    return file_extension


def solve(path):
    print("Searching...\n")
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(root, file))
    file_list = sorted(file_list)
    # print("LOL")
    flag = 0
    for file1 in file_list:
        flag = 1
        f1_extension = split_file_path(file1)
        file_list.remove(file1)
        if f1_extension in doc_set:
            for file2 in file_list:
                f2_extension = split_file_path(file2)
                if f2_extension in doc_set:
                    similarity = nlp_similarity_main(file1, file2)
                    if similarity > 0.8:
                        print(
                            f"{file1} is similar to {file2} with {round(similarity*100, 2)}% similarity")
                        choice = input(
                            "Do you want to delete any of the files? (y/n): ").strip().lower()
                        if choice == 'y':
                            print("Which file do you want to delete? (1/2): ")
                            choice = input().strip()
                            if choice == '1':
                                os.remove(file1)
                                print(f"Deleted: {file1}")
                            elif choice == '2':
                                os.remove(file2)
                                print(f"Deleted: {file2}")
                            else:
                                print("Invalid choice")
                        elif choice == 'n':
                            continue
                        else:
                            print("Invalid choice")

    if (flag):
        print("None Found")
    # print("LOL")


def main():
    while 1:
        readline.parse_and_bind("tab: complete")
        path = input("Enter Path of directory to search for:\n")
        print("\n")
        if (os.path.exists(path)):
            solve(path)
        else:
            print("Not Directory")

        x = int(input("Enter 1 to redo and 2 to exit: "))
        if (x == 2):
            return


# main("/home/manav/Downloads/hell")
