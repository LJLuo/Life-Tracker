import json
from datetime import date
import os

DATA_FILE = "data/habits.json"

def log_habit():
    habit = input("Enter one habit you completed today: ")
    today = str(date.today())

    data = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)

    if today not in data:
        data[today] = []

    data[today].append(habit)

    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent = 2)

    print(f"Habit '{habit}' logged for {today}.")


def view_habit_summary():
    if not os.path.exists(DATA_FILE):
        print("No habit data found.")
        return

    with open(DATA_FILE, 'r') as f:
        data = json.load(f)

    for day, habits in data.items():
        print(f"{day}: {', '.join(habits)}")