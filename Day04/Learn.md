# Day 04 — Learnings

## Topic: Operators & Type Conversion

---

## Theory Studied

### Arithmetic Operators

| Operator | Name           | Example  | Result |
|----------|----------------|----------|------- |
| `+`      | Addition       | `10 + 3` | `13`   |
| `-`      | Subtraction    | `10 - 3` | `7`    |
| `*`      | Multiplication | `10 * 3` | `30`   |
| `/`      | Division       | `10 / 3` | `3.333`|
| `//`     | Floor Division | `10 // 3`| `3`    |
| `%`      | Modulus        | `10 % 3` | `1`    |
| `**`     | Power          | `2 ** 3` | `8`    |

### Operator Precedence — BODMAS

- `**` runs first
- then `*`, `/`, `//`, `%`
- then `+`, `-`
- Use brackets when in doubt — `(2 + 3) * 4`

### Type Conversion

- **Implicit** — Python does it automatically: `5 + 3.0 = 8.0` (int + float = float)
- **Explicit** — you do it manually: `int()`, `float()`, `str()`, `bool()`
- `bool(0)` = False, `bool(1)` = True, `bool("")` = False, `bool("hi")` = True
- `ValueError` happens when converting a non-numeric string: `int("abc")` crashes

### Logical Operators

- `and` — both conditions must be True
- `or` — at least one must be True
- `not` — flips True to False and False to True

---

## Task 1 — Operators Explorer

- Demonstrated all 7 arithmetic operators with real examples
- Showed operator precedence: `2 + 3 * 4 = 14` not 20
- Showed implicit and explicit type conversion with type() checks
- Showed bool conversion: 0 and empty string are False, everything else is True

---

## Task 2 — Login System

- Built 3 separate validation functions: validate_username, validate_password, validate_age
- Each returns a (bool, message) tuple — clean and reusable
- Used `and` operator — ALL 3 conditions must pass for login to succeed
- Used `any()` with generator to check for digits and uppercase in password
- try/except only needed for age — only place where type conversion happens

---

## Research Task — Operators & Type Conversion

### ChatGPT

**Question:** How do arithmetic operators work in Python?
**Key Points:** Python follows BODMAS. `/` always returns float. `//` floors the result. `%` gives remainder.
**Best Insight:** Always use brackets to make operator precedence clear — never rely on memory.

---

### Gemini

**Question:** Explain type conversion in Python with examples
**Key Points:** Implicit conversion happens automatically. Explicit conversion is done manually with int(), float(), str(), bool().
**Best Insight:** Always be careful converting str to int — it will crash if the string is not a number.

---

### Claude

**Question:** What are best practices for using operators in Python?
**Key Points:** Use brackets for clarity. Use `//` for whole number division. Use `%` to check even/odd numbers.
**Best Insight:** `num % 2 == 0` is the cleanest way to check if a number is even.

---

### Article

**Topic:** Python operators and type conversion
**Key Points:** Type conversion is one of the most common sources of bugs. Always validate before converting. Use explicit conversion over implicit whenever possible.
**Best Insight:** Explicit is always better than implicit — Python even says so in its own design philosophy.

---

## What I Learned Today

- `/` always returns float — use `//` when you need a whole number
- `%` modulus gives the remainder — useful for even/odd checks
- Operator precedence follows BODMAS — use brackets to be safe
- `ValueError` only happens during type conversion — not with strings
- `any()` is a clean way to check if any character meets a condition
- All validation functions should return `(bool, message)` tuple for consistency
- `and` requires ALL conditions True — `or` requires just ONE

---

## References

1. ChatGPT — <https://chat.openai.com> — 2026-05-18
2. Gemini — <https://gemini.google.com> — 2026-05-18
3. Claude — <https://claude.ai> — 2026-05-18
4. Article — [paste your article URL here] — 2026-05-18
