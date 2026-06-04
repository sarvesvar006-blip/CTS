def assign_grade(score):
    
    if not isinstance(score, (int, float)):
        return "Invalid input! Score must be a number."
    if score < 0 or score > 100:
        return "Invalid score! Must be between 0 and 100."

    
    if score >= 85:
        grade = "A"
        remark = "Excellent"
    elif score >= 70:
        grade = "B"
        remark = "Good"
    else:
        grade = "C"
        remark = "Needs Improvement"

    return f"Score: {score}\nGrade: {grade}\nRemark: {remark}"


score = 88
result = assign_grade(score)
print(result)