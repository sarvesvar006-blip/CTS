def find_salary_extremes(salaries):
    
    if not isinstance(salaries, list) or len(salaries) == 0:
        return "Invalid input! Provide a non-empty list."

    if not all(isinstance(s, (int, float)) for s in salaries):
        return "Invalid data! All salaries must be numbers."

    
    lowest = min(salaries)
    highest = max(salaries)
    return lowest, highest


salary_list = [50000, 75000, 62000, 95000]
result = find_salary_extremes(salary_list)

if isinstance(result, str):
    print(result)
else:
    lowest, highest = result
    print(f"Lowest Salary : {lowest}")
    print(f"Highest Salary: {highest}")