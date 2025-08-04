def main():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = add(num1, num2)
            elif operator == "-":
                result = subtract(num1, num2)
            elif operator == "*":
                result = multiply(num1, num2)
            elif operator == "/":
                result = divide(num1, num2)
            else:
                print("Invalid operator")
                continue

            print(f"{num1} {operator} {num2} = {result}")

        except ValueError:
            print("Please enter valid numbers")

        play_again = input("Do you want to calculate again? (y/n): ").lower()
        if play_again == "y" or play_again == "yes":
            continue
        else:
            print("Goodbye!")
            break


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b


if __name__ == "__main__":
    main()