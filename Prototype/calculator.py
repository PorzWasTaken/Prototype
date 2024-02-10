def get_number(prompt):
    return float(input(prompt))


def add(x, y):
    return x + y

def minus(x, y):
    return x - y

def mutiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return("You can't divide by zero")


def calculator():
    x_value = get_number("Please enter your first number: ")
    y_value = get_number("Please enter your second number: ")
    operation(x_value, y_value)

def operation (x_value, y_value):
    operation = input("Please choose your operation +, -, *, / ")

    if operation == ("+"):
        print(add(x_value, y_value))
    elif operation == ("-"):
        print(minus(x_value, y_value))
    elif operation == ("*"):
        print(mutiply(x_value, y_value))   
    elif operation == ("/"):
        print(divide(x_value, y_value))
    else:
        print("No way you messed this up bro")

calculator()
            


