# main.py
# Explore water usage by industries in Michigan

#Imports
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
    #Load data
    data = np.genfromtxt(os.path.join(ROOT, DATA), delimiter=",", skip_header=1, usecols=NUM_COLS, dtype=(str, np.int64, np.int64, np.int64, np.int64, str, int))

    #Create main window
    root = tk.Tk()

    root.title("Michigan Water Usage From 2013 to 2022")
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    main_labels = []
    main_labels.append(tk.Label(text="Michigan Water Usage From 2013 to 2022", font=('bold', 16, "underline")).grid(row=1, column=1, padx=(10, 10), pady=(5, 10)))
    main_labels.append(tk.Button(text="Bar Graph by County", command=lambda: bar_graph_county(data)).grid(row=2, column=1))

    root.mainloop()


def bar_graph_county(data):
    print("Working Button")
    pass


if __name__ == "__main__":
    main()