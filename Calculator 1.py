# Basic Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


operation = input("Enter the operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
    print(f"{num1} plus {num2} equals {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} minus {num2} equals {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} times {num2} equals {result}")
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} divided by {num2} equals {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please use +, -, *, or /.")
