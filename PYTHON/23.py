import math

def calculate_circle_area(radius):
    if not isinstance(radius, (int, float)):
        return "Invalid input! Radius must be a number."
    if radius <= 0:
        return "Invalid radius! Must be greater than 0."

    area = math.pi * (radius ** 2)
    return f"Area of circle: {area:.2f}"


radius = 5

result = calculate_circle_area(radius)
print(result)