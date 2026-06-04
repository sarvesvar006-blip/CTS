import csv

def process_employee_data(file_name):
    try:
        with open(file_name, "r") as file:
            reader = csv.DictReader(file)

            employees = [
                {
                    "name": row["name"],
                    "salary": float(row["salary"])
                }
                for row in reader
            ]

        if not employees:
            return "No data found in file."

        high_salary_employees = [
            emp for emp in employees if emp["salary"] > 50000
        ]

        total_salary = sum(emp["salary"] for emp in employees)
        average_salary = total_salary / len(employees)

        print("Employees with salary > 50000:")
        for emp in high_salary_employees:
            print(emp)

        print(f"\nAverage Salary: {average_salary:.2f}")

    except FileNotFoundError:
        print("Error: File not found!")
    except KeyError:
        print("Error: CSV must contain 'name' and 'salary' columns.")
    except ValueError:
        print("Error: Invalid salary data in file.")


process_employee_data("employees.csv")