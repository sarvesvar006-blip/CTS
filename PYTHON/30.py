def safe_division(a, b):
    try:
        result = a / b
        return f"Result: {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"


# Example values
num1 = 10
num2 = 0

# Function call
output = safe_division(num1, num2)

# Print result
print(output)