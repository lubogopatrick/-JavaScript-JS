def calculate_total_amount(principal, days):
    # Constants
    interest_rate = 0.10
    fine_rate = 0.01

    # Calculate interest
    interest = principal * interest_rate

    # Calculate fine
    fine = 0
    if days > 30:
        fine = (days - 30) * (principal * fine_rate)

    # Calculate total amount
    total_amount = principal + interest + fine
    return total_amount

# Example usage
principal_amount = 1000  # Principal loan amount
days_passed = 45  # Number of days passed

total_paid = calculate_total_amount(principal_amount, days_passed)
print(f"Total amount paid by the client after {days_passed} days: ${total_paid:.2f}")
