from enum import Enum
import math

class Calculator:
    class Operation(Enum):
        Add = 1,
        Subtract = 2,
        Multiply = 3,
        Divide = 4
        Sqrt = 4


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
        elif operation == "Sqrt":
            print("Result:", Calculator.sqrt(x))
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
        pass

    @staticmethod
    def divide(x, y):
        pass

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)

def get_input_operation():
    operations = ["Add", "Subtract", "Multiply", "Divide", "Sqrt"]

    print("Select operation:")
    for idx, operation in enumerate(operations):
        print(f"{idx+1}. {operation}")

    operation_index = int(input("Enter your choice (1/2/3/4/5): "))
    return operations[operation_index-1]

def get_input_numbers(operation):
    if operation == "Sqrt":
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
