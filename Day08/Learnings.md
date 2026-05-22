# Day 08 — Learnings

## Topic: Lists & List Operations Deep Dive

---

## 📚 Theory Studied

### List Comprehensions

- Concise one-line way to create lists
- Basic: `[x for x in list]`
- With condition: `[x for x in list if condition]`
- With transformation: `[x.upper() for x in list]`
- Faster and cleaner than for loop + append()

### zip()

- Combines two lists into pairs
- `for name, grade in zip(names, grades)`
- Both lists must be in sync — same index = same student
- Returns pairs as tuples: `("Ali", 88)`

### enumerate()

- Gives index AND value while looping
- `for i, name in enumerate(names, start=1)`
- Cleaner than using range(len(list))

### sorted() vs sort()

- `sort()` — modifies original list in place
- `sorted()` — returns new sorted list, original unchanged
- Both support `reverse=True` for descending order
- `key=lambda x: x[1]` — sort by second item in tuple

### Lambda

- One-line anonymous function
- `lambda x: x[1]` = "take x and return x[1]"
- Used with sorted(), map(), filter()

---

## Task 1 — Student Grade Manager

- Built 6 functions: add, remove, update, average, top students, above/below average
- Used `zip()` to pair names and grades together
- Used `sorted()` with `lambda` to sort by grade descending
- Used list comprehension to filter above/below average students
- Bug fixed: used `name[i]` instead of `names[i]` — was indexing string characters

---

## Task 2 — Shopping Cart System

- Used list of dictionaries — each item has name, price, quantity keys
- Built add, remove, update, total, receipt and recent items functions
- Applied 10% discount when total exceeds $100
- Used slicing `cart[-3:]` for recently added items
- Bug fixed: capitalized keys `"Name"` vs lowercase `"name"` caused KeyError
- Bug fixed: `item[quantity]` instead of `item["quantity"]` in update function
- Bug fixed: receipt totals were inside the loop instead of outside

---

## Task 3 — Data Cleaning Pipeline

- Simulated a real data cleaning pipeline in 5 steps
- Step 1: Remove None values using `if item is not None`
- Step 2: Remove empty strings using `if item.strip() != ""`
- Step 3: Strip whitespace using `item.strip()`
- Step 4: Normalize to Title Case using `item.title()`
- Step 5: Remove duplicates while preserving order
- Generated data quality report with completeness percentage
- Learned: in real AI projects 80% of work is data cleaning

---

## Research Task — Python Lists & List Operations

### ChatGPT

**Question:** Explain list operations with practical examples
**Key Points:** List comprehensions are 35% faster than for loops. zip() stops at shortest list. enumerate() is cleaner than range(len()).
**Best Insight:** Always use list comprehension for simple transformations — it is faster and more readable.

---

### Gemini

**Question:** When should I use append() vs insert() vs extend()?
**Key Points:** append() for single items to end. insert() when position matters. extend() for merging lists.
**Best Insight:** Use extend() instead of calling append() in a loop — it is faster and cleaner.

---

### Claude

**Question:** Explain list operations with practical examples
**Key Points:** List comprehensions can replace map() and filter(). zip() is memory efficient. sorted() is safer than sort() for keeping originals.
**Best Insight:** Use sorted() over sort() when you need to keep the original list unchanged — sort() is destructive.

---

### Article

**Topic:** Python Lists: A Complete Guide
**Key Points:** Lists are dynamic arrays in memory. Appending is O(1) but inserting at position 0 is O(n). List comprehensions create a new list in memory.
**Best Insight:** For large datasets use generators instead of list comprehensions — they are memory efficient.

---

## What I Learned Today

- List comprehensions are faster and cleaner than for loops
- zip() pairs two lists together — both must stay in sync
- enumerate() gives index + value — cleaner than range(len())
- sorted() returns new list, sort() modifies in place
- lambda is a one-line function used for sorting and filtering
- Dictionary keys must be consistent — capitalize causes KeyError
- Indentation inside loops matters — totals must be outside the loop
- Data cleaning is 80% of real AI work — clean data = good model

---

## References

1. ChatGPT — <https://chat.openai.com> — 2026-05-22
2. Gemini — <https://gemini.google.com> — 2026-05-22
3. Claude — <https://claude.ai> — 2026-05-22
