# Python weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == "K":
    weight = weight * 2.205
    print(f"your weight is: {round (weight, 2)} Lbs.")
elif unit == "L":
    weight = weight / 2.205
    print(f"your weight is: {round (weight, 2)} Kgs.")
else:
    print(f"{unit} was not valid")