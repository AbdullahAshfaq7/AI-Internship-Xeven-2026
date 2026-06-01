# Day 09 — Tuples & Sets

## Files

| File                 | Description                                                  |
|----------------------|--------------------------------------------------------------|
| `coordinates.py`     | Tuple-based geographic coordinates with distance calculation |
| `visitor_tracker.py` | Set-based visitor tracking with set operations               |
| `email_validator.py` | Email validation using sets for domains and registered emails|
| `LEARNINGS.md`       | Detailed research notes and key takeaways                    |
| `README.md`          | This file                                                    |

## What I Built

- `coordinates.py` — geographic coordinates system using tuples with distance calculation
- `visitor_tracker.py` — unique visitor tracker using sets with union, intersection and difference
- `email_validator.py` — email validation system using sets for domain lookup and duplicate prevention

## Key Concepts Covered

- Tuples — immutable, ordered, use for fixed data like coordinates
- Tuple unpacking — `name, lat, lon = city` cleaner than indexing
- Sets — unordered, unique items only, O(1) fast lookup
- Set operations — union, intersection, difference, symmetric difference
- Set comprehension — `{x for x in items if condition}`
- discard() vs remove() — discard() never crashes if item not found

## Research Summary — Tuples & Sets

> Full research notes and source comparisons are in `LEARNINGS.md`

- **ChatGPT:** Use tuple for fixed data, set for uniqueness, list for everything else
- **Gemini:** Set operations are faster than looping through lists to find common items
- **Claude:** Always unpack tuples — `name, lat, lon = city` is cleaner than `city[0]`
- **Article:** Use discard() over remove() — silently does nothing if item not found

## How to Run

```bash
python3 coordinates.py
python3 visitor_tracker.py
python3 email_validator.py
```
