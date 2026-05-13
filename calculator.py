def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def main():
    operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

    print("Simple Calculator")
    print("Operations: +, -, *, /")
    print("Type 'quit' to exit\n")

    while True:
        try:
            expr = input("Enter expression (e.g. 5 + 3): ").strip()
            if expr.lower() == 'quit':
                break

            parts = expr.split()
            if len(parts) != 3:
                print("Invalid format. Use: number operator number")
                continue

            a, op, b = parts
            if op not in operations:
                print(f"Unknown operator '{op}'. Use +, -, *, /")
                continue

            result = operations[op](float(a), float(b))
            print(f"= {result}\n")

        except ValueError as e:
            print(f"Error: {e}\n")

if __name__ == "__main__":
    main()
