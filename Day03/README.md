# Conditional Statements & Logic

## Files
|        File           |  Description                                     |
|-----------------------|--------------------------------------------------|
| `age_verification.py` | Age classification using if/elif/else            |
| `grade_calculator.py` | Grade calculator with letter grades and feedback |
| `LEARNINGS.md`        | Research notes, insights and study notes         |
| `README.md`           | This file                                        |

## Task 1 — Age Verification System
Built a program that classifies a person into Child, Teenager, Adult or Senior based on age:
- Used `if/elif/else` to check age ranges and assign category and message
- Used `return` outside all blocks so it works for every category
- Used `try/except` to handle invalid input like letters instead of numbers
- Learned that `return` inside a block only returns for that specific case

---

## Task 2 — Grade Calculator
Built a grade calculator that takes a student name and score and returns a letter grade:
- Used `if/elif/else` to classify scores into A, B, C, D, F
- Added validation to reject scores below 0 or above 100
- Used `float()` for input so decimal scores like 85.5 are accepted
- Returned the full result string outside all blocks

---

## Task 3 — Research: Boolean Logic & Clean Conditionals

>Full research notes, source comparisons and coding style analysis are documented in `LEARNINGS.md`

### Quick Summary
- **ChatGPT:** Always handle edge cases first — more than 3 levels of nesting means restructure your code
- **Gemini:** Use early return pattern — check errors at the top, write clean main logic below
- **Claude:** Boolean logic should read like English — `if is_valid:` is cleaner than `if is_valid == True:`
- **Article:** Flat code is better than nested — the best conditional is the one you don't need

### Key Takeaway
`elif` chain is always better than nested `if` — flat, readable, and easy to follow top to bottom

---

## References
1. Claude 
2. ChatGPT 
3. Gemini 
4. Article 