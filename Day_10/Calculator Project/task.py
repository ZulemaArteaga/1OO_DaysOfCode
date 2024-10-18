"""The goal is to build a calculator program."""
import art

def add(n1, n2): return n1 + n2
def subtract (n1, n2): return n1 - n2
def multiply(n1, n2): return n1 * n2
def divide(n1, n2): return n1 / n2 if n2 != 0 else "Undefined (cannot divide by zero)"

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

def type_number():
    while True:
        try:
            number = float(input("Type a number: "))
            return number
        except ValueError:
            # Restart the loop if the typed input is not a number
            print("Invalid Option. Please enter a number.")
            continue

def calculator():
    print(art.logo)

    n1 = type_number()

    while True:
        operator_input = input('Type a mathematical operator (+, -, *, /): ')
        if operator_input not in ["+", "-", "*", "/"]:
            print("Invalid operator. Type '+', '-', '*' or '/'\n")
            continue  # Restart the loop if the operator is invalid

        n2 = type_number()

        result = operations[operator_input](n1, n2)
        # if the operator_input is +, then operations will return the add function.
        print(f"{n1} {operator_input} {n2} = {result}")

        play_again = input("Would you like to continue working with the previous result? \n"
                           "Type 'yes' to continue, or 'no' to exit: ").lower()

        if play_again == "no":
            print("Exiting the calculator.")
            break
        elif play_again == "yes":
            n1 = result
            print("Continuing with result:", result)
        else:
            print("Invalid Option. Exiting the calculator.")
            break

calculator()

