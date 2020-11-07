from tkinter import *
from math import *

root = Tk()
root.title('Calculator')
root.resizable(width=False, height=False)

#Creating main box
e = Entry(root, width = 40, font = 'Calibri 12', justify = 'right')
e.grid(row = 1, column = 0, columnspan = 4, pady = 10, padx = 10)

#Defining functions
def button_click(number):
    e.insert(END, number)

def button_reciprocal():
    first_number = e.get()
    f_num = float(first_number)
    e.delete(0,END)
    e.insert(0, 1/f_num)

def button_log():
    first_number = e.get()
    global f_num
    global math
    math = 'log'
    f_num = float(first_number)
    e.delete(0,END)

def button_sign_change():
    first_number = e.get()
    f_num = float(first_number)
    e.delete(0,END)
    e.insert(0, f_num*(-1))

def button_clear():
    e.delete(0, END)

def button_sqrt():
    first_number = e.get()
    global f_num
    global math
    math = 'root'
    f_num = float(first_number)
    e.delete(0,END)

def button_exponentiation():
    first_number = e.get()
    global f_num
    global math
    math = 'exponentiation'
    f_num = float(first_number)
    e.delete(0,END)

def button_percentage():
    first_number = e.get()
    f_num = float(first_number)
    e.delete(0,END)
    e.insert(END, float(f_num/100))

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = 'division'
    f_num = float(first_number)
    e.delete(0,END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = 'multiplication'
    f_num = float(first_number)
    e.delete(0,END)

def button_substract():
    first_number = e.get()
    global f_num
    global math
    math = 'substraction'
    f_num = float(first_number)
    e.delete(0,END)

def button_add():
    first_number = e.get()
    global f_num
    global math
    math = 'addition'
    f_num = float(first_number)
    e.delete(0,END)

def button_equal():
    second_number = e.get()
    e.delete(0,END)
    if math == 'log':
        e.insert(0,log(f_num, float(second_number)))
    if math == 'root':
        e.insert(0, f_num**(1/2))
    if math == 'exponentiation':
        e.insert(0, f_num ** float(second_number))
    if math == 'division':
        e.insert(0, f_num / float(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * float(second_number))
    if math == 'addition':
        e.insert(0, f_num  + float(second_number))
    if math == 'substraction':
        e.insert(0, f_num  - float(second_number))

def button_point():
    if '.' not in str(e.get()):
        first_number = str(e.get())+ '.'
        e.delete(0,END)
        e.insert(END, first_number)
    else:
        pass

#Defining buttons

button_0 = Button(root, text = '0', padx = 15, pady = 10, command = lambda: button_click(0))
button_1 = Button(root, text = '1', padx = 15, pady = 10, command = lambda: button_click(1))
button_2 = Button(root, text = '2', padx = 15, pady = 10, command = lambda: button_click(2))
button_3 = Button(root, text = '3', padx = 15, pady = 10, command = lambda: button_click(3))
button_4 = Button(root, text = '4', padx = 15, pady = 10, command = lambda: button_click(4))
button_5 = Button(root, text = '5', padx = 15, pady = 10, command = lambda: button_click(5))
button_6 = Button(root, text = '6', padx = 15, pady = 10, command = lambda: button_click(6))
button_7 = Button(root, text = '7', padx = 15, pady = 10, command = lambda: button_click(7))
button_8 = Button(root, text = '8', padx = 15, pady = 10, command = lambda: button_click(8))
button_9 = Button(root, text = '9', padx = 15, pady = 10, command = lambda: button_click(9))

button_point = Button(root, text = '.', padx = 15, pady = 10, command = button_point)
button_equal = Button(root, text = '=', padx = 30, pady = 10, command = button_equal)
button_add = Button(root, text = '+', padx = 15, pady = 10, command = button_add)
button_substract = Button(root, text = '-', padx = 15, pady = 10, command = button_substract)
button_multiply = Button(root, text = '*', padx = 15, pady = 10, command = button_multiply)
button_divide = Button(root, text = '/', padx = 15, pady = 10, command = button_divide)
button_sqrt = Button(root, text = '√', padx = 15, pady = 10, command = button_sqrt)
button_exponentiation = Button(root, text = 'y^x', padx = 15, pady = 10, command = button_exponentiation)
button_percentage = Button(root, text = '%', padx = 15, pady = 10, command = button_percentage)
button_log = Button(root, text = 'log', padx = 15, pady = 10, command = button_log)
button_reciprocal = Button(root, text = '1/x', padx = 15, pady = 10, command = button_reciprocal)
button_sign_change = Button(root, text = '\u00B1', padx = 15, pady = 10, command = button_sign_change)
button_clear = Button(root, text = '\u232B', padx = 15, pady = 10, command = button_clear)

#Putting buttons on the screen

button_0.grid(row = 8, column = 0, sticky = 'nsew')
button_point.grid(row = 8, column = 1, sticky = 'nsew')
button_equal.grid(row = 8, column = 2, columnspan = 2, sticky = 'nsew')

button_1.grid(row = 7, column = 0, sticky = 'nsew')
button_2.grid(row = 7, column = 1, sticky = 'nsew')
button_3.grid(row = 7, column = 2, sticky = 'nsew')
button_add.grid(row = 7, column = 3, sticky = 'nsew')

button_4.grid(row = 6, column = 0, sticky = 'nsew')
button_5.grid(row = 6, column = 1, sticky = 'nsew')
button_6.grid(row = 6, column = 2, sticky = 'nsew')
button_substract.grid(row = 6, column = 3, sticky = 'nsew')

button_7.grid(row = 5, column = 0, sticky = 'nsew')
button_8.grid(row = 5, column = 1, sticky = 'nsew')
button_9.grid(row = 5, column = 2, sticky = 'nsew')
button_multiply.grid(row = 5, column = 3, sticky = 'nsew')

button_sqrt.grid(row = 4, column = 0, sticky = 'nsew')
button_exponentiation.grid(row = 4, column = 1, sticky = 'nsew')
button_percentage.grid(row = 4, column = 2, sticky = 'nsew')
button_divide.grid(row = 4, column = 3, sticky = 'nsew')

button_reciprocal.grid(row = 3, column = 0, sticky = 'nsew')
button_log.grid(row = 3, column = 1, sticky = 'nsew')
button_sign_change.grid(row = 3, column = 2, sticky = 'nsew')
button_clear.grid(row = 3, column = 3, sticky = 'nsew')

root.mainloop()
