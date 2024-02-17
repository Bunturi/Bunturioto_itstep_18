# Define the decorator function
def decorator(func):
    # Define the wrapper function inside the decorator
    def wrapper(num):
        # Check if the number is not positive
        # Raise a ValueError if is not
        if num <= 0:
            raise ValueError("The number must be positive")
        else:
            print(num)
        return func(num)

    return wrapper



# Apply the decorator to the function is_positive
@decorator
def is_positive(num):
    # Simply return the number
    return num