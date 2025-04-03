from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")
root.geometry("300x200")

label = ttk.Label(root)

def press_button(char):
    label.config(text=label.cget("text") + char)
def press_equal():
    try:
        result = eval(label.cget("text"))
        label.config(text=str(result))
    except Exception as e:
        label.config(text="Error")

botton_1 = ttk.Button(root, text="1", command=lambda: press_button("1"))
botton_1.grid(row=2, column=0)
botton_2 = ttk.Button(root, text="2", command=lambda: press_button("2"))
botton_2.grid(row=2, column=1)
botton_3 = ttk.Button(root, text="3", command=lambda: press_button("3"))
botton_3.grid(row=2, column=2)
botton_4 = ttk.Button(root, text="4", command=lambda: press_button("4"))
botton_4.grid(row=1, column=0)
botton_5 = ttk.Button(root, text="5", command=lambda: press_button("5"))
botton_5.grid(row=1, column=1)
botton_6 = ttk.Button(root, text="6", command=lambda: press_button("6"))
botton_6.grid(row=1, column=2)
botton_7 = ttk.Button(root, text="7", command=lambda: press_button("7"))
botton_7.grid(row=0, column=0)
botton_8 = ttk.Button(root, text="8", command=lambda: press_button("8"))
botton_8.grid(row=0, column=1)
botton_9 = ttk.Button(root, text="9", command=lambda: press_button("9"))
botton_9.grid(row=0, column=2)
botton_comma = ttk.Button(root, text=".", command=lambda: press_button("."))
botton_comma.grid(row=3, column=0)
botton_0 = ttk.Button(root, text="0", command=lambda: press_button("0"))
botton_0.grid(row=3, column=1)
botton_equal = ttk.Button(root, text="=", command=lambda: press_equal())
botton_equal.grid(row=3, column=2)
botton_plus = ttk.Button(root, text="+", command=lambda: press_button("+"))
botton_plus.grid(row=3, column=4)
botton_minus = ttk.Button(root, text="-", command=lambda: press_button("-"))
botton_minus.grid(row=2, column=4)
botton_multiply = ttk.Button(root, text="*", command=lambda: press_button("*"))
botton_multiply.grid(row=1, column=4)
botton_divide = ttk.Button(root, text="/", command=lambda: press_button("/"))
botton_divide.grid(row=0, column=4)

label.grid(row=4, column=0, columnspan=3)

root.mainloop()