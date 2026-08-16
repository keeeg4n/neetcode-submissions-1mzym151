import math

class AreaCalc:
    def calculate(self, length: int, width: int = 0):
        if width != 0:
            return length * width

        return round(math.pi * (length ** 2), 2)
    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
