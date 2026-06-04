import statistics

def analyze_sales(file_name):
    try:
        with open(file_name, "r") as file:
            data = file.readlines()

        sales = []

        for line in data:
            try:
                value = float(line.strip())
                sales.append(value)
            except ValueError:
                print(f"Skipping invalid data: {line.strip()}")

        if not sales:
            return "No valid sales data found."

        mean_value = statistics.mean(sales)
        median_value = statistics.median(sales)

        return (
            f"Sales Data: {sales}\n"
            f"Mean Sales: {mean_value:.2f}\n"
            f"Median Sales: {median_value:.2f}"
        )

    except FileNotFoundError:
        return "File not found! Please check the file name."


result = analyze_sales("sales.txt")
print(result)