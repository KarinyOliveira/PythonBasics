# input() = A function that prompts the user to enter data
#           Returns the entered data as a string

# name = input("What is your name? ")
# age = int(input("How old are you? "))
#
# print(f"Hello {name}!")
# print(f"You are {age} years old")

# length = float(input("Enter the length: "))
# width = float(input("Enter the width: "))
#
# area = length * width
#
# print(f"The area is {area}cm²")

item = input("What item would you like to buy? ")
price = float(input("What is the price? "))
quantity = int(input("How many would you like? "))

total = price * quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is ${total}")