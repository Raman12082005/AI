def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"


while True:

    print("\n===== Simple Calculator =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you for using the calculator!")
        break

    if choice not in [1, 2, 3, 4]:
        print("Invalid Choice")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result =", add(num1, num2))

    elif choice == 2:
        print("Result =", subtract(num1, num2))

    elif choice == 3:
        print("Result =", multiply(num1, num2))

    elif choice == 4:
        print("Result =", divide(num1, num2))