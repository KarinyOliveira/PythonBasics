# Type casting = the process of converting a variable from onde data to another
#                str(), int(), float(), bool()

name = "Ashley Smith"
age = 25
gpa = 3.2
is_student = True

print(f"Name: {name} is",type(name))
print(f"Age: {age} is",type(age))
print(f"GPA: {gpa} is",type(gpa))
print(f"Is student: {is_student} is",type(is_student))

# gpa = int(gpa)
# print(f"GPA after casting is {gpa}",type(gpa))
# age = float(age)
# print(f"Age after casting is {age}",type(age))
# age = str(age)
# print(f"Age after casting is {age}",type(age))
name = bool(name)
print(f"Name after casting is {name}",type(name))