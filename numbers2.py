# Simple calculator
firstvalue = float(input("Enter your first value:"))
secondvalue = float(input("Enter your second value:"))

operator = input("Enter operator:")

if operator == "+":
    print("The result is", firstvalue + secondvalue)
elif operator == "-":
    print("The result is", firstvalue - secondvalue)
elif operator == "*":
    print("The result is", firstvalue * secondvalue)
elif operator == "/":
    print("The result is", firstvalue / secondvalue)
else:
    print("Invalid operator")

