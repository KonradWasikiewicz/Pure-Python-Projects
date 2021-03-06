""" window that comes up at the beginning where user selects the algo"""

import os
import tkinter as tk

def choose():
    master = tk.Tk(className=' Sorting Algos')      # setting up root and a window name
    master.geometry("350x100")                      # window size
    master.configure(background='white')
    variable = tk.StringVar(master)                 # create a tkinter variable

    base_path = os.path.dirname(__file__)           # setting up a relative path to the icon
    icon_path = os.path.join(base_path, "icon.ico")
    master.iconbitmap(icon_path)

    algos = ["Bubble Sort",
            "Merge Sort",
            "Quick Sort",
            "Selection Sort",
            "Insertion Sort",
            "Shell Sort",
            "Heap Sort",
            "Radix Sort",
            "Count Sort",
            "Bucket Sort"]


    text = tk.Text(master, height=1, width=50, padx=15, pady=10, font ='Calibri 14') # creating a text widget and configuring it
    text.tag_configure('tag-center', justify='center')
    text.insert('end', "Select your algorithm form the list below", 'tag-center')
    text.pack()

    variable.set("Click me!")

    drop_down = tk.OptionMenu(master, variable, *algos)     # creating a drop down list
    drop_down.config(font ='Calibri 14', bg='white')
    drop_down.pack()

    # on change dropdown value
    def change_dropdown(*args):
        global dropdown
        dropdown = variable.get()
        master.destroy()                # closing the window after choosing the algo

    # link function to change dropdown
    variable.trace('w', change_dropdown)
choose()
tk.mainloop()
