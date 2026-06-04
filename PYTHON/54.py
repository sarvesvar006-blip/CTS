class Product:
    def __init__(self, product_id, name, stock):
        self.product_id = product_id
        self.name = name
        self.stock = stock

    def __str__(self):
        return f"{self.product_id} | {self.name} | Stock: {self.stock}"


class Perishable(Product):
    def __init__(self, product_id, name, stock, expiry_date):
        super().__init__(product_id, name, stock)
        self.expiry_date = expiry_date


class Electronics(Product):
    def __init__(self, product_id, name, stock, warranty_years):
        super().__init__(product_id, name, stock)
        self.warranty_years = warranty_years


class InventoryManager:
    def __init__(self):
        self.inventory = {}   # product_id -> product object
        self.low_stock_alerts = set()

    def add_product(self, product):
        self.inventory[product.product_id] = product

    def update_stock(self, product_id, stock):
        if product_id in self.inventory:
            self.inventory[product_id].stock = stock
        else:
            print("Product not found!")

    def check_low_stock(self, threshold=5):
        self.low_stock_alerts.clear()

        for pid, product in self.inventory.items():
            if product.stock <= threshold:
                self.low_stock_alerts.add(pid)

    def show_inventory(self):
        print("\n--- INVENTORY SUMMARY ---")
        for product in self.inventory.values():
            print(product)

        print("\n--- LOW STOCK ALERTS ---")
        if not self.low_stock_alerts:
            print("No low stock items!")
        else:
            for pid in self.low_stock_alerts:
                print(self.inventory[pid])


# ---------------- Demo ----------------
manager = InventoryManager()

manager.add_product(Perishable("P101", "Milk", 3, "2026-06-10"))
manager.add_product(Electronics("E201", "Laptop", 10, 2))
manager.add_product(Perishable("P102", "Bread", 2, "2026-06-05"))
manager.add_product(Electronics("E202", "Phone", 4, 1))

manager.check_low_stock(threshold=5)
manager.show_inventory()