
name = input("Enter your full name: ")
phone = input("Enter your phone number: ")

length = len(name)
print(f"Length: {length}")

index = name.find("h")
index_last = name.rfind("h")

print(f"h first index: {index}")
print(f"h last index: {index_last}")

capit = name.capitalize()
upper = name.upper()
lower = name.lower()

print(f"Capitalized name: {capit}")
print(f"Uppercase name: {upper}")
print(f"Lowercase name: {lower}")

is_digit = name.isdigit()
print(f"{name} is digit? {is_digit}")

is_alpha = name.isalpha()
print(f"{name} is alpha? {is_alpha}")

dash_count = phone.count("-")
print(f"Number of - : {dash_count}")

new_phone = phone.replace("-","")
print(f"New phone replaced: {new_phone}")



