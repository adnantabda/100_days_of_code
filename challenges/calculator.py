"""
Calculator that supports basic operations ( +, -, /, * ).
Project for Angela Wu's 100 days of code challenges.
Day # 10
"""

# Defining basic operations


def addition(n1, n2):
    return n1 + n2


def substraction(n1, n2):
    return n1 - n2


def multiplication(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


# Using operation symbols as the keys of a dict and the functions(w/o parenthesis) a value
operations = {
    "+": addition,
    "-": substraction,
    "*": multiplication,
    "/": division,
}


def calculator():
    """Basic operations with memory to store your previous results
    and keep calculating."""

    number_1 = float(input("Enter the first number: "))

    # Show operation symbols
    print("\n Operations")
    for symbol in operations:
        print(f"\t{symbol}")

    # Flag
    should_continue = True

    while should_continue:
        # Ask what operation to perform
        operation_symbol = input("Type the operation symbol: ")
        # Next number
        number_2 = float(input("\nEnter the next number: "))

        operation = operations[operation_symbol]
        result = operation(number_1, number_2)

        print(f"\n{number_1} {operation_symbol} {number_2} = {result}")

        print(f"\nDo you wish to continue calculating with {result}?")
        print("Enter 'y' to continue.")
        print("Enter 'n' to start again.")
        answer = input()

        if answer == 'y':
            number_1 = result

        elif answer == 'n':
            # Use function as a revursive function (keeps calling itself)
            calculator()
        else:
            should_continue = False


calculator()






