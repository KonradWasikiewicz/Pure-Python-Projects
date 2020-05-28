# https://www.youtube.com/watch?v=XhCfsuMyhXo

#dodac pasek na gorze w wyborem np Edit, View i tam np wybor layoutu i inne przełączniki
#zastanowic sie nad guzikami MC/MR/MS 
#dodac: przecinek, nawiasy oba, 1/x, logarytm
#jak wychodzi liczba calkowita to w int a nie float
# pomyslec jak zoptymalizowac te kazdorazowe definiowanie zmiennych globalnych 
#2+3*3 -> ma byc 11 a nie 9 

from tkinter import *

root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)

e = Entry(root, width = 55, borderwidth = 3, justify='right')    #zmodyfikowac wysokosc i dodac wyswietlanie działania w finalnej wersji 
e.grid(row = 0, column = 0, columnspan = 4, pady = 10, padx = 10)

#Defining functions
def button_click(number):
    e.insert(END, number)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)
    e.delete(0,END)

def button_substract():
    first_number = e.get()
    global f_num
    global math
    math = 'substraction'
    f_num = float(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_number)
    e.delete(0,END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    e.delete(0,END)

def button_sqrt():
    first_number = e.get()
    global f_num
    global math
    math = 'root'
    f_num = float(first_number)
    e.delete(0,END)

def button_point():
    if '.' not in str(e.get()):
        first_number = str(e.get())+ '.'
        e.delete(0,END)
        e.insert(END, first_number)
    else:
        pass


def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == 'addition':
        e.insert(0, f_num  + float(second_number))
    if math == 'substraction':
        e.insert(0, f_num  - float(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * float(second_number))
    if math == 'division':
        e.insert(0, f_num / float(second_number))
    if math == 'root':
        e.insert(0, f_num**(1/2))

def button_clear():
    e.delete(0, END)



#Defining buttons 

button_0 = Button(root, text = '0', padx = 20, pady = 10, command = lambda: button_click(0))
button_1 = Button(root, text = '1', padx = 20, pady = 10, command = lambda: button_click(1))
button_2 = Button(root, text = '2', padx = 20, pady = 10, command = lambda: button_click(2))
button_3 = Button(root, text = '3', padx = 20, pady = 10, command = lambda: button_click(3))
button_4 = Button(root, text = '4', padx = 20, pady = 10, command = lambda: button_click(4))
button_5 = Button(root, text = '5', padx = 20, pady = 10, command = lambda: button_click(5))
button_6 = Button(root, text = '6', padx = 20, pady = 10, command = lambda: button_click(6))
button_7 = Button(root, text = '7', padx = 20, pady = 10, command = lambda: button_click(7))
button_8 = Button(root, text = '8', padx = 20, pady = 10, command = lambda: button_click(8))
button_9 = Button(root, text = '9', padx = 20, pady = 10, command = lambda: button_click(9))

button_add = Button(root, text = '+', padx = 10, pady = 10, command = button_add)
button_substract = Button(root, text = '-', padx = 10, pady = 10, command = button_substract) 
button_multiply = Button(root, text = '*', padx = 10, pady = 10, command = button_multiply) 
button_divide = Button(root, text = '/', padx = 10, pady = 10, command = button_divide) 
button_point = Button(root, text = '.', padx = 20, pady = 10, command = button_point) 
button_sqrt = Button(root, text = '√', padx = 20, pady = 10, command = button_sqrt) 

button_equal = Button(root, text = '=', padx = 60, pady = 10, command = button_equal)
button_clear = Button(root, text = '\u232B', padx = 60, pady = 10, command = button_clear)


#Putting buttons on the screen 

button_0.grid(row = 4, column = 0, sticky="nsew")

button_1.grid(row = 3, column = 0, sticky="nsew")
button_2.grid(row = 3, column = 1, sticky="nsew")
button_3.grid(row = 3, column = 2, sticky="nsew")

button_4.grid(row = 2, column = 0, sticky="nsew")
button_5.grid(row = 2, column = 1, sticky="nsew")
button_6.grid(row = 2, column = 2, sticky="nsew")

button_7.grid(row = 1, column = 0, sticky="nsew")
button_8.grid(row = 1, column = 1, sticky="nsew")
button_9.grid(row = 1, column = 2, sticky="nsew")
 

button_add.grid(row = 1, column = 3, sticky="nsew")
button_substract.grid(row = 2, column = 3, sticky="nsew")
button_multiply.grid(row = 3, column = 3, sticky="nsew")
button_divide.grid(row = 4, column = 3, sticky="nsew")

button_point.grid(row = 4, column = 1, sticky="nsew")
button_sqrt.grid(row = 4, column = 2, sticky="nsew")

button_equal.grid(row = 5, column = 0, columnspan = 2, sticky="nsew")
button_clear.grid(row = 5, column = 2, columnspan = 2, sticky="nsew")

root.mainloop()
