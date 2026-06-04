def write_to_file():
    file_name = "greeting.txt"

    with open(file_name, "w") as file:
        file.write("Hello World")

    return f"Message written to {file_name} successfully."


result = write_to_file()
print(result)