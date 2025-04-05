import tkinter as tk
from parser import Parser

class CalculatorLogic:
    def __init__(self):
        self.expression = ""
        
    def  add_input(self, value):
        self.expression += str(value)
    
    def clear(self):
        self.expression = ""
        
    def calculate(self):
        try:
            result = Parser(self.expression)
            self.expression = str(result)
            return result
        except Exception as e:
            self.expression = ""
            return "Error"
    