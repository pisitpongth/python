def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    a = int(input("Enter the first number: "))

    b = int(input("Enter the second number: "))

    print("-" * 40)
    print("add, minus, multiply, divide")
    print("-" * 40)
    operation = input("Enter the operation: ")

    if operation == "add":
        result = plus(a, b)
    elif operation == "minus":
        result = minus(a, b)
    elif operation == "multiply":
        result = multiply(a, b)
    elif operation == "divide":
        result = divide(a, b)

    print(f"The result is: {result}")


if __name__ == "__main__":
    main()
