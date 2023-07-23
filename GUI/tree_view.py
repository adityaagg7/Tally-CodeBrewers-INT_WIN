import os
import subprocess
import tkinter as tk
from tkinter import *
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

primary_color = "#1f3557"
secondary_color = "#f2a154"
bg_color = "#f5f5f5"
text_color = "#333333"


def main():
    def get_subdir_size(path, max_depth=1):
        cmd = f"du -ad {max_depth} {path}"
        result = subprocess.run(
            cmd, shell=True, capture_output=True, text=True)
        list_of_directories = result.stdout.strip().split('\n')
        final_list = []
        for directory in list_of_directories:
            split_list = directory.split("\t")
            if split_list[-1].startswith(path):
                split_list[-1] = split_list[-1][len(path):]
            final_list.append(split_list)
        final_list[-1][-1] = "Total"
        return final_list

    def create_pie_chart(frame, path):
        list_of_size_and_dir = get_subdir_size(path)
        sizes = []
        subdirectories = []
        total_size = 0
        for list in list_of_size_and_dir:
            if list[-1] != "Total":
                total_size += int(list[0])
                sizes.append(list[0])
                subdirectories.append((list[-1]))
        fig = Figure(figsize=(7, 7))
        # fig = Figure()
        ax = fig.add_subplot(111)
        # wedges, patches, texts = ax.pie(sizes, labels=None, autopct='%1.1f%%')
        ax.pie(sizes, labels=None)
        labels = [
            f'{l}, {100 * int(s) / total_size:.2f}%' for l, s in zip(subdirectories, sizes)]
        ax.legend(loc='best', labels=labels, alignment='right', draggable=True)
        # ax.legend(bbox_to_anchor=(1, 0.5), loc='center left', labels=labels)
        canvas = FigureCanvasTkAgg(fig, master=frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

    def populate_treeview(tree, parent, path):
        items = os.listdir(path)
        for item in items:
            item_path = os.path.join(path, item)
            is_directory = os.path.isdir(item_path)
            item_id = tree.insert(parent, "end", text=item, values=[
                                  item_path], open=False)
            if is_directory:
                tree.insert(item_id, "end", text="dummy")

    def on_node_expand(event):
        item = event.widget.focus()
        if not item:
            return
        tree = event.widget
        list_of_children = tree.get_children(item)
        selected_item = tree.item(item)
        if selected_item["text"] != home_directory:
            path = tree.item(item)["values"][0]
        else:
            path = home_directory
        if list_of_children and tree.item(list_of_children[0], option="text") == "dummy":
            tree.delete(list_of_children[0])
            populate_treeview(tree, item, path)
        if path != home_directory:
            for widget in right_frame.winfo_children():
                widget.destroy()
            create_pie_chart(right_frame, path)

    def delete_item():
        selected_item = treeview.focus()
        if selected_item:
            item = treeview.item(selected_item)
            path = item["values"][0]
            if os.path.exists(path):
                if os.path.isdir(path):
                    os.rmdir(path)
                else:
                    os.remove(path)
                treeview.delete(selected_item)
                path = path.split("/")[:-1]
                path = "/".join(path)
                if path != home_directory:
                    for widget in right_frame.winfo_children():
                        widget.destroy()
                create_pie_chart(right_frame, path)

    def open_file_explorer():
        selected_item = treeview.focus()
        if selected_item:
            item = treeview.item(selected_item)
            path = item["values"][0]
            cmd = f"xdg-open {path}"
            subprocess.run(cmd, shell=True, capture_output=True, text=True)

    def do_popup(event):
        try:
            right_context_menu.tk_popup(event.x_root, event.y_root)
        finally:
            right_context_menu.grab_release()

    home_directory = os.path.expanduser("~")
    root = tk.Tk()
    root.title("File Explorer")
    left_frame = ttk.Frame(root, padding=10)
    right_frame = ttk.Frame(root, padding=10)
    left_frame.pack(side=LEFT)
    right_frame.pack(side=RIGHT)
    create_pie_chart(right_frame, home_directory)
    treeview = ttk.Treeview(left_frame)
    treeview.pack(fill="both", expand=True)
    root_node = treeview.insert("", "end", text=home_directory, open=False)
    treeview.insert(root_node, "end", text="dummy")
    treeview.bind("<<TreeviewOpen>>", on_node_expand)

    right_context_menu = Menu(root, tearoff=0)
    right_context_menu.add_command(
        label="Open in File Explorer", command=open_file_explorer)
    right_context_menu.add_command(label="Delete", command=delete_item)
    right_context_menu.add_separator()

    treeview.bind("<Button-3>", do_popup)
    right_frame.bind("<Button-3>", do_popup)
    left_frame.bind("<Button-3>", do_popup)

    root.mainloop()
# main()
