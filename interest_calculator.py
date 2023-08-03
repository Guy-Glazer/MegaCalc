def calculate_interest(yearly_interest, deposit_amount, total_days, withdrawal_days):
    interest_per_day = yearly_interest / 365
    total_interest = 0
    remaining_days = total_days

    while remaining_days > 0:
        days_for_calculation = min(remaining_days, withdrawal_days)
        total_interest += (deposit_amount + total_interest) * interest_per_day * days_for_calculation
        remaining_days -= days_for_calculation

    return total_interest

if __name__ == "__main__":
    yearly_interest = float(input("Yearly interest rate (%): ")) / 100
    deposit_amount = float(input("Deposit amount: "))
    total_days = int(input("Total number of days: "))
    withdrawal_days = int(input("Number of days until withdrawal possibility: "))

    total_interest = calculate_interest(yearly_interest, deposit_amount, total_days, withdrawal_days)
    print(f"Total interest accumulated: {total_interest:.2f}")
