import time
import json
import os
from datetime import datetime

DATA_FILE = "data/work_sessions.json"

def start_work_session():
    label = input("What are you working on? ")

    input("Press Enter to START the timer...")
    start = time.time()

    input("Press Enter to STOP the timer...")
    end = time.time()

    elapsed = end - start
    minutes = int(elapsed // 60)
    seconds = int(elapsed % 60)

    print(f"You worked on '{label}' for {minutes}m {seconds}s.")

    session = {
        "label": label,
        "duration": round(elapsed, 2),
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    sessions = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            sessions = json.load(f)

    sessions.append(session)

    with open(DATA_FILE, 'w') as f:
        json.dump(sessions, f, indent=2)

    print("Work session saved!")

def get_worktime_today():
    total_worktime = 0
    today = datetime.now().strftime("%Y-%m-%d")
    if not os.path.exists(DATA_FILE):
        print("Sorry! No sessions found.")
        return

    with open(DATA_FILE, 'r') as f:
        work_times = json.load(f)

    for worktime in work_times:
        if worktime.get("timestamp", "").startswith(today):
            total_worktime += worktime.get("duration", 0)

    minute = int(total_worktime // 60)
    second = int(total_worktime % 60)

    print(f"Your total work time today ({today}): {minute}m and {second}s")

