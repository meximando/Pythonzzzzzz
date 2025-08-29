# Get user total income
total_income = get_income()

# Record all expenses
expenses = record_expenses()

# Calculate total expenses
total_expenses = calculate_total(expenses)

# Display the summary to the user
print("\n--- Budget Summary ---")
print(f"Total Income: ${total_income:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${total_income - total_expenses:.2f}")
