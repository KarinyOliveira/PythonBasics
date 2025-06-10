# Python calculator

operator = "+"

while operator != "E":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operator desired (+,-, /, *, E - to Exit): ")

    if operator == "+":
        total = num1 + num2
        print(f"The sum of {num1} and {num2} is {round(total, 2)}")
    elif operator == "-":
        total = num1 - num2
        print(f"The subtraction of {num1} and {num2} is {round(total, 2)}")
    elif operator == "*":
        total = num1 * num2
        print(f"The multiplication of {num1} and {num2} is {round(total, 2)}")
    elif operator == "/":
        total = num1 / num2
        print(f"The division of {num1} and {num2} is {round(total, 2)}")
    elif operator == "E":
        print("Exiting....")
    else:
        print(f"{operator} - Invalid operator, try again!")