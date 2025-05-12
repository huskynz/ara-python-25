class Calculator:
    """A calculator class that performs operations on two numbers."""
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num1 - self.num2
    
    def multiply(self):
        return self.num1 * self.num2
    
    def divide(self):
        return round(self.num1 / self.num2, 3)
    



calc_1 = Calculator(2, 3)

print(calc_1.add())
print(calc_1.subtract())
print(calc_1.divide())
print(calc_1.multiply())
