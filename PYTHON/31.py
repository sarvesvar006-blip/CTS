def display_cart(cart):
    if not isinstance(cart, list) or len(cart) == 0:
        return "Invalid input! Cart must be a non-empty list."
    if not all(isinstance(item, (int, float)) for item in cart):
        return "Invalid data! All cart items must be numbers."

    return f"Shopping Cart Items: {cart}"


cart = [100, 250, 75]

result = display_cart(cart)
print(result)