def split_bill(total_bill, people):
    
    if not (isinstance(total_bill, (int, float)) and total_bill >= 0):
        return "Invalid bill amount!"
    if not (isinstance(people, int) and people > 0):
        return "Invalid number of people!"


    share = total_bill // people

    return share



total_bill = 1250
people = 4
result = split_bill(total_bill, people)

if isinstance(result, str):
    print(result)
else:
    print(f"Each person should pay: {result:.2f}")