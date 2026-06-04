import csv
from datetime import datetime

def process_expenses(file_name):
    try:
        current_month = datetime.now().month

        with open(file_name, "r") as file:
            reader = csv.DictReader(file)

            expenses = [
                {
                    "date": row["date"],
                    "amount": float(row["amount"]),
                    "category": row["category"]
                }
                for row in reader
            ]

        # Filter current month expenses
        current_month_expenses = [
            exp for exp in expenses
            if datetime.strptime(exp["date"], "%Y-%m-%d").month == current_month
        ]

        if not current_month_expenses:
            return "No expenses found for current month."

        # Group by category
        category_totals = {}

        for exp in current_month_expenses:
            category = exp["category"]
            amount = exp["amount"]

            category_totals[category] = category_totals.get(category, 0) + amount

        print("Expense Summary (Current Month):")
        for category, total in category_totals.items():
            print(f"{category}: {total:.2f}")

    except FileNotFoundError:
        print("Error: expenses.csv file not found!")
    except ValueError:
        print("Error: Invalid data format in CSV file.")


process_expenses("expenses.csv")