import tkinter as tk
from calculatorLogic import CalculatorLogic

class CalculatorFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.logic = CalculatorLogic()
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self, text="", anchor="e", bg="white", font=("Arial", 24))
        self.label.grid(row=0, column=0, columnspan=4, sticky="nsew")
        
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self, text=text, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, sticky="nsew")
        
        for i in range(5):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)
            
    def on_button_click(self, value):
        if value == '=':
            result = self.logic.calculate()
            self.label.config(text=result)
        elif value == 'C':
            self.logic.clear()
            self.label.config(text="")
        else:
            self.logic.add_input(value)
            self.label.config(text=self.logic.expression)
        