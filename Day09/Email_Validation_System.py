# day09/email_validator.py
# Email Validation System
# Author: Abdullah | Date: 01-06-2026

"""
Validates emails using sets.
Demonstrates set membership, operations and duplicate prevention.
"""

# --- VALID DOMAINS --- stored as a set for fast lookup

valid_domains = {"icloud.com", "gmail.com", "yahoo.com", "hotmail.com", "outlook.com"}

# --- REGISTERED EMAILS --- set prevents duplicates automatically

registered_emails = set()

# --- FUNCTIONS ---


def validate_email(email):
    """
    Validate email address.
    Checks @ symbol and domain against valid domains set.
    Returns (bool, message) tuple.
    """

    if "@" not in email:
        return False, "Invalid email: missing '@' symbol."

    # Split email into username and domain
    parts = email.split("@")  # noqa: F841

    if len(parts) != 2:
        return False, "Invalid Email Format"

    username, domain = parts

    # Check username is not empty
    if not username:
        return False, "Username cannot be empty"

    # Check domain is in valid set — O(1) fast lookup!
    if domain not in valid_domains:
        return False, f"Invalid domain: {domain}"

    return True, "Valid email"


def register_email(email):
    """
    Register an email address.
    Set automatically prevents duplicates.
    """
    is_valid, message = validate_email(email)

    if not is_valid:
        print(f"Cannot register {email} — {message}")
        return

    if email in registered_emails:
        print(f"{email} is already registered!")
        return

    registered_emails.add(email)
    print(f"Registered: {email}")


def get_emails_by_domain(emails, domain):
    """
    Get all emails from a specific domain.
    Uses set comprehension to filter.
    """
    return {email for email in emails if email.split("@")[1] == domain}


# --- MAIN PROGRAM ---

# Test emails
test_emails = [
    "ali@gmail.com",
    "sara@yahoo.com",
    "ahmed@gmail.com",
    "test@fake.com",
    "notanemail",
    "@gmail.com",
    "omar@outlook.com",
]

# Validate each email
print("=== Email Validation ===")
for email in test_emails:
    is_valid, message = validate_email(email)
    status = "✅ Valid" if is_valid else f"❌ {message}"
    print(f"{email:<25} → {status}")

# Register emails
print("\n=== Registering Emails ===")
register_email("ali@gmail.com")
register_email("sara@yahoo.com")
register_email("ahmed@gmail.com")
register_email("ali@gmail.com")  # duplicate!
register_email("test@fake.com")  # invalid domain!

# Show registered emails
print(f"\nTotal registered: {len(registered_emails)}")
print(f"Registered: {registered_emails}")

# Filter by domain
print("\n=== Emails by Domain ===")
gmail_users = get_emails_by_domain(registered_emails, "gmail.com")
yahoo_users = get_emails_by_domain(registered_emails, "yahoo.com")
print(f"Gmail users: {gmail_users}")
print(f"Yahoo users: {yahoo_users}")

# Set operations on domains
registered_domains = {email.split("@")[1] for email in registered_emails}
print(f"\nRegistered domains: {registered_domains}")
missing_domains = valid_domains - registered_domains
print(f"Domains with no users: {missing_domains}")
