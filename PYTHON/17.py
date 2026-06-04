def countdown(count):
   
    if not isinstance(count, int) or count <= 0:
        return "Invalid input! Count must be a positive integer."

    
    while count > 0:
        print(f"Count: {count}")
        count -= 1


count = 5

result = countdown(count)
if result:
    print(result)