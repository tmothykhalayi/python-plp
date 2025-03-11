

# Get user input for two numbers and an operation
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

# Perform the operation using Python operators
print(f"{num1} {operation} {num2} = ", end="")

# Perform calculation directly based on the operation
result = num1 + num2 if operation == "+" else num1 - num2 if operation == "-" else num1 * num2 if operation == "*" else num1 / num2

print(result)
