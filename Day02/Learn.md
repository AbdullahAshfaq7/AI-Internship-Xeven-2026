#day02/Learn.md
#Author: Abdullah | Date: 2026-05-14

## Topic: Python Variables & Data Types & Basic Calculator Build

## Task 1 — Data Types Explorer
Created a script that shows all 4 Python data types:
- **int** — whole numbers like `student_age = 20`
- **float** — decimal numbers like `grade_average = 85.5`
- **bool** — True or False like `is_enrolled = True`
- **str** — text like `student_name = "Ali Hassan"`

Used `type()` to display the type of each variable and practiced type conversion:
- int → str using `str()`
- str → float using `float()`
- float → int using `int()` (decimal gets cut off!)

---

## Task 2 — Interactive Calculator
Built a calculator that takes two numbers from the user and performs 4 operations:
- Addition, Subtraction, Multiplication, Division
- Used `float(input())` to convert user input from string to number
- Added menu with 4 choices using `if/elif`
- Handled division by zero with an extra check
- Used `try/except` to handle invalid input like `abc` gracefully
---

## Task 3 - Theory + Research

### ChatGPT
**Question:** How does Python handle memory for different data types?
**Key Points:** Python automatically manages memory. Small integers (-5 to 256) are cached and reused. Garbage collector cleans up unused variables.
**Best Insight:** You don't manually free memory in Python — it handles it for you.

---

### Gemini
**Question:** Explain mutable vs immutable types in Python with examples
**Key Points:** Immutable = cannot change after creation (int, float, bool, str). Mutable = can change (list, dict, set)
**Best Insight:** Strings are immutable — you can't change one letter, you have to create a whole new string.

---

### Claude
**Question:** What are best practices for naming variables in Python?
**Key Points:** Use snake_case, be descriptive, avoid reserved words like list/str/print
**Best Insight:** Good variable names make code readable without needing comments.

---

### Article
**Key Points:** Every value in Python is an object with a type, value and memory address. Type conversion creates a brand new object in memory.
**Best Insight:** Use type() to always check what type your variable is when debugging.

---

### What I Learned Today
- Python has 4 main data types: int, float, bool, str
- type() shows the type of any variable
- input() always returns a string — must convert manually
- try/except stops the program from crashing on bad input
- Always use snake_case for variable names (PEP 8)

---

### References
1. ChatGPT — https://chat.openai.com
2. Gemini — https://gemini.google.com
3. Claude — https://claude.ai —
4. Article — (https://medium.com/geekculture/how-variables-are-saved-in-python-and-rust-side-by-side-1-float-e2e3eace7302).