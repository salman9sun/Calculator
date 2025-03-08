from tkinter import *

def button_press(num):
    global equation_text
    num_str = str(num)
    if equation_text and equation_text[-1] in "+-×÷" and num_str in "+-×÷":
        return
    if num_str == "^":
        equation_text = equation_text + "**"
    else:
        equation_text = equation_text + num_str
    equation_label.set(equation_text.replace("**", "^"))

def equal():
    global equation_text
    try:
        equation_text_for_eval = equation_text.replace('÷', '/').replace('×', '*').replace("^", "**")
        total = str(eval(equation_text_for_eval))
        equation_label.set(total)
        equation_text = total
    except (SyntaxError, NameError):
        equation_label.set("Error")
        equation_text = ""
    except (ZeroDivisionError):
        equation_label.set("Can't divide by zero!")
        equation_text = ""

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

def backspace():
    global equation_text
    equation_text = equation_text[:-1]
    equation_label.set(equation_text.replace("**", "^"))

def square_root():
    global equation_text
    equation_text = f"({equation_text})**0.5"
    equation_label.set(equation_text.replace("**", "^"))
    equal()

def percentage():
    button_press('%')

def power():
    button_press('^')

def key_press(event):
    key = event.char
    if key in "0123456789+-*/().÷×":
        button_press(key)
    elif key == '%':
        percentage()
    elif event.keysym == "Return":
        equal()
    elif event.keysym == "BackSpace":
        backspace()
    elif event.keysym == "Escape":
        clear()

window = Tk()
window.title("Calculator")
window.configure(bg="#121212")
window.geometry("450x750")
window.resizable(False, False)
window.bind("<Key>", key_press)

equation_text = ""
equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('Segoe UI Variable', 30, 'bold'),
              bg="#1E1E1E", fg="white", width=20, height=2, anchor='e', bd=0, relief="flat")
label.pack(pady=20, padx=15)

frame = Frame(window, bg="#121212")
frame.pack()

button_width = 6
button_height = 3
button_margin = 10
button_params = {'font': ('Segoe UI Variable', 22, 'bold'), 'width': button_width, 'height': button_height, 'bd': 0, 'bg': '#333333', 'fg': 'white', 'relief': 'flat'}
button_params_yellow = {'font': ('Segoe UI Variable', 22, 'bold'), 'width': button_width, 'height': button_height, 'bd': 0, 'bg': '#F1C40F', 'fg': 'black', 'relief': 'flat'}
button_params_red = {**button_params, 'bg': '#E74C3C'}
button_params_orange = {**button_params, 'bg': '#FF8C00'}
button_params_white = {**button_params, 'bg': '#F39C12', 'fg': 'white'}

buttons = [
    ('√', square_root), ('^', power), ('C', clear), ('⌫', backspace),
    ('(', lambda: button_press('(')), (')', lambda: button_press(')')), ('%', percentage), ('÷', lambda: button_press('÷')),
    ('7', lambda: button_press('7')), ('8', lambda: button_press('8')), ('9', lambda: button_press('9')), ('×', lambda: button_press('×')),
    ('4', lambda: button_press('4')), ('5', lambda: button_press('5')), ('6', lambda: button_press('6')), ('-', lambda: button_press('-')),
    ('1', lambda: button_press('1')), ('2', lambda: button_press('2')), ('3', lambda: button_press('3')), ('+', lambda: button_press('+')),
    ('00', lambda: button_press('00')), ('0', lambda: button_press('0')), ('.', lambda: button_press('.')), ('=', equal),
]

for i, (text, cmd) in enumerate(buttons):
    row = i // 4
    col = i % 4
    button_style = button_params if text not in "+-×÷=" else button_params_white if text != "=" else button_params_orange
    if text in ["C", "⌫"]:
        button_style = button_params_red
    btn = Button(frame, text=text, command=cmd, **button_style)
    btn.grid(row=row, column=col, padx=button_margin, pady=button_margin)

for i in range(6):
    frame.rowconfigure(i, weight=1)
for i in range(4):
    frame.columnconfigure(i, weight=1)

window.mainloop()
