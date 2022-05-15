expression = input("Expression: ")

x, y, z = expression.split(" ")

if y == "+":
    print(float(int(x) + int(z)))

elif y == "-":
    print(float(int(x) - int(z)))

elif y == "*":
    print(float(int(x) * int(z)))

elif y == "/":
    print(float(int(x) / int(z)))

else:
    print("Unknown operator")