import os

def clear():
    os.system('clear')
    
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
    }

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    continue_math = True

    while continue_math:
        op_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        math_stuff = operations[op_symbol]
        answer = math_stuff(num1, num2)

        print(f"{num1} {op_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == "y":
            num1 = answer
        else:
            continue_math = False
            clear()
            calculator()
calculator()