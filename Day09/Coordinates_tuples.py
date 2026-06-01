# day09/coordinates.py
# Geographic Coordinates System
# Author: Abdullah | Date: 01-06-2026

"""
Stores city locations as tuples and calculates distances.
Demonstrates tuple packing, unpacking and immutability.
"""

import math  # noqa: F401

# --- CITY DATA — stored as tuples (name, latitude, longitude) ---
cities = [
    ("Lahore", 31.5497, 74.3436),
    ("Karachi", 24.8607, 67.0011),
    ("Islamabad", 33.6844, 73.0479),
]

# --- FUNCTIONS ---

""" 
Calculate distance between two coordinate tuples.
Uses Euclidean distance formula.
"""


def calculate_distance(coord1, coord2):

    # Unpack both tuples
    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # euclidean distance formula
    return math.sqrt((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2)


"""
Find closest city to a target coordinate.
Returns tuple of (city_name, distance).
"""


def find_closest_city(cities, target):

    # unpack target coordinate
    target_lat, target_lon = target

    closest_city = None  # noqa: F841
    closest_distance = float("inf")  # noqa: F841

    for city in cities:
        name, lat, lon = city  # unpack city tuple
        distance = calculate_distance((lat, lon), (target_lat, target_lon))

        if distance < closest_distance:
            closest_distance = distance
            closest_city = name  # noqa: F841

            return closest_city, round(closest_distance, 2)


def show_all_cities(cities):
    """Display all cities with their coordinates."""
    for city in cities:
        name, lat, lon = city
        print(f"{name}: ({lat}, {lon})")


# --- MAIN PROGRAM ---

# Display all cities
show_all_cities(cities)

# Calculate distance between two cities
lahore = cities[0][1], cities[0][2]  # (lat, lon)
karachi = cities[1][1], cities[1][2]

distance = calculate_distance(lahore, karachi)
print(f"\nDistance Lahore → Karachi: {distance:.2f} units")

# Find closest city to a target
target = (32.0, 72.0)
closest, dist = find_closest_city(cities, target)
print(f"Closest city to {target}: {closest} ({dist} units)")

# --- DEMONSTRATE IMMUTABILITY ---
print("\nTuple Immutability:")
city = ("Lahore", 31.55, 74.35)
print(f"Original tuple: {city}")

try:
    city[0] = "Karachi"  # this will fail!
except TypeError as e:
    print(f"TypeError: {e}")
    print("Tuples cannot be modified — this is intentional!")
