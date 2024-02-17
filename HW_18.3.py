

# Apply the decorator to the transaction function
@decorator
def transaction(deposit, amount):
    return deposit, amount