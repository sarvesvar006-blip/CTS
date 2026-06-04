def calculate_net_salary(salary, tax_rate):
    
    if salary < 0:
        return "Invalid salary amount!"
    if tax_rate < 0 or tax_rate > 1:
        return "Invalid tax rate! Must be between 0 and 1."

    
    tax = salary * tax_rate
    net_salary = salary - tax

    return net_salary



salary = 75000.5
tax_rate = 0.18


result = calculate_net_salary(salary, tax_rate)


if isinstance(result, str):
    print(result)
else:
    print(f"Net Salary after tax: {result:.2f}")