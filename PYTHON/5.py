def display_coordinates(coords):
    
    if not isinstance(coords, tuple) or len(coords) != 2:
        return "Invalid input! Coordinates must be a tuple of two values."

    x, y = coords  

    if not (isinstance(x, (int, float)) and isinstance(y, (int, float))):
        return "Invalid coordinates! Must be numbers."

    
    return f"Coordinates: (X = {x:.2f}, Y = {y:.2f})"



point = (10.5, 20)


result = display_coordinates(point)


print(result)