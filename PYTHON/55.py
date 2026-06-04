import matplotlib.pyplot as plt

class Category:
    def __init__(self, name, limit):
        self.name = name
        self.limit = limit
        self.spent = 0

    def add_expense(self, amount):
        if amount <= 0:
            print("Invalid amount!")
            return

        self.spent += amount

        if self.spent > self.limit:
            print(f"⚠ Alert: {self.name} budget exceeded!")


class BudgetPlanner:
    def __init__(self):
        self.categories = {}

    def add_category(self, name, limit):
        self.categories[name] = Category(name, limit)

    def add_expense(self, name, amount):
        if name in self.categories:
            self.categories[name].add_expense(amount)
        else:
            print("Category not found!")

    def show_summary(self):
        print("\n--- BUDGET SUMMARY ---")
        for cat in self.categories.values():
            print(f"{cat.name}: Spent {cat.spent} / Limit {cat.limit}")

    def plot_budget(self):
        labels = []
        spent = []

        for cat in self.categories.values():
            labels.append(cat.name)
            spent.append(cat.spent)

        plt.pie(spent, labels=labels, autopct='%1.1f%%')
        plt.title("Monthly Budget Distribution")
        plt.show()


# ---------------- DEMO ----------------
planner = BudgetPlanner()

planner.add_category("Food", 5000)
planner.add_category("Transport", 2000)
planner.add_category("Shopping", 3000)

# input loop
for i in range(5):
    cat = input("Enter category: ")
    amt = float(input("Enter expense: "))
    planner.add_expense(cat, amt)

planner.show_summary()
planner.plot_budget()