import tkinter as tk
from tkinter import ttk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        # Style configuration
        style = ttk.Style()
        style.theme_use('clam')
        
        # Variables
        self.current_number = tk.StringVar()
        self.current_number.set("0")
        self.stored_number = 0
        self.current_operation = None
        self.new_number = True
        
        self.create_widgets()
        
    def create_widgets(self):
        # Display
        display_frame = ttk.Frame(self.root)
        display_frame.pack(fill='x', padx=10, pady=10)
        
        self.display = ttk.Entry(display_frame, textvariable=self.current_number, 
                                font=('Arial', 20), justify='right', state='readonly')
        self.display.pack(fill='x')
        
        # Buttons frame
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Configure grid weights
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for i in range(4):
            buttons_frame.grid_columnconfigure(i, weight=1)
        
        # Button definitions
        buttons = [
            ('C', 0, 0, 1, 1), ('±', 0, 1, 1, 1), ('%', 0, 2, 1, 1), ('÷', 0, 3, 1, 1),
            ('7', 1, 0, 1, 1), ('8', 1, 1, 1, 1), ('9', 1, 2, 1, 1), ('×', 1, 3, 1, 1),
            ('4', 2, 0, 1, 1), ('5', 2, 1, 1, 1), ('6', 2, 2, 1, 1), ('-', 2, 3, 1, 1),
            ('1', 3, 0, 1, 1), ('2', 3, 1, 1, 1), ('3', 3, 2, 1, 1), ('+', 3, 3, 1, 1),
            ('0', 4, 0, 2, 1), ('.', 4, 2, 1, 1), ('=', 4, 3, 1, 1)
        ]
        
        # Create buttons
        for (text, row, col, rowspan, colspan) in buttons:
            button = ttk.Button(buttons_frame, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, 
                       padx=2, pady=2, sticky='nsew')
    
    def button_click(self, value):
        if value.isdigit() or value == '.':
            self.handle_number(value)
        elif value in ['+', '-', '×', '÷']:
            self.handle_operator(value)
        elif value == '=':
            self.calculate()
        elif value == 'C':
            self.clear()
        elif value == '±':
            self.toggle_sign()
        elif value == '%':
            self.percentage()
    
    def handle_number(self, number):
        if self.new_number:
            self.current_number.set(number)
            self.new_number = False
        else:
            if number == '.' and '.' in self.current_number.get():
                return
            current = self.current_number.get()
            if current == '0' and number != '.':
                self.current_number.set(number)
            else:
                self.current_number.set(current + number)
    
    def handle_operator(self, operator):
        if self.current_operation and not self.new_number:
            self.calculate()
        
        self.stored_number = float(self.current_number.get())
        self.current_operation = operator
        self.new_number = True
    
    def calculate(self):
        if self.current_operation is None:
            return
        
        current = float(self.current_number.get())
        
        if self.current_operation == '+':
            result = self.stored_number + current
        elif self.current_operation == '-':
            result = self.stored_number - current
        elif self.current_operation == '×':
            result = self.stored_number * current
        elif self.current_operation == '÷':
            if current == 0:
                self.current_number.set("Error")
                self.new_number = True
                return
            result = self.stored_number / current
        
        # Format result
        if result.is_integer():
            self.current_number.set(str(int(result)))
        else:
            self.current_number.set(str(result))
        
        self.current_operation = None
        self.new_number = True
    
    def clear(self):
        self.current_number.set("0")
        self.stored_number = 0
        self.current_operation = None
        self.new_number = True
    
    def toggle_sign(self):
        current = float(self.current_number.get())
        result = -current
        if result.is_integer():
            self.current_number.set(str(int(result)))
        else:
            self.current_number.set(str(result))
    
    def percentage(self):
        current = float(self.current_number.get())
        result = current / 100
        if result.is_integer():
            self.current_number.set(str(int(result)))
        else:
            self.current_number.set(str(result))

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()







