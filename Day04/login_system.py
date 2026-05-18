#day04/login_system.py
#Login System in Python That Demonstrates Logical Operators and Type Conversion.
#Author: Abdullah | Date: 18-06-2026

# --- Func1: Validate User Username ---
"""
    Req:
    Validate username — must be at least 5 characters.
    Returns (bool, message) tuple.

"""

def validate_username(username):
   if len(username) < 5:
    return False, "Username must be at least 5 characters long."
    return True, "Username is valid."
   

# --- Func2: Validate Password ---
"""
    Validate password — must be at least 8 characters,
    contain at least one number and one uppercase letter.

"""

def validate_password(password):
  if len(password) < 8:
    return False, "Password must be at least 8 characters long."
  if not any(char.isdigit() for char in password):
    return False, "Password must contain at least one number."
  if not any(char.isupper() for char in password):
    return False, "Password must contain at least one uppercase letter."
  
    return True, "Password is valid."
  
# --- Func3: Validate Age ---
"""
    Validate age — must be 18 or older.
    Returns (bool, message) tuple.
    
"""

def validate_age(age):
  if age < 18:
    return False, "You must be at least 18 years old to register."
    return True, "Age is valid."
  
# --- Func4: Validate Login ---
"""
    Run all validations and return final login result.
    Uses logical AND — all conditions must pass.

"""

def validate_login(username, password, age):
    username_valid, username_msg = validate_username(username)
    password_valid, password_msg = validate_password(password)
    age_valid, age_msg = validate_age(age)

    if username_valid and password_valid and age_valid:
        return True, f"Welcome {username}! Your login is successful."
    
    error_messages = []
    if not username_valid:
        error_messages.append(username_msg)
    if not password_valid:
        error_messages.append(password_msg)
    if not age_valid:
        error_messages.append(age_msg)

    return False, "\n".join(error_messages)


# --- Main Program ---
print("=== Welcome to the Login System ===")
try:
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    age_input = input("Enter your age: ")
    age = int(age_input) # Type conversion from string to int

    #run login validation
    success, message = validate_login(username, password, age)
    print(message)

except ValueError:
    print("Invalid input for age. Please enter a valid number.")