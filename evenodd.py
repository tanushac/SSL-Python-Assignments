"""This is a python program to check if the given number is even or odd
Tanusha Choudhary
0801IT221131"""
def check(number):
    """
    Checks if a given number is even or odd.
    Parameters:
    - number (int): The number to be checked.
    Returns:
    str: 'Even' if the number is even, 'Odd' otherwise.
    """
    if number % 2 == 0:
        return 'Even'
    else:
        return 'Odd'
x = int(input("Enter a number: "))
result = check(x)
print('The number',x, 'is' ,result,'.')
