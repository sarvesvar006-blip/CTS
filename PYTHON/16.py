def print_numbers(count):
   
    if not isinstance(count, int) or count <= 0:
        return "Invalid input! Count must be a positive integer."

    for i in range(count):
        print(f"Number: {i + 1}")


count = 5

result = print_numbers(count)
if result:
    print(result)