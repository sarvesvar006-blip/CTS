def find_common_skills(set1, set2):
    if not (isinstance(set1, set) and isinstance(set2, set)):
        return "Invalid input! Both inputs must be sets."
    if not set1 or not set2:
        return "Invalid input! Sets cannot be empty."

    common = set1 & set2

    return f"Common Skills: {common}"


skills1 = {"Python", "SQL", "Java"}
skills2 = {"Python", "C++", "SQL"}

result = find_common_skills(skills1, skills2)
print(result)