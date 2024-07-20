# main.py
# Explore water usage by industries in Michigan

# Imports
import os
import pdb # pdb.set_trace()
import math
# External Libraries (pip installs)
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))
DATA = "water_use_data_2013_to_2022.csv"
NUM_COLS = [i for i in range(1, 8)]

def main():
    # Load data
    headers = np.genfromtxt(os.path.join(ROOT, DATA), delimiter=",", dtype=str)[0][1:]
    data = np.genfromtxt(os.path.join(ROOT, DATA), delimiter=",", usecols=NUM_COLS, dtype=None, names=True)

    # Create main window
    root = tk.Tk()
    root.title("Michigan Water Usage From 2013 to 2022")
    mainframe = tk.Frame(root)
    mainframe.grid(column=0, row=0)
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    # Create main menu labels
        # Title label
    main_labels = []
    l1 = tk.Label(mainframe, text="Michigan Water Usage From 2013 to 2022", font=('bold', 16, "underline"))
    l1.grid(row=1, column=1, padx=(10, 10), pady=(5, 10))
    # l1.place(relx=0, rely=0)
    main_labels.append(l1)

        # Bar Graph Button
    b1 = tk.Button(mainframe, text="Bar Graph", command=lambda: bar_graph(root, mainframe, data, headers, main_labels))
    b1.grid(row=2, column=1, pady=(0, 10))
    # b1.place(relx=.2, rely=.5)
    main_labels.append(b1)

        # Multi-line Graph Button
    b2 = tk.Button(mainframe, text="Multi-line Graph", command=lambda: multiline_graph(root, mainframe, data, headers, main_labels))
    b2.grid(row=3, column=1, pady=(0, 10))
    main_labels.append(b2)

    root.mainloop() 


def create_base_labels(main_labels, mainframe, title_string, y_axis_string, y_axis_options):
    '''Create base labels for all graphs (Back Button, Title, Y-axis)'''
    # Remove main menu elements
    remove_labels(main_labels)

    # Create multi-line graph labels
        # Back Button
    base_labels = []
    b1 = tk.Button(mainframe, text="Back", command=lambda: back_to_main(base_labels, main_labels))
    b1.grid(row=1, column=1, padx=(10, 10), pady=(5, 0))
    base_labels.append(b1)

        # Title Label
    l1 = tk.Label(mainframe, text=title_string, font=('bold', 16, "underline"))
    l1.grid(row=2, column=1, padx=(10, 10), pady=(5, 10), columnspan=2)
    base_labels.append(l1)

        # Y-Axis label
    l2 = tk.Label(mainframe, text="Y Axis:")
    l2.grid(row=4, column=1, padx=(10, 10), pady=(5, 10))
    base_labels.append(l2)

        # Y-Axis Options Menu
    y_axis_string.set(y_axis_options[0])
    om1_options = y_axis_options
    om1 = tk.OptionMenu(mainframe, y_axis_string, *om1_options)
    om1.grid(row=4, column=2, padx=(10, 10), pady=(5, 10))
    base_labels.append(om1)

    return base_labels
    pass


def bar_graph(root, mainframe, data, headers, main_labels):
    '''Window for creating bar graphs'''
    # Remove main menu elements
    remove_labels(main_labels)

    # Create bar graph labels
        # Base Labels
    y_axis_string = tk.StringVar(root)
    bar_graph_labels = create_base_labels(main_labels, mainframe, "Bar Graph", y_axis_string, [headers[1], headers[2], headers[3], headers[4]])

        # Data Limiter Label
    l4 = tk.Label(mainframe, text="Limit data:")
    l4.grid(row=5, column=1, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(l4)

        # Data Limiter Options Menu 1
    limiter_string = tk.StringVar(root)
    limiter_string.set("")
    om3_options = [""]
    om3 = tk.OptionMenu(mainframe, limiter_string, *om3_options, command=lambda t: print(limiter_string.get()))
    om3.grid(row=6, column=1, columnspan=2, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(om3)

        # Data Limiter Options Menu 2
    specify_string = tk.StringVar(root)
    specify_string.set("None")
    om4_options = ["None", headers[5], headers[6]]
    om4 = tk.OptionMenu(mainframe, specify_string, *om4_options, command=lambda i: change_options(specify_string.get(), limiter_string, data, om3))
    om4.grid(row=5, column=2, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(om4)

        # X-Axis Label
    l2 = tk.Label(mainframe, text="X Axis:")
    l2.grid(row=3, column=1, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(l2)

        # X-Axis Options Menu
    x_axis_string = tk.StringVar(root)
    x_axis_string.set(headers[0])
    curr_x_string = tk.StringVar(root)
    curr_x_string.set(headers[0])
    om1_options = [headers[0], headers[5], headers[6]]
    om1 = tk.OptionMenu(mainframe, x_axis_string, *om1_options, command=lambda y: update_limiter(x_axis_string, curr_x_string, om4, specify_string, limiter_string, data, om3))
    om1.grid(row=3, column=2, padx=(10, 10), pady=(5, 10))
    bar_graph_labels.append(om1)

        # Create Bar Graph Button
    b2 = tk.Button(mainframe, text="Create Bar Graph", command=lambda: create_bar_graph(x_axis_string.get(), y_axis_string.get(), specify_string.get(), limiter_string.get(), data))
    b2.grid(row=7, column=1, padx=(10, 10), pady=(5, 10), columnspan=2)
    bar_graph_labels.append(b2)


def create_bar_graph(x_axis, y_axis, limited, limiter, data):
    '''Create a bar graph with the data specified by the user'''

    # Prepare variables for data collection
    if limited == "county" or limited == "industry":
        limiter = bytes(limiter[2:-1], 'utf-8')
    elif limited == "year":
        limiter = int(limiter)
    x_data = np.unique(data[x_axis])

    #Grab and calculate data for bar graph
    y_data = np.zeros((len(x_data),))
    for i, x in enumerate(x_data):
        if limited != "None":
            a = np.array(np.where(data[:][x_axis] == x))
            rows = a[np.isin(a, np.array(np.where(data[:][limited] == limiter)))]
            for row in rows:
                y_data[i] += data[row][y_axis]
        else:
            rows = np.where(data[:][x_axis] == x)
            for row in rows[0]:
                y_data[i] += data[row][y_axis]

    # Prepare variables for bar graph creation
    y_height = np.amax(y_data) * 1.1
    num_x_points = 10
    if x_axis == 'county':
        num_x_points = 11
    elif x_axis == 'industry':
        num_x_points = 4
    if limited != "year":
        limiter = str(limiter)[2:-1]
    else:
        limiter = str(limiter)

    # Create bar graph(s)
    for i in range(math.ceil(len(x_data) / num_x_points)):
        fig, ax = plt.subplots(figsize=(14, 5))
        if num_x_points*(i+1) <= len(x_data):
            ax.bar(x_data[num_x_points*i:num_x_points*(i+1)], y_data[num_x_points*i:num_x_points*(i+1)], color=["lightsteelblue", "cornflowerblue", "royalblue", "midnightblue", "navy"])
        else:
            ax.bar(x_data[num_x_points*i:-1], y_data[num_x_points*i:-1], color=["lightsteelblue", "cornflowerblue", "royalblue", "midnightblue", "navy"])
        if limited != "None":
            ax.set_title(y_axis + " per " + x_axis + " in " + str(limited) + ": " + limiter)
        else:
            ax.set_title(y_axis + " per " + x_axis)
        ax.set_ylim([0, y_height])
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)

    plt.show()
    pass


def multiline_graph(root, mainframe, data, headers, main_labels):
    '''Window for creating multi-line graphs'''
    # Remove main menu elements
    remove_labels(main_labels)

    # Create multi-line graph labels
        # Base Labels
    y_axis_string = tk.StringVar(root)
    multi_line_graph_labels = create_base_labels(main_labels, mainframe, "Multi-line Graph", y_axis_string, [headers[1], headers[2], headers[3], headers[4]])

        # X-Axis Label
    l3 = tk.Label(mainframe, text="X Axis:")
    l3.grid(row=3, column=1, padx=(10, 10), pady=(5, 10))
    multi_line_graph_labels.append(l3)

        # X-Axis Options Menu
    x_axis_string = tk.StringVar(root)
    x_axis_string.set(headers[5])
    curr_x_string = tk.StringVar(root)
    curr_x_string.set(headers[5])
    om2_options = [headers[5], headers[6]]
    om2 = tk.OptionMenu(mainframe, x_axis_string, *om2_options)
    om2.grid(row=3, column=2, padx=(10, 10), pady=(5, 10))
    multi_line_graph_labels.append(om2)
    

def update_limiter(new_option, old_option, limit_menu, specify_string, limiter_string, data, limiter_menu):
    '''Update limiter options menu so it includes every x-axis option BUT the one selected'''
    limit_menu['menu'].delete(new_option.get())
    specify_string.set("None")
    change_options("None", limiter_string, data, limiter_menu)
    limit_menu['menu'].add_command(label=old_option.get(), command=tk._setit(specify_string, old_option.get(), lambda p: change_options(specify_string.get(), limiter_string, data, limiter_menu)))
    old_option.set(new_option.get())
    pass


def change_options(string, new_string, data, options_menu):
    '''Change the limiter options to new options'''
    # If there should be no options showing
    if string == "None":
        new_string.set("")
        options_menu['menu'].delete(0, 'end')
        options_menu['menu'].add_command(label="", command=tk._setit(new_string, ""))
        return
    
    # If there should be options for the given limiter
    options_menu['menu'].delete(0, 'end')
    for option in np.unique(data[string]):
        options_menu['menu'].add_command(label=option, command=tk._setit(new_string, option))
    new_string.set(np.unique(data[string])[0])


def remove_labels(labels):
    '''Remove all labels from the window'''
    for label in labels:
        label.grid_remove()


def back_to_main(curr_labels, main_labels):
    '''Remove old window elements and replace main menu elements'''
    remove_labels(curr_labels)
    for label in main_labels:
        label.grid()


if __name__ == "__main__":
    main()