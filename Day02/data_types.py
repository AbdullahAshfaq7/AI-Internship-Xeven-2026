#day02/data_types.py
#Data types in Python
#Author: Abdullah | Date: 2026-05-14


# --- INTEGER --- whole numbers
print("INTEGER DATA TYPE")
student_age = 23
total_students = 50

print(f"Student age:{student_age}")
print(f"type:{type(student_age)}")
print(f"Total Students:{total_students}")
print(f"type:{type(total_students)}")
print("---------------------------------")

# --- FLOAT --- decimal numbers
print("FLOAT DATA TYPE")
marks = 99.5
price= 200.92

print(f"Marks:{marks}")
print(f"type:{type(marks)}")
print(f"Price:{price}")
print(f"type:{type(price)}")
print("---------------------------------")

#--- BOOLEAN --- True or False
print("BOOLEAN DATA TYPE")
quiz_sumbitted = True
assignment_completed = False

print(f"Quiz submitted:{quiz_sumbitted}")
print(f"type:{type(quiz_sumbitted)}")
print(f"Assignment completed:{assignment_completed}")
print(f"type:{type(assignment_completed)}")
print("---------------------------------")

#--- STRING --- Characters/Text
print("STRING DATA TYPE")
name= "abdullah"
city= "lahore"

print(f"Name:{name}")
print(f"Type:{type(name)}")
print(f"City:{city}")
print(f"Type:{type(city)}")
print("---------------------------------")

# --- TYPE CONVERSION ---
print("TYPE CONVERSION")
# int to str
age_as_string = str(student_age)

print(f"Int to String: {age_as_string}")
print(f"Type: {type(age_as_string)}")

# str to float

grade_as_float = float("92.5")
print(f"String to Float: {grade_as_float}")
print(f"Type: {type(grade_as_float)}")

# float to int (decimal gets cut off!)

grade_as_int = int(grade_as_float)
print(f"Float to Int: {grade_as_int}")
print(f"Type: {type(grade_as_int)}")
