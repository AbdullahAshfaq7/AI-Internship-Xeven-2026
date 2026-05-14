#day02/Calculator.py
#basic calculator using user input, error handling.
#Author: Abdullah | Date: 2026-05-14

print("Welcome to the Basic Calculator!")

try:
    # Get numbers from user and convert to float
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Show menu
    print("\nSelect operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    # Perform selected operation
    if choice == '1':
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is: {result}")
    elif choice == '2':
        result = num1 - num2
        print(f"The difference of {num1} and {num2} is: {result}")
    elif choice == '3':
        result = num1 * num2
        print(f"The product of {num1} and {num2} is: {result}")
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"The quotient of {num1} and {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid choice! Please select 1, 2, 3 or 4.")

except ValueError:
    print("Invalid input! Please enter numbers only.")