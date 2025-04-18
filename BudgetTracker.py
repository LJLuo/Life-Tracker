import json
import os
from datetime import date

DATA_FILE = "data/expenses.json"

def log_expense():
    amount = float(input("Enter expense amount: $"))
    category = input("Enter category (e.g., food, transport): ")
    today = str(date.today())

    expense = {
        "amount": amount,
        "category": category,
        "date": today
    }

    expenses = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            expenses = json.load(f)

    expenses.append(expense)

    with open(DATA_FILE, 'w') as f:
        json.dump(expenses, f, indent = 2)

    print(f"Logged ${amount} for {category} on {today}.")

def view_expense_summary():
    if not os.path.exists(DATA_FILE):
        print("Sorry! No expenses found.")
        return

    with open(DATA_FILE, 'r') as f:
        expenses = json.load(f)

    total = 0
    for exp in expenses:
        print(f"{exp['date']}: ${exp['amount']} - {exp['category']}")
        total += exp['amount']

    print(f"\nTotal spent: ${total:.2f}")
