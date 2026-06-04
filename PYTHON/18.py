def find_first_even(start, end):
    if not (isinstance(start, int) and isinstance(end, int)):
        return "Invalid input! Range values must be integers."
    if start > end:
        return "Invalid range! Start should be less than or equal to end."

    for i in range(start, end + 1):
        if i % 2 == 0:
            return f"First even number in range: {i}"

    return "No even number found in the given range."


start = 3
end = 9

result = find_first_even(start, end)
print(result)