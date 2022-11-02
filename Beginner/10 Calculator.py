logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def calculation(n1, n2, operation_type):
    calculations_dict = {"+": n1 + n2, "-": n1 - n2, "*": n1 * n2, "/": n1 / n2}
    result = calculations_dict[operation_type]
    return result

def calculator():
    print(logo)
    first_number = float(input("What's the first number?: "))
    print("""
        +
        -
        *
        /
        """)

    continue_calculating = True
    while continue_calculating:
        operation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = calculation(first_number, second_number, operation)
        print(f"{first_number} {operation} {second_number} = {result}")

        continue_input = input(f"Type 'y' to continue calculating with {result}, or type 'n' to restart: ")
        if continue_input == "y":
            first_number = result
        else:
            continue_calculating = False
            calculator()

calculator()

