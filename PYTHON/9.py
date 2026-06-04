def greet_user():
    
    name = input("Enter your name: ")

    if not name.strip():
        return "Invalid input! Name cannot be empty."

    return f"Hello, {name}! Welcome."

result = greet_user()

print(result)