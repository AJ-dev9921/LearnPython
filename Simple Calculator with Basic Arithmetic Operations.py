# Prompt the user to input the first number
try:
    a = int(input("Enter the 1st Number: "))

    # Prompt the user to input the second number
    b = int(input("Enter the 2nd Number: "))

    # Prompt the user to specify the arithmetic operation
    d = input("Enter Action (+, -, *, /): ")
    
    # Perform addition if the action is '+'
    if d == "+":
        print(f"Answer is: {a + b}")
    
    # Perform subtraction if the action is '-'
    elif d == "-":
        print(f"Answer is: {a - b}")
    
    # Perform multiplication if the action is '*'
    elif d == "*":
        print(f"Answer is: {a * b}")
    
    # Perform division if the action is '/'
    elif d == "/":
        # Check if the divisor (b) is not zero to avoid division by zero error
        if b != 0:
            # Perform the division and format the result to 2 decimal places
            print(f"Answer is: {a / b:.2f}")
        else:
            # Print an error message if division by zero is attempted
            print("Division by zero is not possible.")
    
    # Handle invalid actions
    else:
        print("Invalid action input. Please enter one of +, -, *, /.")

# Handle cases where the input cannot be converted to an integer
except ValueError:
    print("Invalid input. Please enter numeric values for the numbers.")
