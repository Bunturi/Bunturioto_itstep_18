# Define a decorator function
def decorator(func):
    def wrapper(deposit, amount):
        # Set a commission fee
        commission = 1
        # Check if the deposit after deducting the commission fee
        # is sufficient for the transaction amount if not rise ValueError
        if deposit - commission >= amount:
            return "Payment completed successfully"
        else:
            raise ValueError("There is insufficient amount in the account")


# Apply the decorator to the transaction function
@decorator
def transaction(deposit, amount):
    return deposit, amount