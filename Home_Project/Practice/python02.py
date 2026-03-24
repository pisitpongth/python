def plus(a, b):
    return a + b


def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("[add, minus, multiply, divide]")
operation = input("Enter the operation: ")

if operation == "add":
    result = plus(a, b)
elif operation == "minus":
    result = minus(a, b)
elif operation == "multiply":
    result = multiply(a, b)
elif operation == "divide":
    result = divide(a, b)

print(f"The result of {a} {operation} {b} is: {result}")
