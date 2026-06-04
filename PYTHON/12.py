def check_pass_fail(marks):
   
    if not isinstance(marks, (int, float)):
        return "Invalid input! Marks must be a number."
    if marks < 0 or marks > 100:
        return "Invalid marks! Must be between 0 and 100."

    if marks >= 50:
        return "Pass"
    else:
        return "Fail"

marks = 75

result = check_pass_fail(marks)
print(f"Student Result: {result}")