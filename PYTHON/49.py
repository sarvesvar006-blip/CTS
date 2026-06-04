from tabulate import tabulate

class TemperatureConverter:
    
    def c_to_f(self, c):
        return (c * 9/5) + 32

    def f_to_c(self, f):
        return (f - 32) * 5/9

    def c_to_k(self, c):
        return c + 273.15

    def k_to_c(self, k):
        return k - 273.15

    def f_to_k(self, f):
        return self.c_to_k(self.f_to_c(f))

    def k_to_f(self, k):
        return self.c_to_f(self.k_to_c(k))


converter = TemperatureConverter()

while True:
    print("\n--- Temperature Converter ---")
    print("1. Celsius → Fahrenheit")
    print("2. Fahrenheit → Celsius")
    print("3. Celsius → Kelvin")
    print("4. Kelvin → Celsius")
    print("5. Fahrenheit → Kelvin")
    print("6. Kelvin → Fahrenheit")
    print("7. Show Conversion Table")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "8":
        print("Exiting...")
        break

    try:
        if choice == "1":
            c = float(input("Enter Celsius: "))
            print(f"Fahrenheit: {converter.c_to_f(c):.2f}")

        elif choice == "2":
            f = float(input("Enter Fahrenheit: "))
            print(f"Celsius: {converter.f_to_c(f):.2f}")

        elif choice == "3":
            c = float(input("Enter Celsius: "))
            print(f"Kelvin: {converter.c_to_k(c):.2f}")

        elif choice == "4":
            k = float(input("Enter Kelvin: "))
            print(f"Celsius: {converter.k_to_c(k):.2f}")

        elif choice == "5":
            f = float(input("Enter Fahrenheit: "))
            print(f"Kelvin: {converter.f_to_k(f):.2f}")

        elif choice == "6":
            k = float(input("Enter Kelvin: "))
            print(f"Fahrenheit: {converter.k_to_f(k):.2f}")

        elif choice == "7":
            data = [
                ["C → F", converter.c_to_f(0)],
                ["F → C", converter.f_to_c(32)],
                ["C → K", converter.c_to_k(0)],
                ["K → C", converter.k_to_c(273.15)],
            ]

            print("\nConversion Table:")
            print(tabulate(data, headers=["Conversion", "Result"], tablefmt="grid"))

        else:
            print("Invalid choice!")

    except ValueError:
        print("Error: Please enter numeric values only.")