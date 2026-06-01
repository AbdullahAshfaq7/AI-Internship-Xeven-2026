# Day 09 — Learnings

## Topic: Tuples & Sets

## Theory Studied

### Tuples

- Immutable sequences — cannot be changed after creation
- Faster than lists — Python optimizes them internally
- Use for fixed data: coordinates, RGB colors, dates
- Syntax: `city = ("Lahore", 31.55, 74.35)`

### Tuple Packing & Unpacking

- Packing: putting values into a tuple `city = ("Lahore", 31.55, 74.35)`
- Unpacking: taking values out `name, lat, lon = city`
- Swap variables: `a, b = b, a`
- Return multiple values from functions: `return (city, distance)`

### Sets

- Unordered collections of unique items — no duplicates ever
- Fast membership lookup — O(1) vs O(n) for lists
- Syntax: `visitors = {"192.168.1.1", "10.0.0.1"}`
- Add: `set.add(x)` — Remove safely: `set.discard(x)`

### Set Operations

- Union `|` — all items from both sets
- Intersection `&` — items in BOTH sets
- Difference `-` — items in first but NOT second
- Symmetric difference `^` — items in ONE set only

### When to use what

| | Tuple | List | Set |
|---------|------|-----|
| Ordered | Yes | Yes | No |
| Mutable | No | Yes | Yes |
| Duplicates | Yes | Yes | No |
| Fast lookup | Yes | No | Yes |
| Use for | Fixed data | Ordered data | Unique data |

## Task 1 — Geographic Coordinates System

- Stored city data as tuples: (name, latitude, longitude)
- Used tuple unpacking: `name, lat, lon = city`
- Used Euclidean distance formula with math.sqrt()
- Used float("inf") as starting value for closest distance
- Demonstrated TypeError when trying to modify a tuple
- Returned result as tuple: `return (closest_city, distance)`

## Task 2 — Unique Visitor Tracker

- Used sets to automatically remove duplicate IP addresses
- Union | — all unique visitors across all days
- Intersection & — visitors who came on multiple days
- Difference - — visitors unique to one specific day
- Symmetric difference ^ — visitors who came on one day only
- Calculated retention rate and growth rate using set sizes

## Task 3 — Email Validation System

- Used set for valid_domains — O(1) fast lookup
- Used set for registered_emails — automatic duplicate prevention
- Split email with email.split("@") to get username and domain
- Used set comprehension: `{email for email in emails if condition}`
- Used set difference to find domains with no registered users

## Research Task — Tuples & Sets

### ChatGPT

**Question:** When should I use tuples vs lists vs sets?
**Key Points:** Tuples for fixed data, lists for ordered mutable data, sets for unique collections. Tuples are 20% faster than lists. Sets have O(1) lookup vs O(n) for lists.
**Best Insight:** If your data should never change — use a tuple. If you need uniqueness — use a set. Otherwise use a list.

### Gemini

**Question:** Explain set operations with practical examples
**Key Points:** Set operations are mathematical — same as Venn diagrams. Union combines, intersection finds common, difference finds exclusive items.
**Best Insight:** Set operations are much faster than looping through lists to find common or unique items.

### Claude

**Question:** What are best practices for using tuples in Python?
**Key Points:** Use tuples for heterogeneous data (different types together). Use named tuples for clarity. Always unpack tuples instead of indexing.
**Best Insight:** `name, lat, lon = city` is cleaner than `city[0], city[1], city[2]` — always unpack!

### Article

**Topic:** Python Tuples and Sets — Complete Guide
**Key Points:** Tuples are hashable — can be used as dictionary keys. Sets are implemented as hash tables. discard() is safer than remove() — never crashes.
**Best Insight:** Use discard() instead of remove() when you are not sure if the item exists — it silently does nothing if not found.

## What I Learned Today

- Tuples are immutable — use for data that should never change
- Tuple unpacking is cleaner than indexing: `name, lat, lon = city`
- Sets automatically remove duplicates — perfect for tracking unique items
- Set operations are faster than looping through lists
- O(1) lookup in sets vs O(n) in lists — sets are much faster for membership checks
- discard() is safer than remove() — does not crash if item not found
- Set comprehension: `{x for x in items if condition}`
- float("inf") is useful as a starting value when finding minimum

## References

1. ChatGPT — <https://chat.openai.com> — 2026-05-26
2. Gemini — <https://gemini.google.com> — 2026-05-26
3. Claude — <https://claude.ai> — 2026-05-26
4. Article
