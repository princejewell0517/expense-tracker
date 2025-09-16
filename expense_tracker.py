# expense_tracker.py

# Simple Expense Tracker by Prince Hickman

expenses = {}

def add_expense(category, amount):
    if category in expenses:
        expenses[category] += amount
    else:
        expenses[category] = amount

def show_expenses():
    print("\n--- Expense Summary ---")
    total = 0
    for category, amount in expenses.items():
        print(f"{category}: ${amount:.2f}")
        total += amount
    print(f"Total Expenses: ${total:.2f}\n")

print("Welcome to the Expense Tracker!")
while True:
    print("1. Add Expense")
    print("2. Show Expenses")
    print("3. Exit")
    choice = input("Choose an option (1/2/3): ")

    if choice == "1":
        category = input("Enter category (Food, Travel, etc.): ")
        try:
            amount = float(input("Enter amount: "))
            add_expense(category, amount)
            print(f"Added ${amount:.2f} to {category}.")
        except ValueError:
            print("❌ Please enter a valid number.")
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        print("Goodbye! 👋")
        break
    else:
        print("Invalid choice, please try again.")
