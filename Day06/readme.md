# Day 06 — Python Lists

## Files

| File                    | Description                               |
|-------------------------|-------------------------------------------|
| `student_management.py` | All list operations demonstrated          |
| `grade_tracker.py`      | Parallel lists with grade analysis        |
| `list_slicing.py`       | All slicing patterns on numbers 1-20      |
| `LEARNINGS.md`          | Detailed research notes and key takeaways |
| `README.md`             | This file                                 |

## What I Built

- `student_management.py` — demonstrates all list operations: create, add, remove, slice, sort
- `grade_tracker.py` — tracks student grades using parallel lists, finds highest, lowest and average
- `list_slicing.py` — demonstrates all slicing patterns on a list of numbers 1 to 20

## Key Concepts Covered

- Lists — ordered, mutable, mixed data types, 0-indexed
- Indexing — positive (`list[0]`) and negative (`list[-1]`)
- Slicing — `list[1:4]`, `list[:5]`, `list[-5:]`, `list[::2]`, `list[::-1]`
- Adding — `append()`, `insert()`, `extend()`
- Removing — `remove()`, `pop()`, `clear()`
- Methods — `sort()`, `reverse()`, `count()`, `index()`, `len()`

## Research Summary — Python Lists & List Methods

> Full research notes and source comparisons are in `LEARNINGS.md`

- **ChatGPT:** Use `append()` over `insert()` whenever possible — it is much faster for large lists
- **Gemini:** Use `extend()` for adding multiple items — faster than calling `append()` in a loop
- **Claude:** `list[-1]` is cleaner than `list[len(list)-1]` — always use negative indexing from end
- **Article:** `sort()` modifies in place — use `sorted()` when you need to keep original list unchanged

## How to Run

```bash
python3 student_management.py
python3 grade_tracker.py
python3 list_slicing.py
```
