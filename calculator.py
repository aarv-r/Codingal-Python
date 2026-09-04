def calculator_add(a,b):
    return a+b
def calculator_sub(a,b):
    return a-b
def calculator_mul(a,b):
    return a*b
def calculator_div(a,b):
    return a/b
operation = input("Enter operation (+, -, *, /): ")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if operation == "+":
    print(calculator_add(a,b))
elif operation == "-":
    print(calculator_sub(a,b))
elif operation == "*":
    print(calculator_mul(a,b))
elif operation == "/":
    print(calculator_div(a,b))
else:
    print("invalid operation/values")