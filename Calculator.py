num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))
op = float(input("Enter Operation: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    if num1 or num2 != 0:
        print(num1 / num2)
    else:
        print("Can't Divide With Zero")
else:
    print("Invalid Operator")
