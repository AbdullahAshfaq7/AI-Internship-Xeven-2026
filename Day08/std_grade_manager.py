# day08/student_grade_manager.py
# Student Grade Manager
# Author: Abdullah | Date: 22-05-2026

"""
Manages student name and grades using parallel lists.
Demonstrates list comprehension, zip(), sorted(), and and functions.
"""

# --- FUNCTIONS ---


def add_student(names, grades, name, grade):
    """Adds a student and their grade to the lists."""
    names.append(name)
    grades.append(grade)
    print(f"Added Student: {name} with Grade: {grade}")


def remove_student(names, grades, name):
    """Removes a student and their grade from the lists."""
    if name in names:
        index = names.index(name)  # noqa: F841
        names.pop(index)
        grades.pop(index)
        print(f"Removed Student: {name}")
    else:
        print(f"Student {name} Not Found!")


def update_grade(names, grades, name, new_grade):
    """update a student grade by name"""
    if name in names:
        index = names.index(name)  # noqa: F841
        old_grade = grades[index]  # noqa: F841
        grades[index] = new_grade
        print(f"Updated Student Grade: {name} - {old_grade} -> {new_grade}")
    else:
        print(f"student {name} not found")


def get_avg(grades):
    """Calculate and Return AVG Grade"""
    return sum(grades) / len(grades)


def get_top_students(names, grades, n=3):
    """Return Top n Students sorted by grade"""

    # zip names and grade together then sort by grade

    paired = list(zip(names, grades))
    sorted_pairs = sorted(paired, key=lambda x: x[1], reverse=True)
    return sorted_pairs[:n]


def display_all_students(names, grades):
    """Displays all students and their grades"""
    print("All Students with Grades:")
    for i, (name, grade) in enumerate(zip(names, grades), start=1):
        print(f"{i}. {name:<10} - {grade}")


# --- MAIN PROGRAM ---
names = ["Ronaldo", "Messi", "Neymar", "Ramos"]
grades = [97, 90, 85, 88]

# Display initial students
display_all_students(names, grades)

# Add a new student
add_student(names, grades, "zlatan", 87)

# Update a student's grade
update_grade(names, grades, "Neymar", 89)

# Remove a student
remove_student(names, grades, "Messi")

# Display updated students
display_all_students(names, grades)

# Display average grade
avg_grade = get_avg(grades)
print(f"Average Grade: {avg_grade:.2f}")

# Display top 3 students
print("Top Students:")
for i, (name, grade) in enumerate(get_top_students(names, grades), start=1):
    print(f"{i}. {name} - {grade}")

# Above and Below Average Students using list comprehension
above = [names[i] for i in range(len(names)) if grades[i] > avg_grade]
below = [names[i] for i in range(len(names)) if grades[i] < avg_grade]
print(f"Above Average Students: {above}")
print(f"Below Average Students: {below}")
