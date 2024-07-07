# main.py
# Explore water usage by industries in Michigan

# Imports
import os
import pdb
import math
# External Libraries (pip installs)
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = "water_use_data_2013_to_2022.csv"
NUM_COLS = [i for i in range(1, 8)]

def main():
    # pdb.set_trace()
    # Load data
    headers = np.genfromtxt(os.path.join(ROOT, DATA), delimiter=",", dtype=str)[0][1:]
    data = np.genfromtxt(os.path.join(ROOT, DATA), delimiter=",", usecols=NUM_COLS, dtype=None, names=True)

    # pdb.set_trace()

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
    '''Window for creating bar graphs'''
    # Remove main menu elements
    remove_labels(main_labels)

    # Create labels
    bar_graph_labels = []
    b1 = tk.Button(mainframe, text="Back", command=lambda: back_to_main(bar_graph_labels, main_labels))
    b1.grid(row=1, column=1, padx=(10, 10), pady=(5, 0))
    bar_graph_labels.append(b1)

    l1 = tk.Label(mainframe, text="Bar Graph", font=('bold', 16, "underline"))
    l1.grid(row=2, column=1, padx=(10, 10), pady=(5, 10), columnspan=2)
    bar_graph_labels.append(l1)

    l2 = tk.Label(mainframe, text="X Axis:")
    l2.grid(row=3, column=1, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(l2)

    x_axis_string = tk.StringVar(root)
    x_axis_string.set(headers[0])
    om1_options = [headers[0], headers[5], headers[6]]
    om1 = tk.OptionMenu(mainframe, x_axis_string, *om1_options)
    om1.grid(row=3, column=2, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(om1)

    l3 = tk.Label(mainframe, text="Y Axis:")
    l3.grid(row=4, column=1, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(l3)

    y_axis_string = tk.StringVar(root)
    y_axis_string.set(headers[1])
    om2_options = [headers[1], headers[2], headers[3], headers[4]]
    om2 = tk.OptionMenu(mainframe, y_axis_string, *om2_options)
    om2.grid(row=4, column=2, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(om2)

    l4 = tk.Label(mainframe, text="Specify other data:")
    l4.grid(row=5, column=1, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(l4)

    limiter_string = tk.StringVar(root)
    limiter_string.set("")
    om3_options = [""]
    om3 = tk.OptionMenu(mainframe, limiter_string, *om3_options)
    om3.grid(row=6, column=1, columnspan=2, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(om3)

    specify_string = tk.StringVar(root)
    specify_string.set("None")
    om4_options = ["None", headers[0], headers[5], headers[6]]
    om4 = tk.OptionMenu(mainframe, specify_string, *om4_options)#, command=lambda i: change_options(specify_string.get(), data, om3)
    om4.grid(row=5, column=2, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(om4)

    b2 = tk.Button(mainframe, text="Create Bar Graph", command=lambda: create_bar_graph(x_axis_string.get(), y_axis_string.get(), data))
    b2.grid(row=7, column=1, padx=(10, 10), pady=(5, 10), columnspan=2)
    bar_graph_labels.append(b2)


# def change_options(string, data, options_menu):
#     '''Change the specify options to new options'''
#     if string == "None":
#         return
#     for option in np.unique(data[string]):



def create_bar_graph(x_axis, y_axis, data):
    '''Create a bar graph with the data specified by the user'''

    x_data = np.unique(data[x_axis])
    x_ind = data.dtype.names.index(x_axis)

    y_data = np.zeros((len(x_data),))
    for i, x in enumerate(x_data):
        rows = np.where(data[:][x_axis] == x)
        for row in rows[0]:
            y_data[i] += data[row][y_axis]

    y_height = np.amax(y_data) * 1.1
    num_x_points = 10
    if x_axis == 'county':
        num_x_points = 11
    elif x_axis == 'industry':
        num_x_points = 4
    for i in range(math.ceil(len(x_data) / num_x_points)):
        fig, ax = plt.subplots(figsize=(14, 5))
        if num_x_points*(i+1) <= len(x_data):
            ax.bar(x_data[num_x_points*i:num_x_points*(i+1)], y_data[num_x_points*i:num_x_points*(i+1)], color=["lightsteelblue", "cornflowerblue", "royalblue", "midnightblue", "navy"])
        else:
            ax.bar(x_data[num_x_points*i:-1], y_data[num_x_points*i:-1], color=["lightsteelblue", "cornflowerblue", "royalblue", "midnightblue", "navy"])
        ax.set_title(y_axis + " per " + x_axis)
        ax.set_ylim([0, y_height])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)

    plt.show()
    pass


def remove_labels(labels):
    '''Remove all labels from the window'''
    for label in labels:
        label.grid_remove()


def back_to_main(curr_labels, main_labels):
    remove_labels(curr_labels)
    for label in main_labels:
        label.grid()


if __name__ == "__main__":
    main()