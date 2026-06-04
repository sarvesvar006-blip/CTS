import math

class CartItem:
    def __init__(self, name, price, quantity):
        self.name = name

        # validation
        self.price = price if price > 0 else 0
        self.quantity = quantity if quantity > 0 else 0

    def total_price(self):
        return self.price * self.quantity


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def calculate_total(self):
        return sum(item.total_price() for item in self.items)

    def print_receipt(self):
        print("\n----- RECEIPT -----")
        for item in self.items:
            print(f"{item.name} | {item.price} x {item.quantity} = {item.total_price()}")

        subtotal = self.calculate_total()
        gst = subtotal * 0.18
        total = subtotal + gst

        print("-------------------")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"GST (18%): {gst:.2f}")
        print(f"Total: {total:.2f}")


# ------------------ Demo ------------------

cart = ShoppingCart()

cart.add_item(CartItem("Milk", 50, 2))
cart.add_item(CartItem("Rice", 60, 5))
cart.add_item(CartItem("Sugar", 40, 3))

cart.remove_item("Sugar")

cart.print_receipt()