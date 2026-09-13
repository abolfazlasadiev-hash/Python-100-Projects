num1 = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))


if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Error: Cannot divide by zero.")
        exit()
else:
    print("Error: Invalid operation.")
    exit()

print("Result:", result)