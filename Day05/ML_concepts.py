# day05/ML_concepts.py
# Machine Learning Concepts in Python.
# Author: Abdullah | Date: 19-06-2026

# --- SUPERVISED LEARNING SIMULATOR ---
"""
Simulates supervised learning — model learns from labeled data.
Example: Email spam detector based on keywords.

"""


def supervised_learning_demo():
    print("=== Supervised Learning — Spam Detector ===")

    # Training data — labeled examples (input, label)
    training_data = [
        ("free money now", "spam"),
        ("congratulations you won", "spam"),
        ("let's meet at 3pm", "not spam"),
        ("please review the document", "not spam"),
    ]
    print(f"Trained on {len(training_data)} labeled examples")

    spam_keywords = [
        "free",
        "money",
        "won",
        "click",
    ]  # noqa: F841

    def predict(email):
        # Simple rule-based prediction based on keywords
        email_lower = email.lower()  # noqa: F841
        for keyword in spam_keywords:
            if keyword in email_lower:
                return "spam"
        return "not spam"

    # Test the model on new emails
    # Test the model

    test_emails = [
        "win a free iPhone today",
        "team lunch on Friday",
        "click here to claim prize",
        "please send the report",
    ]

    for email in test_emails:
        prediction = predict(email)
        print(f"Email: '{email}'")
        print(f"Prediction: {prediction}\n")


# --- UNSUPERVISED LEARNING SIMULATOR ---
"""
Simulates unsupervised learning — finds patterns without labels.
    Example: Groups customers by age automatically.
"""


def unsupervised_learning_demo():
    print("=== Unsupervised Learning — Customer Grouping ===")

    # Sample customer data (age, spending score, name)
    customer_data = [
        (25, 80, "Mohammad"),
        (30, 60, "Abdullah"),
        (22, 90, "Jess"),
        (35, 40, "Ronaldo"),
        (28, 70, "Messi"),
        (40, 30, "Neymar"),
    ]
    print(f"Analyzing {len(customer_data)} customers without labels")

    Young = []
    Middle = []
    Older = []

    for age, spending_score, name in customer_data:
        if age < 30:
            Young.append(name)
        elif 30 <= age < 40:
            Middle.append(name)
        else:
            Older.append(name)

            # Show Results
            print(f"Young Customers: {Young}")
            print(f"Middle-aged Customers: {Middle}")
            print(f"Older Customers: {Older}")


#  --- REINFORCEMENT LEARNING SIMULATOR ---
"""
    Simulates reinforcement learning — learns by reward and penalty.
    Example: Simple agent learning to avoid obstacles.
    
"""


def reinforcement_learning_demo():
    print("=== Reinforcement Learning — Reward System ===")

    # Simulated environment with rewards and penalties
    action = [  # noqa: F841
        ("move forward", "reward", +10),
        ("hit obstacle", "penalty", -20),
        ("collect coin", "reward", +5),
        ("fall into pit", "penalty", -50),
    ]

    total_score = 0  # noqa: F841
    for act, outcome, points in action:
        total_score += points
        print(f"Action: {act} | Outcome: {outcome} | {points:+d} {points}")
    print(f"Total Score: {total_score}")
    print("Agent learns to maximize rewards and minimize penalties over time.")


# --- REGRESSION VS CLASSIFICATION ---
"""
    Shows the difference between regression and classification.
"""


def regression_vs_classification():
    print("=== Regression vs Classification ===")

    # Regression — predicts a NUMBER

    print("Regression Examples (predicts a number):")
    house_sizes = [1000, 1500, 2000, 2500]

    # Simple formula: price = size * 100

    for size in house_sizes:
        price = size * 100
        print(f"  House size: {size} sqft → Predicted price: ${price:,}")

    print()

    # Classification — predicts a CATEGORY

    print("Classification Examples (predicts a category):")
    students = [
        ("Ali", 85),
        ("Sara", 45),
        ("Ahmed", 72),
        ("Zara", 30),
    ]

    for name, score in students:
        result = "Pass" if score >= 50 else "Fail"
        print(f"  {name} scored {score} → {result}")


# --- RUN ALL DEMOS ---

print("=" * 50)
print("       ML CONCEPTS EXPLORER — DAY 05")
print("=" * 50)
print()

supervised_learning_demo()
unsupervised_learning_demo()
reinforcement_learning_demo()
regression_vs_classification()
