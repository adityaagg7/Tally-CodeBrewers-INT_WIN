import os
import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

primary_color = "#1f3557"
secondary_color = "#f2a154"
bg_color = "#f5f5f5"
text_color = "#333333"


def get_directory_size(path):
    total_size = 0
    for dirpath, _, filenames in os.walk(path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            try:
                total_size += os.path.getsize(fp)
            except:
                pass
    return total_size


def get_subdirectory_sizes(path):
    subdirectories = [d for d in os.listdir(
        path) if os.path.isdir(os.path.join(path, d))]
    sizes = []
    for subdir in subdirectories:
        subdir_path = os.path.join(path, subdir)
        sizes.append(get_directory_size(subdir_path))
    return sizes


def get_path_of_item(self):
    item = treeview.selection()[0]
    parent_iid = treeview.parent(item)
    node = []
    while parent_iid != '':
        node.insert(0, treeview.item(parent_iid)['text'])
        parent_iid = treeview.parent(parent_iid)
    i = treeview.item(item, "text")
    # home_directory = os.path.expanduser("~")
    path = os.path.join(home_directory, *node, i)
    for widget in right_frame.winfo_children():
        widget.destroy()
    create_pie_chart(right_frame, path)


def create_pie_chart(frame, path):
    sizes = get_subdirectory_sizes(path)
    subdirectories = [d for d in os.listdir(
        path) if os.path.isdir(os.path.join(path, d))]

    fig = Figure()
    ax = fig.add_subplot(111)
    # wedges, patches, texts = ax.pie(sizes, labels=None, autopct='%1.1f%%')
    ax.pie(sizes, labels=None)
    # ax.pie(sizes, labels=subdirectories, autopct='%1.1f%%')
    # patches, labels, dummy = zip(*sorted(zip(patches, subdirectories, sizes),
    #                                      key=lambda x: x[2],
    #                                      reverse=True))
    # ax.legend(patches, labels, loc='center left', bbox_to_anchor=(-0.1, 1.),
    # fontsize=8)
    labels = [f'{l}, {s:0.1f}%' for l, s in zip(subdirectories, sizes)]
    ax.legend(bbox_to_anchor=(0.5, -0.05), loc='lower left', labels=labels)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill='both', expand=True)


# def create_vertical_buttons(frame, num_buttons):
#     for i in range(num_buttons):
#         ttk.Button(frame, text=f'Button {i + 1}').grid(row=i, column=0, pady=5)


def populate_treeview(tree, parent, path):
    items = os.listdir(path)
    for item in items:
        item_path = os.path.join(path, item)
        is_directory = os.path.isdir(item_path)
        item_id = tree.insert(parent, "end", text=item, open=False)

        if is_directory:
            populate_treeview(tree, item_id, item_path)


def create_tree(root):
    treeview.insert("", "end", text=home_directory, open=True)
    # Calling pack method on the treeview
    treeview.pack()
    populate_treeview(treeview, "", home_directory)

    # # Inserting items to the treeview
    # # Inserting parent
    # treeview.insert('', '0', 'item1',
    #                 text ='GeeksforGeeks')

    # # Inserting child
    # treeview.insert('', '1', 'item2',
    #                 text ='Computer Science')
    # treeview.insert('', '2', 'item3',
    #                 text ='GATE papers')
    # treeview.insert('', 'end', 'item4',
    #                 text ='Programming Languages')

    # # Placing each child items in parent widget
    # treeview.move('item2', 'item1', 'end')
    # treeview.move('item3', 'item1', 'end')
    # treeview.move('item4', 'item1', 'end')


# Create the main application window
root = tk.Tk()
root.title('Tkinter Horizontal Layouts')

# left_frame = ttk.Frame(root, padding=10)
# left_frame.grid(row=0, column=0, sticky='ns')

center_frame = ttk.Frame(root, padding=10)
center_frame.grid(row=0, column=1, sticky='ns')

right_frame = ttk.Frame(root, padding=10)
right_frame.grid(row=0, column=2, sticky='ns')

treeview = ttk.Treeview(center_frame, columns=1)
treeview.column("1", width=150)
treeview.bind('<ButtonRelease-1>', get_path_of_item)
home_directory = os.path.expanduser("~")

create_pie_chart(right_frame, home_directory)
# create_vertical_buttons(left_frame, 5)
# create_vertical_buttons(right_frame, 10)

create_tree(root)
root.mainloop()
