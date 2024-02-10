def get_number(prompt):
    return float(input(prompt))

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero."

def calculator():
    x_value = get_number("Enter the first number: ")
    y_value = get_number("Enter the second number: ")

    operation = input("Please choose your operation +, -, *, /: ")

    if operation == "+":
        print(add(x_value, y_value))
    elif operation == "-":
        print(subtract(x_value, y_value))
    elif operation == "*":
        print(multiply(x_value, y_value))
    elif operation == "/":
        print(divide(x_value, y_value))
    else:
        print("Invalid operation. Please enter +, -, *, /")

# Call the calculator function
calculator()
