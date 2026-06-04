def add(a, b):
   
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        return "Invalid input! Both values must be numbers."


    result = a + b

    return result

output = add(5, 3)

print(f"Sum: {output}")