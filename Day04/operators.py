#day04/operators.py
#Operators in Python
#Author: Abdullah | Date: 18-06-2026

# --- ARITHMETIC OPERATORS ---
num1 = 10
num2 = 5

print(f"=== Arithmetic Operators ===")

print(f"Addition: {num1} + {num2} = {num1 + num2}")
print(f"Substraction: {num1} - {num2} = {num1 - num2}")
print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
print(f"Division: {num1} / {num2} = {num1 / num2}")
print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")

# --- OPERATOR PRECEDENCE ---

print("\n=== Operator Precedence ===")
print(f"2 + 3 * 4 = {2 + 3 * 4}")        # 14 — multiplication first
print(f"(2 + 3) * 4 = {(2 + 3) * 4}")    # 20 — brackets first

# --- TYPE CONVERSION ---

print("\n=== Type Conversion ===")

# Implicit conversion — Python does it automatically
implicit = 5 + 3.0
print(f"5 + 3.0 = {implicit} — Type: {type(implicit)}")  # float

# Explicit conversion — we do it manually
age_str = "22"
age_int = int(age_str)
print(f"Age: {age_int} — Type: {type(age_int)}")  # int

# --- LOGICAL/COMPARISON OPERATORS ---
print("\n=== Comparison Operators ===")
age = 22
has_id = True

print(f" age >= 18 & Has ID: {age>=18 and has_id}")  # True
print(f" age >= 18 | Has ID: {age>=18 or has_id}")  # True
print(f" not has_id: {not has_id}")  # False
