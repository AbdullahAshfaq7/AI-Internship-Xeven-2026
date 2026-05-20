# day06/list_slicing.py
# list_slicing Practice
# Author: Abdullah | Date: 20-05-2026

"list slicing is a powerful technique in Python that allows you to access a portion of a list. It uses the syntax list[start:stop:step]"

"where start is the index to begin slicing, stop is the index to end slicing (exclusive), and step is the interval between elements."

# Create list of numbers 1 to 20
numbers = list(range(1, 21))
print(f"Full list:  {numbers}")

# First 5 elements
print(f"First 5:    {numbers[:5]}")

# Last 5 elements
print(f"Last 5:     {numbers[-5:]}")

# Every 3rd element
print(f"Every 3rd:  {numbers[::3]}")

# Reverse entire list
print(f"Reversed:   {numbers[::-1]}")

# Middle 10 elements (index 5 to 15)
print(f"Middle 10:  {numbers[5:15]}")
