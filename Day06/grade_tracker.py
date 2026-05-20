# day06/grade_tracker.py
# Grade Tracker using Parallel Lists
# Author: Abdullah | Date: 20-05-2026

"""
Tracks student names and grades using two parallel lists.
Finds highest, lowest, average and pass/fail results.
"""

# --- PARALLEL LISTS ---
student_names = ["Ali", "Sara", "Ahmed", "Zara", "Omar"]
student_grades = [88, 45, 92, 61, 73]

# --- DISPLAY ALL STUDENTS ---
print("Students & Grades:")

student_names.sort()
for i in range(len(student_names)):
    print(f"{student_names[i]:<10} → {student_grades[i]}")

# --- CALCULATE HIGHEST, LOWEST, AVERAGE ---

# Highest grade

highest_grade = max(student_grades)
highest_index = student_grades.index(highest_grade)
print(f" Highest grade: {student_names[highest_index]}-{highest_grade}")

# Lowest grade
lowest_grade = min(student_grades)
lowest_index = student_grades.index(lowest_grade)
print(f" Lowest grade: {student_names[lowest_index]}-{lowest_grade}")

# Average grade
average_grade = sum(student_grades) / len(student_grades)
print(f" Average grade: {average_grade:.2f}")

# --- PASS / FAIL ---
passed = []
failed = []

for i in range(len(student_names)):
    if student_grades[i] >= 50:
        passed.append(student_names[i])
    else:
        failed.append(student_names[i])

print(f"\nPassed: {passed}")
print(f"Failed: {failed}")
