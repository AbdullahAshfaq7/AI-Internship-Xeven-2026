# Day 06 — Learnings

## Topic: Python Lists

---

## Theory Studied

### What is a List?

- Ordered — items stay in the order you put them
- Mutable — you can change, add and remove items anytime
- Mixed types — can hold int, str, bool, float all together
- 0-indexed — first item is always at position 0

### Indexing

- Positive: `list[0]` = first, `list[1]` = second
- Negative: `list[-1]` = last, `list[-2]` = second from last

### Slicing

- `list[1:4]` — items at index 1, 2, 3 (not 4)
- `list[:5]` — first 5 items
- `list[-5:]` — last 5 items
- `list[::2]` — every 2nd item
- `list[::-1]` — entire list reversed

### Adding Items

- `append()` — adds ONE item to the end
- `insert(i, x)` — adds item at specific position
- `extend()` — adds MULTIPLE items from another list

### Removing Items

- `remove(x)` — removes first occurrence by VALUE
- `pop(i)` — removes by INDEX and returns the item
- `clear()` — removes everything from the list

### List Methods

- `sort()` — sorts in place A-Z or 0-9
- `reverse()` — reverses in place
- `count(x)` — counts how many times x appears
- `index(x)` — returns index of first occurrence of x
- `len()` — returns total number of items

---

## Task 1 — Student Management System

- Created list of 5 students and performed all operations
- Used `append()` to add Bilal to end
- Used `insert(2, "Hina")` to add Hina at position 2
- Used `extend()` to add multiple students at once
- Used `remove()` to delete by name
- Used `pop(0)` to remove and return first student
- Used `clear()` on a temp list to show it empties everything
- Demonstrated all slicing patterns and list methods

---

## Task 2 — Grade Tracker

- Used two parallel lists: names and grades
- Used `max()` and `min()` with `index()` to find top and lowest student
- Used `sum() / len()` to calculate average
- Used list comprehension to filter passed and failed students
- Learned that parallel lists must stay in sync — same index = same student

---

## Task 3 — List Slicing Practice

- Used `list(range(1, 21))` to create numbers 1 to 20
- `[:5]` = first 5, `[-5:]` = last 5
- `[::3]` = every 3rd item
- `[::-1]` = entire list reversed
- `[5:15]` = middle 10 elements

---

## Research Task — Python Lists & List Methods

### ChatGPT

**Question:** Explain list operations with practical examples
**Key Points:** Lists are the most used data structure in Python. append() is O(1) — very fast. insert() at position 0 is O(n) — slow for large lists.
**Best Insight:** Use append() over insert() whenever possible — it is much faster for large lists.

---

### Gemini

**Question:** When should I use append() vs insert() vs extend()?
**Key Points:** append() for adding one item to end. insert() when position matters. extend() for merging two lists.
**Best Insight:** extend() is faster than calling append() in a loop — always prefer extend() for adding multiple items.

---

### Claude

**Question:** Explain list operations with practical examples
**Key Points:** Negative indexing makes code more readable. List comprehensions are faster than for loops for filtering. Always handle IndexError when accessing by index.
**Best Insight:** list[-1] is cleaner than list[len(list)-1] — use negative indexing whenever accessing from the end.

---

### Article

**Topic:** Python Lists: A Complete Guide for Beginners
**Key Points:** Lists are dynamic — they grow and shrink automatically. Slicing creates a new list — it does not modify the original. sort() modifies in place, sorted() returns a new list.
**Best Insight:** sorted() is safer than sort() when you need to keep the original list unchanged.

---

- ## Performance Considerations

- `append()` — O(1) fast — always use for adding to end
- `insert(0, x)` — O(n) slow — shifts all items for large lists
- `remove(x)` — O(n) slow — searches entire list for value
- `pop()` — O(1) fast — removes last item instantly
- `pop(0)` — O(n) slow — shifts all items after removal

---

## What I Learned Today

- Lists are ordered, mutable and can hold mixed data types
- 0-indexed — always starts at 0 not 1
- Negative indexing: -1 is last, -2 is second last
- append() is faster than insert() for large lists
- extend() is faster than calling append() in a loop
- Slicing creates a new list — original stays unchanged
- sort() modifies in place — sorted() returns a new list
- Always handle IndexError when accessing by index

---

## References

1. ChatGPT — <https://chat.openai.com> — 20-05-2026
2. Gemini — <https://gemini.google.com> — 20-05-2026
3. Claude — <https://claude.ai> — 20-05-2026
