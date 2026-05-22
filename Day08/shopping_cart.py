# day08/shopping_cart.py
# Shopping Cart System
# Author: Abdullah | Date: 22-05-2026

"""
Shopping cart using lists.
Demonstrates list operations, slicing and functions.
"""

# --- FUNCTIONS ---


def add_items(cart, name, price, quantity):
    """Add Item To Cart"""
    cart.append({"name": name, "price": price, "quantity": quantity})
    print(f"Added: {name} x{quantity} @ ${price:.2f}")


def remove_item(cart, name):
    """Remove Item From Cart"""
    for item in cart:
        if item["name"] == name:
            cart.remove(item)
            print(f"Removed: {name}")
            return
        print(f"{name} not found in cart")


def update_quantity(cart, name, quantity):
    for item in cart:
        if item["name"] == name:
            old_qty = item["quantity"]  # noqa: F841
            item["quantity"] = quantity
            print(f"Updated: {name} quantity {old_qty} -> {quantity}")
            return
        print(f"{name} not found in the cart")


def calculate_total(cart):
    return sum(item["price"] * item["quantity"] for item in cart)


def display_receipt(cart):
    print("\n=== SHOPPING RECEIPT === ")
    for i, item in enumerate(cart, start=1):
        subtotal = item["price"] * item["quantity"]
        print(
            f" {i}, {item['name']:>10} x{item['quantity']} @ ${item['price']:.2f} = ${subtotal:.2f}"
        )


def get_recent_items(cart, n=3):
    """Return Recent n Items Added To Cart"""
    return [item["name"] for item in cart[-n:]]


# --- MAIN PROGRAM ---

cart = []
add_items(cart, "Apple", 0.99, 5)
add_items(cart, "Bread", 2.49, 2)
add_items(cart, "Milk", 3.99, 1)
add_items(cart, "Eggs", 2.99, 1)

# Update quantity of an item
update_quantity(cart, "Milk", 3)

# remove an item
remove_item(cart, "Bread")

# Display receipt
display_receipt(cart)

# Get recent items
print(f"Recent Items: {get_recent_items(cart)}")
