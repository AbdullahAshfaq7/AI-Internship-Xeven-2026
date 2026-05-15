#day03/grade_calculator.py
#Grade calculator in Python
#Author: Abdullah | Date: 2026-05-15

#make a Function
def calculate_grade(name, score):

    if score < 0 or score >100:
        return "Error: Score must be between 0 and 100"
    elif score >= 90:
        grade = "A"
        message = "Excellent work! Keep it up!" 
    elif score >= 80:
        grade = "B"
        message = "Good job! You're doing well!"
    elif score >= 70:
        grade = "C"
        message = "Not bad! Keep working on it!"
    elif score >= 60:
        grade = "D"
        message = "You passed, but there's room for improvement!"
    else:
        grade = "F"
        message = "Don't give up! Keep trying and you'll get there!"

        return f"Hello {name}!, Your grade is {grade}. {message}"
    
#--Main program--

# Welcome message
print("Welcome to the Grade Calculator Program!")

try:

    #get user input
    user_name = input("Please enter your name:")
    user_score = float(input("Please enter your score (0-100):"))

    # Calculate grade and display result
    print(calculate_grade(user_name, user_score))

except ValueError:
    print("Error: Please enter a valid numeric score.")