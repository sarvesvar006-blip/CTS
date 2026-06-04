def display_coordinates(coords):
    if not isinstance(coords, tuple) or len(coords) != 2:
        return "Invalid input! Coordinates must be a tuple of two values."

    x, y = coords

    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "Invalid coordinates! Values must be numbers."

    return f"Coordinates: (X = {x}, Y = {y})"


coordinates = (10.5, 20)

result = display_coordinates(coordinates)
print(result)