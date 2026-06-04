def sum_of_odds(limit):
    if not isinstance(limit, int) or limit <= 0:
        return "Invalid input! Limit must be a positive integer."

    total = 0

    for i in range(limit):
        if i % 2 == 0:
            continue
        total += i

    return f"Sum of odd numbers: {total}"


limit = 10

result = sum_of_odds(limit)
print(result)