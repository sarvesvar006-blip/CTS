def area(length, width):
    
    if not (isinstance(length, (int, float)) and isinstance(width, (int, float))):
        return "Invalid input! Length and width must be numbers."
    if length <= 0 or width <= 0:
        return "Invalid values! Length and width must be positive."

    
    result = length * width

    return result



output = area(5, 3)

print(f"Area of rectangle: {output}")