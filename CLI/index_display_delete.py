from prettytable import PrettyTable
import os


def main(files):
    m = {}
    i = 0
    table = PrettyTable()
    table.field_names = ['Index', 'Size', 'FilePath']
    for path, size in files:
        m[i] = (path, size)
        table.add_row([i, m[i][1], m[i][0]], divider=True)
        i += 1

    print(table)
    inp = input(
        "\nEnter the comma-separated indices of the files to be deleted or leave empty to exit:   ")

    if len(inp) == 0:
        return
    if (inp == 'all'):
        for path, size in files:
            os.remove(path)
            print("Deleted ", path, "\n")
        print("Deleted all Files\n")
        return

    indices = inp.split(',')
    for index in indices:

        if index.count('-') > 0:
            index1 = int(index.split('-')[0])
            index2 = int(index.split('-')[1])
            for i in range(index1, index2+1):
                if os.path.exists(m[int(i)][0]):
                    os.remove(m[int(i)][0])
                    table.del_row(int(i))
                    print("Deleted ", m[int(i)][0], "\n")
                else:
                    print(f"File {m[int(i)][0]} not found \n")
        else:
            if os.path.exists(m[int(index)][0]):
                os.remove(m[int(index)][0])
                table.del_row(int(index))
                print("Deleted ", m[int(index)][0], "\n")
            else:
                print(f"File {m[int(index)][0]} not found \n")


# main([('/Users/sunidhiaggarwal/Documents/GitHub/Tally-CodeBrewers-INT_WIN/tesat/testssfd', 24),('/home/gsuare/Desktop/hi/h1.txt', 77)])
