def add_expense(expenses, amount):
    if not isinstance(expenses, list):
        return "Invalid input! Expenses must be a list."
    if not isinstance(amount, (int, float)) or amount <= 0:
        return "Invalid expense amount!"

    expenses.append(amount)
    return f"Updated Expenses: {expenses}"


expenses = [200, 450, 300]

result = add_expense(expenses, 150)
print(result)