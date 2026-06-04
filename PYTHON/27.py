def get_length(text):
    if not isinstance(text, str):
        return "Invalid input! Please provide a string."
    if text.strip() == "":
        return "Invalid input! String cannot be empty."

    return f"Length of the string: {len(text)}"


text = "Hello World"

result = get_length(text)
print(result)