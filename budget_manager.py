#This program helps users manage their monthly budget by tracking income and categorized expenses.

#Function to get user's monthly income with error handling
def get_income():
    while True:
        try:
            income = float(input("Enter your total income for the month: $"))
            if income < 0:
                print("Income cannot be negative. Try again.")
                continue
            return income
        except ValueError:
            print("Invalid input. Please enter a number.")

#Function to record expenses with categories and validation
def record_expenses():
    expenses = []  # List to store (amount, category) tuples
    while True:
        try:
            amount = float(input("Enter an expense amount (or -1 to stop): $"))
            if amount == -1:
                break
            if amount < 0:
                print("Expense cannot be negative. Please try again.")
                continue
            category = input("Enter the category for this expense (e.g., rent, food, entertainment): ")
            expenses.append((amount, category))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return expenses

# Function to calculate total expenses
def calculate_total(expenses):
    return sum(amount for amount, _ in expenses)

# Function to summarize expenses by category
def categorize_expenses(expenses):
    category_totals = {}
    for amount, category in expenses:
        if category in category_totals:
            category_totals[category] += amount
        else:
            category_totals[category] = amount
    return category_totals

# Main function to run the program
def main():
    print("Welcome to the Budgeting Tool!")
    
    # Get user income
    total_income = get_income()
    
    # Get list of expenses from the user
    expenses = record_expenses()
    
    # Calculate total expenses
    total_expenses = calculate_total(expenses)
    
    # Calculate remaining balance
    remaining_balance = total_income - total_expenses
    
    # Categorize and summarize expenses
    category_summary = categorize_expenses(expenses)
    # Finally Worked
    # Display results
    print("\n--- Budget Summary ---")
    print(f"Total Income: ${total_income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${remaining_balance:.2f}\n")
    
    print("--- Expense Breakdown by Category ---")
    for category, total in category_summary.items():
        print(f"{category.title()}: ${total:.2f}")
    
    print("\nThank you for using the budgeting tool!")

# Ensure the main function runs
if __name__ == "__main__":
    main()
