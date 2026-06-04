def convert_kg_to_lbs():

    kg_input = input("Enter weight in kilograms: ")


    try:
        kg = float(kg_input)
        if kg <= 0:
            return "Invalid input! Weight must be positive."
    except ValueError:
        return "Invalid input! Please enter a valid number."

    lbs = kg * 2.20462

    return f"Weight in pounds: {lbs:.2f} lbs"
result = convert_kg_to_lbs()
print(result)