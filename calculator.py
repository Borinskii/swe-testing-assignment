class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        #sum
        return a + b

    def subtract(self, a, b):
        #difference
        return a - b

    def multiply(self, a, b):
        #multiplication
        return a * b

    def divide(self, a, b):
        #division, with error handling (division by zero)
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    def clear(self):
        #clear the result
        self.result = 0
