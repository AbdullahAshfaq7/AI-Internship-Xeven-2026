# Day 05 — Learnings

## 1. What is Machine Learning?

AI is the big umbrella. ML is under it:

AI
└── Machine Learning — learns patterns from data
    └── Deep Learning — uses neural networks
        ├── NLP — understands text (what you'll build!)
        └── Computer Vision — understands images

### Simple definition

Instead of programming rules manually, you show the computer thousands of examples and it learns the rules itself.

## 2. Three Types of ML

### Supervised Learning

You give it labeled data (input + correct answer)
It learns to predict the answer for new inputs
Example: Show 1000 emails labeled spam/not spam → it learns to detect spam

### Unsupervised Learning

You give it unlabeled data (input only, no answers)
It finds patterns and groups on its own
Example: Give it customer data → it groups similar customers together

### Reinforcement Learning

Agent learns by trial and error
Gets reward for good actions, penalty for bad ones
Example: Game AI — learns to play chess by playing millions of games

## 3. Regression vs Classification

RegressionClassificationOutputA numberA categoryExamplePredict house priceSpam or not spamExamplePredict temperatureCat or dogExamplePredict salaryPass or fail

## 4. Decision Trees

Think of it as a flowchart of yes/no questions:
Is age > 18?
├── YES → Has income > 30,000?
│         ├── YES → APPROVED
│         └── NO  → REJECTED
└── NO  → REJECTED

Each question splits the data into smaller groups until it reaches a final answer.

## Task 1 — ML Concepts Explorer

- Built supervised learning demo — spam detector using keywords
- Built unsupervised learning demo — customer grouping by age
- Built reinforcement learning demo — agent scoring with rewards and penalties
- Built regression vs classification demo — house prices vs pass/fail
- Used `append()` to build lists dynamically inside loops
- Used tuple unpacking: `for age, spending, name in customer_data`

---

## Task 2 — Decision Tree Simulator

- Built `evaluate_loan()` with 3 decision nodes: age, income, credit score
- Used `path = []` list to track every decision made
- Used `append()` to add each step to the path
- Built `print_result()` to display decision with full path
- Tested 5 applicants with different scenarios — approved and rejected cases
- Learned that explainability is critical in real AI — showing WHY a decision was made

---

## Research Task — ML Concepts & Decision Trees

### ChatGPT

**Question:** What are best practices for implementing Decision Trees?
**Key Points:** Keep trees shallow to avoid overfitting. Always track decision paths for explainability. Validate input data before feeding to the tree.
**Best Insight:** A decision tree that explains its reasoning is more valuable in production than one that is just accurate.

---

### Gemini

**Question:** What is the difference between supervised and unsupervised learning?
**Key Points:** Supervised needs labeled data — expensive to collect. Unsupervised finds hidden patterns — useful for exploration. Most real problems use supervised learning.
**Best Insight:** The quality of your labeled training data matters more than the algorithm you choose.

---

### Claude

**Question:** How does reinforcement learning differ from supervised learning?
**Key Points:** RL learns from interaction with environment, not from a fixed dataset. Reward function design is the hardest part. RL is used in robotics, games and autonomous systems.
**Best Insight:** In RL the agent does not need a teacher — it discovers the best strategy through millions of trials.

---

### Article

**Topic:** Introduction to Machine Learning concepts
**Key Points:** ML is pattern recognition at scale. The three types serve different problems. Decision trees are the most interpretable ML algorithm.
**Best Insight:** Always start with the simplest model — a decision tree — before trying complex neural networks.

---

## What I Learned Today

- ML learns patterns from data instead of following manually coded rules
- Supervised = labeled data, Unsupervised = unlabeled, Reinforcement = rewards
- Regression predicts numbers, Classification predicts categories
- Decision trees make decisions through a chain of yes/no questions
- `append()` adds items to the end of a list dynamically
- Explainability — showing WHY a decision was made — is as important as accuracy
- tuple unpacking makes loops clean: `for age, score, name in data`

---

## References

1. ChatGPT — <https://chat.openai.com> — 2026-05-19
2. Gemini — <https://gemini.google.com> — 2026-05-19
3. Claude — <https://claude.ai> — 2026-05-19
4. Article — 2026-05-19
