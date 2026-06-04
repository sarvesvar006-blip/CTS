def read_file():
    file_name = "greeting.txt"

    try:
        with open(file_name, "r") as file:
            content = file.read()
        return f"File Content:\n{content}"
    except FileNotFoundError:
        return "File not found! Please check if the file exists."


result = read_file()
print(result)