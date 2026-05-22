# Day 08 — Lists & List Operations Deep Dive

## Files

| File                       | Description                                |
|----------------------------|--------------------------------------------|
| `student_grade_manager.py` |Grade management with sorting and filtering |
| `shopping_cart.py`         |Shopping cart with receipt and discount     |
| `data_cleaner.py`          |5-step data cleaning pipeline               |
| `LEARNINGS.md`             |Detailed research notes and key takeaways   |
| `README.md`                |This file.                                  |

## What I Built

- `student_grade_manager.py` — manages students and grades with add, remove, update, sort and filter functions
- `shopping_cart.py` — shopping cart with itemized receipt, discount and recently added items
- `data_cleaner.py` — 5-step data cleaning pipeline with quality report

## Key Concepts Covered

- List comprehensions — `[x for x in list if condition]` faster and cleaner than for loops
- `zip()` — combines two parallel lists into pairs
- `enumerate()` — gives index + value while looping
- `sorted()` with `lambda` — sort list of tuples by specific field
- List of dictionaries — each item stores multiple fields cleanly
- Data cleaning — remove None, empty strings, whitespace, duplicates, normalize case

## Research Summary — Python Lists & List Operations

> 📖 Full research notes and source comparisons are in `LEARNINGS.md`

- **ChatGPT:** List comprehensions are 35% faster than for loops — always prefer them for simple transformations
- **Gemini:** Use extend() instead of calling append() in a loop — faster and cleaner
- **Claude:** Use sorted() over sort() when you need to keep the original list unchanged
- **Article:** For large datasets use generators instead of list comprehensions — more memory efficient

## How to Run

```bash
python3 student_grade_manager.py
python3 shopping_cart.py
python3 data_cleaner.py
```
