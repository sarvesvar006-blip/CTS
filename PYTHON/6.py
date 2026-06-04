def check_even_odd(number):
    
    if not isinstance(number, int):
        return "Invalid input! Please enter an integer."

    
    remainder = number % 2
    if remainder == 0:
        return "Even"
    else:
        return "Odd"

number = 17
result = check_even_odd(number)
print(f"Number {number} is {result}")