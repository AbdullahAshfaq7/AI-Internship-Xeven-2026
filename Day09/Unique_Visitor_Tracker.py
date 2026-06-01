# day09/visitor_tracker.py
# Unique Visitor Tracker
# Author: Abdullah | Date: 2026-05-26

"""
Tracks website visitors using sets.
Demonstrates set operations: union, intersection, difference.
"""

# --- VISITOR DATA ---

# Sets automatically remove duplicates!
monday_visitors = {
    "192.168.1.1",
    "10.0.0.1",
    "172.16.0.5",
    "192.168.1.1",  # duplicate — automatically removed
}

tuesday_visitors = {
    "10.0.0.1",
    "192.168.2.10",
    "172.16.0.5",
    "10.0.0.99",
}

wednesday_visitors = {
    "192.168.2.10",
    "10.0.0.99",
    "172.16.0.5",
    "192.168.5.5",
}

# --- DISPLAY VISITORS ---
print(f"Monday visitors:    {monday_visitors}")
print(f"Tuesday visitors:   {tuesday_visitors}")
print(f"Wednesday visitors: {wednesday_visitors}")

# --- SET OPERATIONS ---

# Union — ALL unique visitors across all days
all_visitors = monday_visitors | tuesday_visitors | wednesday_visitors
print(f"\nTotal unique visitors: {len(all_visitors)}")
print(f"All visitors: {all_visitors}")

# Intersection — visited BOTH Monday AND Tuesday
common_mon_tue = monday_visitors & tuesday_visitors
print(f"\nVisited both Mon & Tue: {common_mon_tue}")

# Difference — ONLY on Monday, not Tuesday
only_monday = monday_visitors - tuesday_visitors
print(f"Only on Monday:         {only_monday}")

# Difference — ONLY on Tuesday, not Monday
only_tuesday = tuesday_visitors - monday_visitors
print(f"Only on Tuesday:        {only_tuesday}")

# Symmetric difference — visited only ONE day
one_day_only = monday_visitors ^ tuesday_visitors
print(f"Visited only one day:   {one_day_only}")

# --- METRICS ---

# Retention rate — Monday visitors who came back Tuesday
returning = monday_visitors & tuesday_visitors
retention_rate = len(returning) / len(monday_visitors) * 100
print(f"\nRetention rate: {retention_rate:.1f}%")

# Growth rate — new visitors on Tuesday
new_tuesday = tuesday_visitors - monday_visitors
growth_rate = len(new_tuesday) / len(monday_visitors) * 100
print(f"Growth rate:    {growth_rate:.1f}%")

# --- ADD NEW VISITOR ---
print(f"\nBefore add: {wednesday_visitors}")
wednesday_visitors.add("10.0.0.200")
print(f"After add:  {wednesday_visitors}")

# --- REMOVE VISITOR ---
wednesday_visitors.discard("10.0.0.99")
print(f"After remove: {wednesday_visitors}")
