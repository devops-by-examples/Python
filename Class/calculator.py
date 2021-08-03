class calculator:
    def __init__(self, type, num1, num2):
        self.type = type
        self.num1 = num1
        self.num2 = num2
    
    def calculation(self):
        if self.type == "addition":
            return self.num1 + self.num2
        if self.type == "subtraction":
            return self.num1 - self.num2
        if self.type == "multiplication":
            return self.num1 * self.num2
        if self.type == "division":
            return self.num1 // self.num2

print("Addition of numbers")            
obj = calculator("addition", 8, 4)
out = obj.calculation()
print(out)

print("Subtraction of numbers")            
obj = calculator("subtraction", 8, 4)
out = obj.calculation()
print(out)

print("Multiplication of numbers")            
obj = calculator("multiplication", 8, 4)
out = obj.calculation()
print(out)

print("Division of numbers")            
obj = calculator("division", 8, 4)
out = obj.calculation()
print(out)
