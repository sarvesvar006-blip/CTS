from math import *

def math_operations(num):
    if not isinstance(num, (int, float)):
        return "Invalid input! Please enter a number."
    if num < 0:
        return "Invalid input! Number must be non-negative."

    square_root = sqrt(num)
    power_value = pow(num, 2)
    circle_area = pi * (num ** 2)

    return (
        f"Square Root: {square_root:.2f}\n"
        f"Power (num^2): {power_value:.2f}\n"
        f"Circle Area (using radius=num): {circle_area:.2f}"
    )


number = 4

result = math_operations(number)
print(result)