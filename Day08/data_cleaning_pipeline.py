# day08/data_cleaner.py
# Data Cleaning Pipeline
# Author: Abdullah | Date: 22-05-2026

"""
Cleans messy data step by step using list comprehensions.
Demonstrates real-world data cleaning pipeline.
"""

# --- MESSY DATA ---
raw_data = [
    "  ali  ",
    "SARA",
    None,
    "ali",
    "  AHMED  ",
    "",
    "sara",
    None,
    "  AHMED  ",
    "hina",
]

print(f"Original Data:  {raw_data}")
print(f"Original Count: {len(raw_data)}\n")

# --- STEP 1: Remove None values ---
step1 = [item for item in raw_data if item is not None]
print(f"Step 1 - Remove None:    {step1}")

# --- STEP 2: Remove empty strings ---
step2 = [item for item in step1 if item.strip() != ""]
print(f"Step 2 - Remove empty:   {step2}")

# --- STEP 3: Strip whitespace ---
step3 = [item.strip() for item in step2]
print(f"Step 3 - Strip spaces:   {step3}")

# --- STEP 4: Normalize to Title Case ---
step4 = [item.title() for item in step3]
print(f"Step 4 - Title case:     {step4}")

# --- STEP 5: Remove duplicates (keep order) ---
seen = []
step5 = [seen.append(item) or item for item in step4 if item not in seen]
print(f"Step 5 - Remove dupes:   {step5}")

# --- DATA QUALITY REPORT ---
print("\n--- Data Quality Report ---")
print(f"Original count:  {len(raw_data)}")
print(f"Final count:     {len(step5)}")
print(f"Removed:         {len(raw_data) - len(step5)}")
print(f"Completeness:    {len(step5) / len(raw_data) * 100:.1f}%")
