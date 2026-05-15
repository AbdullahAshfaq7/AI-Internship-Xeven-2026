# Day 03 — Learnings

## Topic: Conditional Statements & Logic

---

## Theory Studied

### if / elif / else
- Python reads conditions top to bottom and stops at the first True one
- Only ONE block runs even if multiple conditions are True
- `else` is the fallback — runs when nothing above is True
- Order matters — always put most specific condition first
- Indentation is NOT just style — it defines what is inside the block

### Comparison Operators
| Operator | Meaning          | Example |Result  |
|----------|------------------|---------|--------|
| `==`     | equals           | `5 == 5`|  True  |
| `!=`     | not equal        | `5 != 3`|  True  |
| `>`      | greater than     | `10 > 5`|  True  |
| `<`      | less than        | `3 < 7` |  True  |
| `>=`     | greater or equal | `5 >= 5`|  True  |
| `<=`     | less or equal    | `4 <= 6`|  True  |

### Logical Operators
| Operator | Meaning           | Example                       |
|----------|-------------------|-------------------------------|
| `and`    | both must be True | `age > 18 and has_id == True` |
| `or`     | at least one True | `is_admin or is_staff`        |
| `not`    | flips True/False  | `not is_banned`               |

### Most Common Mistakes
- Using `=` instead of `==` inside conditions — assigns instead of compares
- Putting `return` inside a block — only returns for that one case, returns None for others
- Wrong indentation — breaks the entire logic silently
- Deeply nested if statements — hard to read and maintain

---

## Task 1 — Age Verification System

### What I built
A program that takes a name and age and classifies the person into:
- Child (under 13)
- Teenager (13 to 17)
- Adult (18 to 64)
- Senior (65 and above)

### What I learned from this task
- Validate edge cases first — negative age checked before anything else
- `return` must be at the same indentation level as `if` — outside all blocks
- `try/except ValueError` handles non-numeric input gracefully
- Function name must match exactly — `Classify_age` and `classify_age` are different!

### Bug I fixed
`return` was placed inside the `else` block — so it only returned a value for Senior category. All other categories returned `None`. Fixed by moving `return` outside all blocks at the end of the function.

---

## Task 2 — Grade Calculator

### What I built
A program that takes a student name and score (0-100) and returns:
- Letter grade: A, B, C, D or F
- Personalized feedback message

### What I learned from this task
- Used `float()` instead of `int()` to accept decimal scores like 85.5
- Validated score range at the top — rejected below 0 or above 100
- Each elif only needs to check one boundary because previous conditions already filtered the rest
- Returning a formatted f-string gives clean readable output

---

## Research Task — Boolean Logic & Clean Conditionals

### ChatGPT
**Question:** What are best practices for if/elif/else statements?
**Key Points:**
- Always handle edge cases first before main logic
- Keep each condition simple — one idea per condition
- Avoid deeply nested if statements — use elif instead
- Use meaningful variable names so conditions read naturally

**Best Insight:** If you have more than 3 levels of nesting your code needs to be restructured. Deep nesting is a sign of unclear logic.

---

### Gemini
**Question:** What are best practices for if/elif/else statements?
**Key Points:**
- Put the most likely condition first for better performance
- Use positive conditions over negative ones — easier to read
- Use guard clauses to return early and reduce nesting
- Avoid redundant else when return is already used

**Best Insight:** Early return pattern keeps functions flat and readable — check for errors at the top, then write the clean main logic below without any extra nesting.

---

### Claude
**Question:** What are best practices for if/elif/else statements?
**Key Points:**
- Boolean logic should read like plain English
- Use meaningful variable names so conditions are self-explanatory
- Avoid comparing booleans to True/False explicitly
- Keep conditions short — if a condition needs a comment it is too complex

**Best Insight:** `if is_valid:` is cleaner than `if is_valid == True:` — the variable name should tell the story on its own.

---

### Article
**Topic:** Writing clean conditional statements in Python
**Key Points:**
- Flat code is always better than nested code
- Use dictionary mapping instead of long if/elif chains when possible
- Always validate input at the top of the function
- One condition should do one thing only

**Best Insight:** The best conditional is the one you do not need — simplify your logic before writing it. If you can remove an if statement, remove it.

---

## Coding Styles Comparison

### Style 1 — Nested if  Hard to read
```python
if age > 0:
    if age < 18:
        if age < 13:
            print("Child")
        else:
            print("Teenager")
```
Problems: 3 levels deep, hard to follow, easy to make mistakes

---

### Style 2 — elif chain  Clean and flat
```python
if age < 0:
    print("Invalid")
elif age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
```
Benefits: flat structure, easy to read top to bottom, each condition is independent

---

### Verdict — Most Readable Style: elif chain
- Flat structure — easy to follow top to bottom
- No unnecessary nesting
- Each condition is clear and independent
- Easy to add or remove a category without breaking others

---

## What I Learned Today
- `if/elif/else` checks top to bottom — first True wins, rest are skipped
- `==` compares values, `=` assigns values — never mix them up
- `return` must be outside all blocks to work for every condition
- Indentation in Python defines logic — not just style
- Flat elif chains are always better than deeply nested if statements
- Always validate edge cases first before writing main logic
- Function names are case sensitive — `classify_age` and `Classify_age` are different

---

## References
1. ChatGPT — https://chat.openai.com — 2026-05-15
2. Gemini — https://gemini.google.com — 2026-05-15
3. Claude — https://claude.ai — 2026-05-15
4. Article — [paste your article URL here] — 2026-05-15