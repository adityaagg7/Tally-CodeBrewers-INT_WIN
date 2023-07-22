import tkinter as tk

from temp_files import main as temp
from tkt_breakdown_updated import main as breakdown
from tkt_large_files_updated import main as large
from tkt_scan_updated import main as scan
from tktduplicate_delete import main as dupldel
from tktefficent_Delete_updated import main as effdel


def beautify_buttons():
    button_style = {"font": ("Arial", 16), "width": 20, "height": 2, "bg": "lightblue", "bd": 0}

    button1 = tk.Button(root, text="Check Large Files", command=large, **button_style)
    button1.pack(pady=10)

    button2 = tk.Button(root, text="Scan File Type", command=scan, **button_style)
    button2.pack(pady=10)

    button3 = tk.Button(root, text="Breakdown By File Type", command=breakdown, **button_style)
    button3.pack(pady=10)

    button4 = tk.Button(root, text="Find Duplicates", command=dupldel, **button_style)
    button4.pack(pady=10)

    button5 = tk.Button(root, text="Efficient Deletion", command=effdel, **button_style)
    button5.pack(pady=10)

    button6 = tk.Button(root, text="Delete Temporary Files", command=temp, **button_style)
    button6.pack(pady=10)


root = tk.Tk()
root.title("Button Functions")
root.geometry("600x500")

beautify_buttons()

root.mainloop()
