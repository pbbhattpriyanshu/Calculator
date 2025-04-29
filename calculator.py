def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    return x % y

print("🧮 Welcome to the Simple Calculator!")
print("Operations: +, -, *, /, ** (power), % (modulo)")

while True:
    print("\nChoose operation (or type 'exit' to quit):")
    op = input("Enter operation (+, -, *, /, **, %): ")

    if op == "exit":
        print("Goodbye!")
        break

    if op not in ['+', '-', '*', '/', '**', '%']:
        print("Invalid operation. Try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if op == '+':
        result = add(num1, num2)
    elif op == '-':
        result = subtract(num1, num2)
    elif op == '*':
        result = multiply(num1, num2)
    elif op == '/':
        result = divide(num1, num2)
    elif op == '**':
        result = power(num1, num2)
    elif op == '%':
        result = modulo(num1, num2)

    print(f"Result: {result}")
