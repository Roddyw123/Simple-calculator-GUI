from tkinter import *

root = Tk()
root.title("Basic calculator")

root.geometry('354x400')
#screen_height = root.winfo_height()
#screen_length = root.winfo_length()

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def button_clear():
    e.delete(0, END)

def button_addition():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = float(first_number)
    e.delete(0, END)

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = float(first_number)
    e.delete(0, END)

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = float(first_number)
    e.delete(0, END)

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = float(first_number)
    e.delete(0, END)

def button_floating(float):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(float))

def button_squareroot():
    first_number = e.get()
    global f_num
    global math
    math = "sqrt"
    f_num = float(first_number)

def button_exponent():
    first_number = e.get()
    global f_num
    global math
    math = "exponent"
    f_num = float(first_number)
    e.delete(0, END)


def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + float(second_number))

    if math == "subtraction":
        e.insert(0, f_num - float(second_number))

    if math == "multiplication":
        e.insert(0, f_num * float(second_number))

    if math == "division":
        e.insert(0, f_num / float(second_number))

    if math == "sqrt":
        e.insert(0, f_num ** 0.5)

    if math == "exponent":
        e.insert(0, f_num ** float(second_number))



button_0 = Button(root, text="0", padx=40, pady=10, command=lambda: button_add(0))
button_1 = Button(root, text="1", padx=40, pady=10, command=lambda: button_add(1))
button_2 = Button(root, text="2", padx=40, pady=10, command=lambda: button_add(2))
button_3 = Button(root, text="3", padx=40, pady=10, command=lambda: button_add(3))
button_4 = Button(root, text="4", padx=40, pady=10, command=lambda: button_add(4))
button_5 = Button(root, text="5", padx=40, pady=10, command=lambda: button_add(5))
button_6 = Button(root, text="6", padx=40, pady=10, command=lambda: button_add(6))
button_7 = Button(root, text="7", padx=40, pady=10, command=lambda: button_add(7))
button_8 = Button(root, text="8", padx=40, pady=10, command=lambda: button_add(8))
button_9 = Button(root, text="9", padx=40, pady=10, command=lambda: button_add(9))
button_addition = Button(root, text="+",padx=40, pady=10, command=button_addition)
button_equal = Button(root, text="=", padx=98, pady=10, command=button_equal)
button_clear = Button(root, text="Clear", padx=87.5, pady=10, command=button_clear)

button_subtract = Button(root, text="-",padx=41, pady=10, command=button_subtract)
button_multiply = Button(root, text="*",padx=41., pady=10, command=button_multiply)
button_divide = Button(root, text="/",padx=41, pady=10, command=button_divide)
button_float = Button(root, text=".",padx=42, pady=10, command=lambda: button_floating("."))
button_sqrt = Button(root, text="sqrt", padx=32, pady=10, command=button_squareroot)
button_exponent = Button(root, text="^", padx=40.5, pady=10, command=button_exponent)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)
button_addition.grid(row=5, column=0)
button_clear.grid(row=4, column=1, columnspan=2)
button_equal.grid(row=5, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

button_float.grid(row=7, column=0)
button_sqrt.grid(row=7, column=1)
button_exponent.grid(row=7, column=2)

root.resizable(False, False)

root.mainloop()