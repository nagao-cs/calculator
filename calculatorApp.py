from tkinter import *
from tkinter import ttk
from calculatorFrame import CalculatorFrame

class CalculatorApp(Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("300x200")
        
        frame = CalculatorFrame(self)
        frame.pack(expand=True, fill=BOTH)
        
if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()