def check_even_odd(num):
    if not isinstance(num, int):
        return "Invalid input! Please enter an integer."


    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = 8
result = check_even_odd(num)
print(f"Number {num} is {result}")