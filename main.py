from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Simple Calculator")

label = ttk.Label(root, text="Enter a number:")
entry = ttk.Entry(root)
botton = ttk.Button(root, text="Submit")

label.pack()
entry.pack()
botton.pack()

root.mainloop()