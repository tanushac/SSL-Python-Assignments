import sys
def add_two_numbers(num1, num2):
    """
    Adds two numbers and returns the result.

    Parameters:
    - num1 (int): The first number.
    - num2 (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return num1 + num2
if len(sys.argv) != 3:
    print("Usage: python script_name.py <number1> <number2>")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = add_two_numbers(num1, num2)
        print(f'The sum of {num1} and {num2} is: {result}')
    except ValueError:
        print("Please enter valid integers as command line arguments.")
