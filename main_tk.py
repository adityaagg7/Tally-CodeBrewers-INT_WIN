import tkinter as tk
from tkt_large_files import main as large
from tkt_scan import main as scan
from tktbreakdown_by_file_type import main as breakdown
from tktduplicate_delete import main as dupldel
from tktefficentDelete import main as effdel
 
root = tk.Tk()
root.title("Button Functions")

button1 = tk.Button(root, text="Button 1", command=large)
button1.pack()

button2 = tk.Button(root, text="Button 2", command=scan)
button2.pack()

button3 = tk.Button(root, text="Button 3", command=breakdown)
button3.pack()

button4 = tk.Button(root, text="Button 4", command=dupldel)
button4.pack()

button5 = tk.Button(root, text="Button 5", command=effdel)
button5.pack()

root.mainloop() 