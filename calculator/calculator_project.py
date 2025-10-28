from calculator_art import logo

print(logo)

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def division(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        print("Dijeljenje sa 0 nije moguce!")


operations = {"+": add, "-": substract, "*": multiply, "/": division}

def calculator():
    number1 = float(input("Enter first number:\n"))
    should_accumulate = True
    while should_accumulate:
        operation= input("Enter type of mathematical operation: \n + \n - \n * \n / \n")
        number2 = float(input("Enter the second number:\n"))

        result = operations[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {result}")

        should_continue = input("Do you want to continue working with previous result. Type 'y' or 'n'.").lower()

        if should_continue == 'y':
            number1 = result
        else:
            should_accumulate = False
            print("\n"*20)
            calculator()

calculator()

