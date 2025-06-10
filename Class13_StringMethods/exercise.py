# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter your username: ")

if len(username) > 12:
    print("The username should have less than 12 characters")
elif username.find(" ") != -1:
    print("The username cant contain spaces")
elif not username.isalpha():
    print("The username cant contain Digits")
else:
    print(f"Welcome {username}")
