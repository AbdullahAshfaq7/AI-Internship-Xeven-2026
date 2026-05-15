#day03/age_verification.py
#Age verification in Python
#Author: Abdullah | Date: 2026-05-15

#make a Function

def Classify_age(name,age):

    if age < 0:
        return "Error: Age cannot be negative or Zero"
    elif age < 13:
        category = "Child"
        message = "Keep Exploring and Learning!"
    elif age < 18:
        category = "Teenager"
        message = "You have many opportunities ahead!"
    elif age < 65:
        category = "Adult"
        message = "Make the most of your time and enjoy life!"
    else:
        category = "Senior"
        message = "Your Wisdom and Experience are Valuable!"

    return f"Hello {name}!, You are classified as a {category}. {message}"
    

#--Main program--

# Welcome message
print("Welcome to the Age Classification Program!")

try:

    # Get user input
    user_name = input("Please enter your name:")
    user_age = int(input("Please enter your age:"))

    # Classify age and display result
    print(Classify_age(user_name, user_age))

except ValueError:
    print("Invalid input. Please enter a valid age as a number.")