initial_savings = int(input("Enter your initial savings amount: "))
monthly_savings = int(input("Enter the monthly amount you plan to save: "))
months = int(input("Enter the number of months to calculate savings for: "))
total_savings = initial_savings
for month in range(1, months + 1):
    total_savings += monthly_savings
    print(f"Total savings after month {month}: {total_savings:.2f}")