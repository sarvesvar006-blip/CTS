def calculate(a, b, op):
    try:
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return "Error: Cannot divide by zero!"
            return a / b
        else:
            return "Invalid operator! Use +, -, *, /"
    except Exception as e:
        return f"Unexpected error: {e}"


try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    op = input("Enter operator (+, -, *, /): ")

    result = calculate(a, b, op)
    print(f"Result: {result}")

except ValueError:
    print("Error: Please enter valid numeric values.")