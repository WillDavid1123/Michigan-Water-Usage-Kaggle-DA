# main.py
# Explore water usage by industries in Michigan

# Imports
import os
import pdb
# External Libraries (pip installs)
import numpy as np
import tkinter as tk
import matplotlib

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = "water_use_data_2013_to_2022.csv"
NUM_COLS = [i for i in range(1, 8)]

def main():
    # Load data
    headers = np.genfromtxt(os.path.join(ROOT, DATA), delimiter=",", dtype=str)[0][1:]
    data = np.genfromtxt(os.path.join(ROOT, DATA), delimiter=",", skip_header=1, usecols=NUM_COLS, dtype=(str, np.int64, np.int64, np.int64, np.int64, str, int))

    # Create main window
    root = tk.Tk()

    # screen_width = root.winfo_screenwidth()
    # screen_height = root.winfo_screenheight()
    # screen_middle = str(screen_width//2) + "+" + str(screen_height//2)
    # root.geometry("450x200+" + screen_middle)

    root.title("Michigan Water Usage From 2013 to 2022")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    main_labels = []
    l1 = tk.Label(text="Michigan Water Usage From 2013 to 2022", font=('bold', 16, "underline"))
    l1.grid(row=1, column=1, padx=(10, 10), pady=(5, 10))
    # l1.place(relx=0, rely=0)
    main_labels.append(l1)
    b1 = tk.Button(text="Bar Graph", command=lambda: bar_graph(root, data, headers, main_labels))
    b1.grid(row=2, column=1, pady=(0, 10))
    # b1.place(relx=.2, rely=.5)
    main_labels.append(b1)

    root.mainloop() 


def bar_graph(root, data, headers, main_labels):
    '''Create a bar graph with the data specified by the user'''
    # Remove main menu elements
    remove_labels(main_labels)

    # Create labels
    bar_graph_labels = []
    l1 = tk.Label(text="Bar Graph", font=('bold', 16, "underline"))
    l1.grid(row=1, column=1, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(l1)

    l2 = tk.Label(text="Group By:")
    l2.grid(row=2, column=1, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(l2)

    group_by_string = tk.StringVar(root)
    group_by_string.set(headers[0])
    om1 = tk.OptionMenu(root, group_by_string, *headers)
    bar_graph_labels.append(om1)

    pass

def remove_labels(labels):
    '''Remove all labels from the window'''
    for label in labels:
        label.grid_remove()


if __name__ == "__main__":
    main()