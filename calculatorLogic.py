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
            print(self.expression)  # Debugging line to check the expression before parsing
            parser = Parser(self.expression)
            parser.parse(self.expression)
            result = parser.evaluate(parser._output)
            self.expression = result
            return result
        except Exception as e:
            self.expression = ""
            return "Error"
    