''' NAME: THEURI BONFACE KARUE, 
    REG NO: SCT211-0573/2022,
'''

def addition(x, y):
    return x + y


while True:
    print("Enter 'addition' for addition")


    user_input = input(": ")

    if user_input == "quit":
        break
    elif user_input in ("addition"):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if user_input == "addition":
            print("Result:", addition(num1, num2))
    else:
        print("Invalid input. Please enter a valid option.")
