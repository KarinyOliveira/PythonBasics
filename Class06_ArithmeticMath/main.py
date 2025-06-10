# -------- Arithmetic Operators ---------------

# friends = 10

# friends = friends + 1
# friends +=1
# friends = friends - 1
# friends -=1
# friends = friends * 3
# friends *= 3
# friends = friends / 2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# remainder = friends % 2
#
# print(friends)
# print(remainder)

# --------- Math ----------------

# x = 3.14
# w = -8
# y = 4
# z = 5

# result = round(x)
# result = abs(w)
# result = pow(4, 3)
# result = max(x, w, y, z)
# result = min(x, w, y, z)

# print(result)

# import math
#
# x = 9
# y = 9.1
#
# # print(math.pi)
# # print(math.e)
#
# # result = math.sqrt(x)
# # result = math.ceil(y)
# result = math.floor(y)
#
# print(result)

# ---------------- EXERCISES --------------------

import math

# radius = float(input('Enter the radius of a circle: '))
#
# circumference = 2 * math.pi * radius
#
# print(f"The circumference is: {round(circumference, 2)}cm")

# radius = float(input('Enter the radius of a circle: '))
#
# area = math.pi * pow(radius, 2)
#
# print(f"The area of the circle is: {round(area, 2)}cm²")

a = float(input("Enter side A: "))
b = float(input("Enter side B: "))

c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"Side C is {round(c, 2)}cm²")