# day06/student_management.py
# Student Management System using Python Lists
# Author: Abdullah | Date: 20-05-2026

"""
Demonstrates list operations:

#adding items to list: append, insert, extend.

# removing items from list: remove, pop, clear.

# accessing items in list: indexing, slicing

#list methods: sort, reverse, count, index.
"""

# --- "INITIAL STUDENT LIST" ---

students = ["Abdullah", "Aybe", "Ronaldo", "Messi", "Neymar"]
print(f"Initial student list: {students}")

# --- ADDING STUDENTS ---

# Using append to add a student at the end of the list
students.append("Ramos")
print(f"After Append: {students}")

# Using insert to add a student at a specific index
students.insert(4, "Mbappe")
print(f"After Insert: {students}")

# Using extend to add multiple students at once
students.extend(["Marcelo", "Pepe"])
print(f"After Extend: {students}")


# --- REMOVING STUDENTS ---

# Using remove to delete a student by name
students.remove("Pepe")
print(f"After Remove: {students}")

# Using pop to remove a student by index
removed_student = students.pop(6)
print(f"Removed Student: {removed_student}")
print(f"After Pop: {students}")


# --- ACCESSING STUDENTS ---

# Using indexing to access a student
first_student = students[0]
print(f"First Student: {first_student}")

# Using slicing to access a range of students

# first 3 students
first_three = students[:3]
print(f"First Three Students: {first_three}")

# last 3 students
last_three = students[-3:]
print(f"Last Three Students: {last_three}")


# --- LIST METHODS / SORTING ---

# Using sort to sort the student list alphabetically
students.sort()
print(f"Sorted Students: {students}")

# Using reverse to reverse the order of the student list
students.reverse()
print(f"Reversed Students: {students}")

# Using count to count occurrences of a student
count_Ronaldo = students.count("Ronaldo")
print(f"Count of Ronaldo: {count_Ronaldo}")

# Using index to find the index of a student
index_Abdullah = students.index("Abdullah")
print(f"Index of Abdullah: {index_Abdullah}")


# --- LIST INFO ---

print(f"\nTotal students: {len(students)}")
print(f"Index of Ramos: {students.index('Ramos')}")
print(f"Ronaldo appears:    {students.count('Ronaldo')} time(s)")
