class Calculator:
    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y

    def clear_memory(self):
        self.memory = 0

    def store_to_memory(self, value):
        self.memory = value

    def recall_from_memory(self):
        return self.memory


# Usage
calc = Calculator()
while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'clear' to reset the result")
    print("Enter 'quit' to end the program")

    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input == "clear":
        calc.clear_memory()
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if user_input == "add":
            result = calc.add(num1, num2)
        elif user_input == "subtract":
            result = calc.subtract(num1, num2)
        elif user_input == "multiply":
            result = calc.multiply(num1, num2)
        elif user_input == "divide":
            result = calc.divide(num1, num2)
        print("Result:", result)
    else:
        print("Unknown input")
