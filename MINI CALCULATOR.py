##MINI CALCULATOR

first = int(input("Enter first number:"))
operator = input("Enter your oprator(*,+,-,,/,%):")
second = int(input("Enter second number:"))

if operator == "+":
    print(first + second)
elif operator == "-":
    print(first - second)
elif operator == "*":
    print(first * second)
elif operator == "/":
    print(first / second)
elif operator == "%":
    print(first % second)
else:
    print("invalid opration")