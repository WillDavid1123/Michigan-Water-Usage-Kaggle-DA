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
    root.title("Michigan Water Usage From 2013 to 2022")
    mainframe = tk.Frame(root)
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    main_labels = []
    l1 = tk.Label(mainframe, text="Michigan Water Usage From 2013 to 2022", font=('bold', 16, "underline"))
    l1.grid(row=1, column=1, padx=(10, 10), pady=(5, 10))
    # l1.place(relx=0, rely=0)
    main_labels.append(l1)
    b1 = tk.Button(mainframe, text="Bar Graph", command=lambda: bar_graph(root, mainframe, data, headers, main_labels))
    b1.grid(row=2, column=1, pady=(0, 10))
    # b1.place(relx=.2, rely=.5)
    main_labels.append(b1)

    root.mainloop() 


def bar_graph(root, mainframe, data, headers, main_labels):
    '''Create a bar graph with the data specified by the user'''
    # Remove main menu elements
    remove_labels(main_labels)

    # Create labels
    bar_graph_labels = []
    l1 = tk.Label(mainframe, text="Bar Graph", font=('bold', 16, "underline"))
    l1.grid(row=1, column=1, padx=(10, 10), pady=(5, 10), columnspan=2)
    bar_graph_labels.append(l1)

    l2 = tk.Label(mainframe, text="X Axis:")
    l2.grid(row=2, column=1, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(l2)

    x_axis_string = tk.StringVar(root)
    x_axis_string.set(headers[0])
    om1 = tk.OptionMenu(mainframe, x_axis_string, headers[0], headers[5], headers[6])
    om1.grid(row=2, column=2, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(om1)

    l3 = tk.Label(mainframe, text="Y Axis:")
    l3.grid(row=3, column=1, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(l3)

    y_axis_string = tk.StringVar(root)
    y_axis_string.set(headers[1])
    om2 = tk.OptionMenu(mainframe, y_axis_string, headers[1], headers[2], headers[3], headers[4])
    om2.grid(row=3, column=2, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(om2)

    b1 = tk.Button(mainframe, text="Create Bar Graph", command=lambda: create_bar_graph(x_axis_string, y_axis_string, data, headers))
    b1.grid(row=4, column=1, padx=(10, 10), pady=(5, 10), columnspan=2)
    bar_graph_labels.append(b1)

def create_bar_graph(x_axis, y_axis, data, headers):
    pass


def remove_labels(labels):
    '''Remove all labels from the window'''
    for label in labels:
        label.grid_remove()


if __name__ == "__main__":
    main()