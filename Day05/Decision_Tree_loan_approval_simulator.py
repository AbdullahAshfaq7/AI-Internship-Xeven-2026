# day05/Decision_Tree_loan_approval_simulator.py
# Decision Tree Loan Approval Simulator
# Author: Abdullah | Date: 19-06-2026

"""
Simulates a Decision Tree for loan approval.
Shows how a real Decision Tree makes decisions step by step.
"""


def evaluate_loan(name, age, income, credit_score):
    path = []  # noqa: F841

    # Node 1: Age Check
    if age < 18:
        path.append("Age < 18: Reject")
        return {"Approved": False, "Reason": "Applicant is underage", "Path": path}
    path.append("Age >= 18: Continue")

    # Node 2: Income Check
    if income < 30000:
        path.append("Income < $30,000: Reject")
        return {"Approved": False, "Reason": "Income too low", "Path": path}
    path.append("Income >= $30,000: Continue")

    # Node 3: Credit Score Check
    if credit_score < 600:
        path.append("credit_score < 600: Reject")
        return {"Approved": False, "Reason": "Credit score too low", "Path": path}
    path.append("credit_score >= 600: Approve")

    return {"Approved": True, "Reason": "All criteria met", "Path": path}


def print_results(name, result):
    """Printing the Decision Results with Full Path"""
    print(f"Decision for {name}:")
    print(f"Status: {result['Approved']}:)")  # noqa: F821
    print(f"Reason: {result['Reason']}")
    print("Decision Path:")
    for step in result["Path"]:
        print(f" - {step}")


# Test the Decision Tree Simulator with different applicants
applicants = [
    {"name": "Abdullah", "age": 25, "income": 100000, "credit_score": 900},
    {"name": "Aybe", "age": 17, "income": 40000, "credit_score": 650},
    {"name": "Orhan", "age": 30, "income": 60000, "credit_score": 750},
]

print("=" * 50)
print("     LOAN APPROVAL DECISION TREE")
print("=" * 50)

for applicant in applicants:
    results = evaluate_loan(
        applicant["name"],
        applicant["age"],
        applicant["income"],
        applicant["credit_score"],
    )
    print_results(applicant["name"], results)


print("\n" + "=" * 50)
