from HabitTracker import log_habit, view_habit_summary
from BudgetTracker import log_expense, view_expense_summary
from WorkTimer import start_work_session, get_worktime_today


def main():
    while True:
        print("\n Life Tracker Menu: ")
        print("1. Log a habit")
        print("2. View habit summary")
        print("3. Log an expense")
        print("4. View expense summary")
        print("5. Start a work session")
        print("6. View work session summary")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            log_habit()
        elif choice == '2':
            view_habit_summary()
        elif choice == '3':
            log_expense()
        elif choice == '4':
            view_expense_summary()
        elif choice == '5':
            start_work_session()
        elif choice == '6':
            get_worktime_today()
        elif choice == '7':
            print("Bye! See you next time!")
            break
        else:
            print('Sorry! Invalid Choice. Please try again.')

if __name__ == "__main__":
    main()