class calculator:
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def calculate(self, op):
        if op=='add':
            return self.a+self.b
        elif op=='sub':
            return self.a-self.b
        elif op=='mul':
            return self.a*self.b
        elif op=='div':
            if self.b==0:
                return "Error: Division by zero"
            return self.a/self.b
        else:
            return "Invalid operation"

a=float(input("Enter first no:"))
b=float(input("Enter second no:"))
op=input("Enter operation (add, sub, mul, div):")
c1=calculator(a, b)
print("Result:", c1.calculate(op))
