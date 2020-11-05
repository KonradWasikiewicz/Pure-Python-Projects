''' button ok, umiejscowienie return, tak zeby sie komunikowaly

caption

https://stackoverflow.com/questions/45441885/how-can-i-create-a-dropdown-menu-from-a-list-in-tkinter

przemyslec czy to koniecznie musi byc w funkcji

chyba trzeba to w while loop, zeby click me nie zaciagalo jako odpowidz
'''

import os
import tkinter as tk

# def check():
#     run = True
#     while run:
#         if variable.get() != "Click me!":
#             print(variable.get())
#             run = False
#         else:
#             continue


def choose():
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

    master = tk.Tk(className=' Sorting Algos')      # setting up root and a window name
    master.geometry("350x100")                      # window size
    master.configure(background='white')

    BASE_PATH = os.path.dirname(__file__)           # setting up a relative path to the icon
    ICON_PATH = os.path.join(BASE_PATH, "icon.ico")
    master.iconbitmap(ICON_PATH)

    text = tk.Text(master, height=1, width=50, padx=15, pady=10, font ='Calibri 14') # creating a text widget and configuring it
    text.tag_configure('tag-center', justify='center')
    text.insert('end', "Select your algorithm form the list below", 'tag-center')
    text.pack()

    variable = tk.StringVar(master)
    variable.set("Click me!")

    drop_down = tk.OptionMenu(master, variable, *algos)     # creating a drop down list
    drop_down.config(font ='Calibri 14', bg='white')
    drop_down.pack()

    # check()

    tk.mainloop()



choose()
