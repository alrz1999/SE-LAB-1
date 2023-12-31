from enum import Enum
import math

class Calculator:
    class Operation(Enum):
        Add = 1,
        Subtract = 2,
        Multiply = 3,
        Divide = 4,
        Power = 5,
        Sqrt = 6,
        log  = 7,
        sin  = 8,
        cos  = 9

    @staticmethod
    def calculate(x, operation, y):
        if operation == "Add":
            print("Result:", Calculator.add(x, y))
        elif operation == "Subtract":
            print("Result:", Calculator.subtract(x, y))
        elif operation == "Multiply":
            print("Result:", Calculator.multiply(x, y))
        elif operation == "Divide":
            print("Result:", Calculator.divide(x, y))
        elif operation == "Power":
            print("Result:", Calculator.power(x, y))
        elif operation == "Sqrt":
            print("Result:", Calculator.sqrt(x))
        elif operation == "Log":
            print("Result:", Calculator.log(x))
        elif operation == "Sin":
            print("Result:", Calculator.sin(x)) 
        elif operation == "Cos":
            print("Result:", Calculator.cos(x))  
        else:
            print("Invalid choice")
            raise AttributeError

    @staticmethod
    def add(x, y):
        return x + y


    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x*y

    @staticmethod
    def divide(x, y):
        return x/y

    @staticmethod
    def power(x, y):
        return math.pow(x, y)

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)
    @staticmethod
    def log(x):
        return math.log10(x)
    @staticmethod
    def sin(x):
        return math.sin(x)
    @staticmethod
    def cos(x):
        return math.cos(x)

def get_input_operation():
    operations = ["Add", "Subtract", "Multiply", "Divide", "Power", "Sqrt","log","sin","cos"]

    print("Select operation:")
    for idx, operation in enumerate(operations):
        print(f"{idx+1}. {operation}")

    operation_index = int(input("Enter your choice (1/2/3/4/5/6/7/8/9): "))
    return operations[operation_index-1]

def get_input_numbers(operation):
    if operation == "Sqrt":
        num = float(input("Enter number: "))
        return num, None
    elif operation == "log":
        num = float(input("Enter number: "))
        return num, None
    elif operation == "sin":
        num = float(input("Enter number: "))
        return num, None
    elif operation == "cos":
        num = float(input("Enter number: "))
        return num, None   
    else:        
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2

if __name__ == "__main__":       
    operation = get_input_operation()
    num1, num2 = get_input_numbers(operation)
    Calculator.calculate(num1, operation, num2)
