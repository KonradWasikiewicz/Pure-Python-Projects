import os
import tkinter as tk


# setting up a relative path for the icon
BASE_PATH = os.path.dirname(__file__)
ICON_PATH = os.path.join(BASE_PATH, "icon.png")


def choose_algo():
    ALGOS = ["Bubble Sort",
            "Merge Sort",
            "Quick Sort",
            "Selection Sort",
            "Insertion Sort",
            "Shell Sort",
            "Heap Sort",
            "Radix Sort",
            "Count Sort",
            "Bucket Sort"]

    master = tk.Tk()
    variable = tk.StringVar(master)
    w = tk.OptionMenu(master, variable, *ALGOS)
    master.iconbitmap(ICON_PATH)
    w.pack()
    tk.mainloop()

choose_algo()