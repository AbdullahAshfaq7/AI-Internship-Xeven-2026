# Day 04 — Operators & Type Conversion

## Files

| File              | Description                                              |
|-------------------|----------------------------------------------------------|
| `operators.py`    | All arithmetic operators, precedence and type conversion |
| `login_system.py` | Login validator with username, password and age checks   |
| `LEARNINGS.md`    | Detailed research notes and key takeaways                |
| `README.md`       | This file                                                |

## What I Built

- `operators.py` — demonstrates all 7 arithmetic operators, precedence and type conversion
- `login_system.py` — multi-condition login validator using logical operators and type conversion

## Key Concepts Covered

- Arithmetic operators: `+`, `-`, `*`, `/`, `//`, `%`, `**`
- Operator precedence — BODMAS rule, use brackets when in doubt
- Type conversion — implicit (automatic) vs explicit (manual)
- Logical operators — `and`, `or`, `not`
- `ValueError` — only happens during type conversion, not with strings

## Research Summary — Operators & Type Conversion

> Full research notes and source comparisons are in `LEARNINGS.md`

- **ChatGPT:** Always use brackets to make operator precedence clear — never rely on memory
- **Gemini:** Always validate before converting — str to int crashes if string is not a number
- **Claude:** `num % 2 == 0` is the cleanest way to check if a number is even
- **Article:** Explicit conversion is always better than implicit — be clear about what you're doing

## How to Run

```bash
python3 operators.py
python3 login_system.py
```
