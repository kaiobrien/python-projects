#def format_name(f_name, l_name):
#    if f_name == "" or l_name == "":
#        return "No valid inputs provided."
#    full_name = f_name + " " + l_name
#    return full_name.title()
    
#print(format_name(input("What is your first name?\n"), input("What is your last name?\n")))
from art import logo


def add(n1,n2):
    return n1 + n2
def subtract(n1,n2):
    return n1 - n2
def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract, 
    "*": multiply, 
    "/": divide
    }
""" Putting everything into the function calculator allows this to be repeatable. 
    Recursion: calling a function within itself e.g. calling calculator() within calculator()
    Also calling the calculator after setting should_continue to False starts the calculator app from the 
    beginning instead of just exiting the app. 
"""
def calculator():
    print(logo)
    for symbol in operations:
        print(symbol)
    num1 = float(input("What's the first number:\n"))
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation:\n")
        num2 = float(input("What's the next number:\n"))
        calculation_symbol = operations[operation_symbol]
        answer = round(calculation_symbol(num1, num2), 3)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        continue_calc = input(f"Do you want to continue calculating with {answer}? Type y or n to start a new calculation \n")
        if continue_calc == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()