def get_next_age():
   
    age_input = input("Enter your age: ")
    if not age_input.isdigit():
        return "Invalid input! Please enter a valid number."

    age = int(age_input)

    next_age = age + 1
    return f"Next year you'll be {next_age}"

result = get_next_age()
print(result)