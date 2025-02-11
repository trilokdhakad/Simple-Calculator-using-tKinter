
from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    result_label.config(text='')

def get_operator(op):
    global first_number, operator
    first_number = float(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number, second_number, operator
    second_number = float(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(round(first_number / second_number, 2)))

def create_button(text, row, col, command):
    btn = Button(root, text=text, bg='#00a65a', fg='white', width=5, height=2, command=command)
    btn.grid(row=row, column=col, sticky='nsew')
    btn.config(font=('verdana', 14))
    return btn

root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0, 0)
root.configure(background='black')

# Configure grid weights for resizing
for i in range(5):  # 5 rows
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # 4 columns
    root.grid_columnconfigure(j, weight=1)

# Result display label
result_label = Label(root, text='', bg='black', fg='white', anchor='e')
result_label.grid(row=0, column=0, columnspan=4, pady=(50, 25), sticky='nsew')
result_label.config(font=('verdana', 30, 'bold'))

# Buttons
create_button('7', 1, 0, lambda: get_digit(7))
create_button('8', 1, 1, lambda: get_digit(8))
create_button('9', 1, 2, lambda: get_digit(9))
create_button('+', 1, 3, lambda: get_operator('+'))

create_button('4', 2, 0, lambda: get_digit(4))
create_button('5', 2, 1, lambda: get_digit(5))
create_button('6', 2, 2, lambda: get_digit(6))
create_button('-', 2, 3, lambda: get_operator('-'))

create_button('1', 3, 0, lambda: get_digit(1))
create_button('2', 3, 1, lambda: get_digit(2))
create_button('3', 3, 2, lambda: get_digit(3))
create_button('*', 3, 3, lambda: get_operator('*'))

create_button('C', 4, 0, clear)
create_button('0', 4, 1, lambda: get_digit(0))
create_button('=', 4, 2, get_result)
create_button('/', 4, 3, lambda: get_operator('/'))

root.mainloop()
